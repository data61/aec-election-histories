from django.contrib.contenttypes import fields as generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db import models as gis
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from django.core.serializers import serialize
from django.contrib.gis.db.models import Extent

from aec.utils.fields import ConfidenceDate
from aec.utils import GENDER

class Person(TimeStampedModel):
    """
    A person of interest to the AEC
    """
    class Meta:
        verbose_name_plural="People"

    

    name = models.TextField(_("name"), max_length=512, help_text=_("A person name at their first election"))
    country_of_birth = models.CharField(_("Country of birth"), max_length=256, blank=True, help_text=_("Where they were born"))
    gender = models.CharField(choices=GENDER, default=GENDER.Male, max_length=20)
    birth = ConfidenceDate(help_text=_("A date of birth"))
    death = ConfidenceDate(help_text=_("A date of death"))
    notes = models.CharField(_("notes"), max_length=1024, blank=True, help_text=_("A one-line account of a person's life"))

    def __str__(self):
        return self.name


class AlternateName(models.Model):
    """
    An alternate name for a Person
    """
    person = models.ForeignKey(Person, related_name="other_names", help_text=_("Issued identifiers"))
    name = models.TextField(_("name"), help_text=_("An alternate or former name"))


class Election(models.Model):
    """
    A collection of recorded votes to elect one or more representatives to a 
    parliamentary chamber.
    """
    id = models.CharField(max_length=256, primary_key=True)
    label = models.CharField(max_length=128, help_text=_("The name of the election"))
    type = models.CharField(max_length=128, blank=True, help_text=_("The type of election, eg. Full election, By-election, Casual vacancy"))
    poll_date = models.DateField(help_text="The date an election was held.")
    notes = models.TextField(null=True,blank=True)
    # distribution = models.OneToOneField(
    #     Redistribution, related_name="results", help_text=_("The election this electorate is for")
    # )
    # parliament = models.ForeignKey('Parliament',null=True,blank=True)

    def __str__(self):
        return self.label


class ElectoralRegion(models.Model):
    name = models.CharField(max_length=1024)
    election = models.ForeignKey(Election, related_name="electorates", help_text=_("The election this electorate is for"))
    #geom = gis.PolygonField(_("geometry"), null=True, blank=True, help_text=_("A geometry"))
    # def extent(self):
    #     ext = self.areas.aggregate(Extent('geom')).get('geom__extent')
    #     if ext:
    #         return list(ext)
    #     else:
    #         return None

    # def as_json(self):
    #     return serialize('geojson', self.areas.all(),
    #       fields=('name','geom','start_date','end_date','time'))


class AustralianState(ElectoralRegion):
    abbreviation = models.CharField(max_length=1024)


class Division(ElectoralRegion):
    """
    A division for an election held by one or more parliamentarians.
    This entity records the abstract concept of an electorate, rather than a specific
    geographic area as an electorate can change boundaries over time.
    
    Electoral boundaires are stored with a time period in the "ElectorateArea" relation.
    
    For the Australian context, the 'state' of an electorate is recorded as a parent area
    attached to an ElectoralArea.
    """
    # class Meta:
    #     unique_together = ('name', 'election')

    state = models.CharField(max_length=1024)


    @property
    def winner(self):
        # print(self.results.objects.filter.order_by('votes').first().person)
        return PreferencesFlow.objects.filter(division=self).order_by('-stage_of_counts', '-votes').first().person
        # return ElectionResult.objects.filter(electorate=self).order_by('-stage_of_counts', '-votes').first().person

    @property
    def is_uncontested(self):
        return PreferencesFlow.objects.filter(division=self).count() == 1


class Subdivision(ElectoralRegion):
    parent_division = models.ForeignKey(Division, related_name="subdivisions")
    level = models.CharField(max_length=256)


class FirstPreferenceVotes(models.Model):
    """
    A record of the 1st preferences result of an election for an individual.
    """
    region = models.ForeignKey(ElectoralRegion, related_name="results")
    #area = models.CharField(max_length=512)
    vote_type = models.CharField(max_length=512, default="Ordinary")
    person = models.ForeignKey(
        Person,
        help_text="The relation to a person associated with this result."
    )
    votes = models.PositiveIntegerField(default=0)
    notes = models.TextField(null=True,blank=True)

    class meta:
        verbose_name_plural = "First Preference Votes"

class PreferencesFlow(models.Model):
    """
    A record of preference flows for an election for a particular indivi    dual, recorded as a number.
    """
    class Meta:
        ordering = ['stage_of_counts', '-votes']

    division = models.ForeignKey(
        Division, related_name="flows",
        help_text="Division the votes were recorded against."
    )
    person = models.ForeignKey(
        Person,
        help_text="The person associated with a preferences result."
    )
    votes = models.PositiveIntegerField(
        default=0,
        help_text="The total number of votes for an individual at a particular stage of counts"
    )
    stage_of_counts = models.PositiveIntegerField(
        default=0,
        help_text="The stage at which these counts are held. Stages start at 0, and the count increments when the lowest unsuccessful candidate is illiminated and their votes redistributed."
    )



class Party(models.Model):
    """
    An Australian political party that is (or has been) registered with the Australian Electoral Commission

    Parties are often branded with colours in both Party and AEC material, e.g. Labor is often associated with red.
    Colors for parties are recorded for use in presentation where appropriate.
    Colours should be "CSS" safe, eg. Hexidecimal or named HTML web colours.

    Note: Primary/Secondary may not always equate to Foreground/Background text colours during presentation,
    however colours should be readable when used in this fashion.
    """
    class Meta:
        verbose_name_plural="Parties"

    name = models.CharField(_("name"), max_length=512, help_text=_("A primary name, e.g. a legally recognized name"))
    summary = models.CharField(_("summary"), max_length=1024, blank=True, help_text=_("A one-line description of an organization"))
    code = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.name


class PartyMembership(models.Model):
    """
    The record of a persons membership within a political party.
    """
    party = models.ForeignKey(Party)
    start = ConfidenceDate()
    end = ConfidenceDate()
    person = models.ForeignKey('Person', related_name='party_memberships', help_text=_("The person who is a party to the relationship"))


class VoterRecord(models.Model):
    election = models.ForeignKey(Election)
    region = models.ForeignKey(ElectoralRegion)
    gender = models.CharField(choices=GENDER, default=GENDER.Male, max_length=20)
    enrolments = models.PositiveIntegerField(default=0)
    votes_issued = models.PositiveIntegerField(default=0)
