import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


from aec import models


class Person(DjangoObjectType):
    class Meta:
        model = models.Person
        filter_fields = ['name',]
        interfaces = (graphene.relay.Node, )


class FirstPreferenceVotes(DjangoObjectType):
    class Meta:
        filter_fields = ['vote_type',]
        model = models.FirstPreferenceVotes
        interfaces = (graphene.relay.Node, )

class PreferencesFlow(DjangoObjectType):
    class Meta:
        model = models.PreferencesFlow
        interfaces = (graphene.relay.Node, )


class Division(DjangoObjectType):
    winner = graphene.Field(Person, source='winner')
    is_uncontested = graphene.Boolean(source='is_uncontested')
    class Meta:
        model = models.Division
        interfaces = (graphene.relay.Node, )


class Election(DjangoObjectType):
    # electorates = graphene.List(Electorate) #source='electorates')
    class Meta:
        model = models.Election
        filter_fields = ['id',]
        interfaces = (graphene.relay.Node, )



class Party(DjangoObjectType):
    class Meta:
        model = models.Party
        interfaces = (graphene.relay.Node, )

class PartyMembership(DjangoObjectType):
    class Meta:
        model = models.PartyMembership

class Query(graphene.ObjectType):
    people = DjangoFilterConnectionField(Person)
    results = graphene.List(FirstPreferenceVotes)
    elections = DjangoFilterConnectionField(Election)

    @graphene.resolve_only_args
    def resolve_results(self):
        return models.FirstPreferenceVotes.objects.all()

    # @graphene.resolve_only_args
    # def resolve_people(self):
    #     return models.Person.objects.all()

schema = graphene.Schema(query=Query)
