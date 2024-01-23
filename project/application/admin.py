from django.contrib import admin
from . import models

admin.site.register(models.Main)
admin.site.register(models.DemandChart)
admin.site.register(models.GeoChart)
admin.site.register(models.Skills)
