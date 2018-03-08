from django.db import models
from django.utils.translation import ugettext_lazy as _
# from parlhand.extra.multi_field import MultiColumnField
import datetime

# Forked from https://gist.github.com/gipi/2401143
# look also
# https://github.com/dcramer/django-ratings/blob/master/djangoratings/fields.py

from django.core.exceptions import ValidationError
from django.db.models import Field, CharField

__all__ = ['MultiColumnField']

try:
    from hashlib import md5
except ImportError:
    from md5 import new as md5

def _make_property(self, field_name):
    def _get_amount(self, default=None):
        return getattr(self.instance, field_name, default)
    def _set_amount(self, value):
        return setattr(self.instance, field_name, value)
    return property(_get_amount, _set_amount)

def _generate_instance_class(owner_field):
    class MultiColumnFieldInstance(object):
        """
        Represents a single instance of a MultiColumnField on an object, by
        keeping track of both a reference to the parent instance and a
        reference to the MultiColumnField-derived class. This allows for 
        "natural" access to the subfield values by using properties.
        """
        def __init__(self, instance, field):
            self.content_type = None
            self.instance = instance
            self.field = field
            self.names = owner_field.names

            for name in self.names:
                prop = _make_property(self, self.field.field_names[name])
                setattr(MultiColumnFieldInstance, name, prop)

        def to_dict(self):
            d = {}
            for name in self.names:
                d[name] = getattr(self.instance, self.field.field_names[name], None)
            return d

        def __repr__(self):
            return self.field._instance_repr(self)

    return MultiColumnFieldInstance

class MultiColumnField(Field):
    fields = None
    "A field containing multiple sub-fields and spanning multiple columns"
    def __init__(self, *args, **kwargs):
        if not self.fields:
            self.fields = kwargs.pop('fields', None)
        if not self.fields:
            raise ValidationError("no fields attribute or argument provided")
        super(MultiColumnField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        self.name = name
        self.key = md5(self.name).hexdigest()
        self.names = self.fields.keys()        # Names we want to call the fields
        self.field_names = {}                  # What they are internally named

        # Add all of the 'real' fields to the class, cache the calc'd field names
        for suffix,field in self.fields.items():
            field_name = "%s_%s" % (self.name, suffix)
            self.field_names[suffix] = field_name
            cls.add_to_class(field_name, field)

        # Generate the 'instance class' for this MCF-derived class
        self.instance_class = _generate_instance_class(self)

        # Add this field as a class member
        setattr(cls, name, self)

    def get_db_prep_save(self, value):
        pass

    def get_db_prep_lookup(self, lookup_type, value):
        raise NotImplementedError(self.get_db_prep_lookup)

    def __get__(self, instance, type=None):
        """
        Accessor wrapper for a MultiColumnField, to allow for on-the-fly
        MultiColumnFieldInstance generation when used outside of the class.
        """
        if instance is None:
            return self
        # TODO: Add caching here
        return self.instance_class(instance, self)

    def __set__(self, instance, value):
        "sets all values in a MultiColumnField at once"
        if isinstance(value, self.instance_class):
            # TODO: Use added cache here
            temp_field_instance = self.instance_class(instance, self)
            for name in self.names:
                setattr(temp_field_instance, name, getattr(value, name, None))
        elif isinstance(value, dict):
            temp_field_instance = self.instance_class(instance, self)
            for name in self.names:
                setattr(temp_field_instance, name, value[name])
        else:
            raise TypeError

    def _instance_repr(self, instance):
        """
        A stock implementation of the __repr__ function for a generated instance of
        a MultiColumnField-derived class. The generated instance class uses the 
        parent class' __instance_repr__ function to allow for easy overriding.
        """
        return "<'%s' field (MultiColumnField) on instance '%s'>" % (self.name, instance.instance.__repr__())


class ConfidenceDate(MultiColumnField):
    def __init__(self, *args, **kwargs):
        args
        help_text = kwargs.get('help_text','An uncertain date')
        kwargs['fields'] = {
            'date_of_%s': models.DateField(null=True, blank=True, help_text=help_text),
            'date_of_%s_confidence': models.CharField(max_length=200,
                null=True,
                default="YYYY-MM-DD",
                help_text="The confidence of "+help_text.lower()+". Use 'YYYY','YYYY-MM' or 'YYYY-MM-DD'"
            ),
        }
        super(ConfidenceDate, self).__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if value is None or value == "":
            value = None
            confidence = ""
        else:
            value = str(value)
            confidence = 'YYYY-MM-DD'[0:len(value)]
            value = datetime.date( *map(int,(value+'-01-01')[0:10].split('-')) )
        value = {'date':value, 'confidence':confidence}
        super(ConfidenceDate,self).__set__(instance, value)

    def contribute_to_class(self, cls, name):
        self.name = name
        self.key = md5(self.name.encode('utf-8')).hexdigest()
        self.names = self.fields.keys()        # Names we want to call the fields
        self.field_names = {}                  # What they are internally named

        # Add all of the 'real' fields to the class, cache the calc'd field names
        for pattern,field in self.fields.items():
            field_name = pattern % (self.name,)
            self.field_names[pattern] = field_name
            cls.add_to_class(field_name, field)

        # Generate the 'instance class' for this MCF-derived class
        self.instance_class = _generate_instance_class(self)

        # Add this field as a class member
        setattr(cls, name, self)
