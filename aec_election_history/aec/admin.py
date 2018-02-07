from django.contrib import admin

from aec import models

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'date_of_death', 'country_of_birth')
    search_fields = ['name', 'notes']
    ordering = ['name']

# admin.site.register(models.Person, PersonAdmin)

class VoterRecordInline(admin.TabularInline):
    model = models.VoterRecord

@admin.register(models.Election)
class ElectionAdmin(admin.ModelAdmin):
    inlines = [
        VoterRecordInline,
    ]

admin.site.register(models.Division)

admin.site.register(models.FirstPreferenceVotes)
