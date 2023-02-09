from django.contrib import admin
from . models import Services

# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name','created')
    readonly_fields = ('created','updated')

admin.site.register(Services,ServicesAdmin)