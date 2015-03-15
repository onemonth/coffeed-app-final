from django.contrib import admin
import core.models as coremodels
# Register your models here.

admin.site.register(coremodels.Location)
admin.site.register(coremodels.Review)