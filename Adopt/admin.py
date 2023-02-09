from django.contrib import admin
from Adopt import models

# Register your models here.

class RaceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class KindOfPetAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class AnimalAdmin(admin.ModelAdmin):
    list_display =('name','age','birth_date','race')
    list_filter = ('race','age')

    readonly_fields = ('created','updated')

class PersonInformationAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')



admin.site.register(models.Race,RaceAdmin)
admin.site.register(models.KindOfPet,KindOfPetAdmin)
admin.site.register(models.Animal,AnimalAdmin)
admin.site.register(models.PersonInformation,PersonInformationAdmin)



