from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin
from django.conf import settings



# Register your models here.
class PointAdmin(LeafletGeoAdmin):
    # fields to show in admin listview
    list_display = ('nome_prova', 'tipo_prova')

admin.site.register(prove_geognostiche,PointAdmin)
