from django.contrib import admin
from .models import Ego, Morph


class EgoAdmin(admin.ModelAdmin):
    pass

class MorphAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ego, EgoAdmin)
admin.site.register(Morph, MorphAdmin)
