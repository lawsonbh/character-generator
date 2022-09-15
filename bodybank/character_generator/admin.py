from django.contrib import admin
from .models import Ego


class EgoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ego, EgoAdmin)
