from django.contrib import admin
from .models import Ego, Movement, Morph


class EgoAdmin(admin.ModelAdmin):
    pass

class MovementAdmin(admin.ModelAdmin):
    pass

class MorphAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ego, EgoAdmin)
admin.site.register(Movement, MovementAdmin)
admin.site.register(Morph, MorphAdmin)
