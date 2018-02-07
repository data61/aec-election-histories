"""
We tried and failed to get django-popolo to work. But couldn't. So we're replicating the bits we like here.
"""    
from django.contrib.contenttypes import fields as generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db import models as gis
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel


from aec.utils.fields import ConfidenceDate


class Membership(models.Model):
    """
    A relationship between a person and an organization
    see schema at http://popoloproject.com/schemas/membership.json#
    """
    class Meta:
        abstract = True

    start = ConfidenceDate()
    end = ConfidenceDate()
    person = models.ForeignKey('Person', related_name='memberships', help_text=_("The person who is a party to the relationship"))
