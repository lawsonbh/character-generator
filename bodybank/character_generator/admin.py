from django.contrib import admin
from .models import (
    Ego,
    Movement,
    Morph,
    Background,
    Skill,
    Background2Skills,
    Career,
    Career2Skills,
    Item,
)


class EgoAdmin(admin.ModelAdmin):
    pass


class MovementAdmin(admin.ModelAdmin):
    pass


class MorphAdmin(admin.ModelAdmin):
    pass


class BackgroundAdmin(admin.ModelAdmin):
    pass


class SkillAdmin(admin.ModelAdmin):
    pass


class Background2SkillsAdmin(admin.ModelAdmin):
    pass


class CareerAdmin(admin.ModelAdmin):
    pass


class Career2SkillsAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "itype", "complexity_gp", "desc")


admin.site.register(Ego, EgoAdmin)
admin.site.register(Movement, MovementAdmin)
admin.site.register(Morph, MorphAdmin)
admin.site.register(Background, BackgroundAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Background2Skills, Background2SkillsAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Career2Skills, Career2SkillsAdmin)
