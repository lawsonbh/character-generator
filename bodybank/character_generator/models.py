from ssl import OP_ENABLE_MIDDLEBOX_COMPAT
from unicodedata import category
from django.db import models
from django.forms import ModelForm
from django.conf import settings


class Ego(models.Model):
    name = models.CharField(max_length=50)
    cog = models.IntegerField("Cognition (COG)")
    inte = models.IntegerField("Intuition (INT)")
    ref = models.IntegerField("Reflex (REF)")
    sav = models.IntegerField("Savy (SAV)")
    som = models.IntegerField("Somatics (SOM)")
    wil = models.IntegerField("Willpower (WIL)")
    items = models.ManyToManyField("Item")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Movement(models.Model):
    WALKER = "Walker"
    WINGED = "Winged"
    SWIM = "Swim"
    THRUST_VECTOR = "Thrust Vector"
    HOPPER = "Hopper"
    ROTOR = "Rotor"
    IONIC = "Ionic"
    WHEELED = "Wheeled"
    MOVEMENT_NAME_CHOICES = [
        (WALKER, WALKER),
        (WINGED, WINGED),
        (SWIM, SWIM),
        (THRUST_VECTOR, THRUST_VECTOR),
        (HOPPER, HOPPER),
        (ROTOR, ROTOR),
        (IONIC, IONIC),
        (WHEELED, WHEELED),
    ]
    name = models.CharField(
        "Movement Name", max_length=30, choices=MOVEMENT_NAME_CHOICES, default=WALKER
    )
    base = models.IntegerField(default=0)
    full = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Morph(models.Model):
    name = models.CharField(max_length=50, null=True)
    desc = models.TextField("Morph Description", default="")
    COMMON = "Common"
    POD = "Pod"
    UPLIFT = "Uplift"
    SYNTHMORPH = "Synth"
    INFOMORPH = "Info"
    MORPH_TYPE_CHOICES = [
        (COMMON, COMMON),
        (POD, POD),
        (UPLIFT, UPLIFT),
        (SYNTHMORPH, SYNTHMORPH),
        (INFOMORPH, INFOMORPH),
    ]
    mtype = models.CharField(
        "Morph Type", max_length=30, choices=MORPH_TYPE_CHOICES, default=COMMON
    )
    cost = models.IntegerField(default=0)
    avail = models.IntegerField("Availability", default=0)
    wt = models.IntegerField("Wound Threshold", default=0)
    dur = models.IntegerField("Durability", default=0)
    dr = models.IntegerField("Death Rating", default=0)
    ins = models.IntegerField("Insight", default=0)
    mox = models.IntegerField("Moxie", default=0)
    vig = models.IntegerField("Vigor", default=0)
    flex = models.IntegerField(default=0)
    movtype = models.ManyToManyField(Movement, related_name="movement_systems")

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    COMMON_TECH = "Common Tech & Ware"
    MISSION_GEAR = "Mission Gear"
    ITEM_TYPE_CHOICES = [(COMMON_TECH, COMMON_TECH), (MISSION_GEAR, MISSION_GEAR)]
    itype = models.CharField(
        "Item Type", max_length=30, choices=ITEM_TYPE_CHOICES, default=COMMON_TECH
    )
    complexity_gp = models.CharField(max_length=20)
    desc = models.TextField("Description", default="")

    def __str__(self):
        return self.name


class Ego2Morph(models.Model):
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    ego = models.ForeignKey(Ego, related_name="ego_history", on_delete=models.CASCADE)
    morph = models.ForeignKey(
        Morph,
        related_name="morph_history",
        null=True,
        on_delete=models.deletion.SET_NULL,
    )


class Background(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField("Description", default="")

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField("Description", default="")

    def __str__(self):
        return self.name


class Background2Skills(models.Model):
    background = models.ForeignKey(
        Background, related_name="background_to_skill", on_delete=models.CASCADE
    )
    skills = models.ForeignKey(
        Skill, related_name="skill_to_background", on_delete=models.CASCADE
    )
    modifier = models.PositiveIntegerField(default=0)

    def __str__(self):

        return " ".join([str(self.background), str(self.skills), str(self.modifier)])


class Career(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField("Description", default="")

    def __str__(self):
        return self.name


class Career2Skills(models.Model):
    career = models.ForeignKey(
        Career, related_name="career_to_skill", on_delete=models.CASCADE
    )
    skills = models.ForeignKey(
        Skill, related_name="skill_to_career", on_delete=models.CASCADE
    )
    modifier = models.PositiveIntegerField(default=0)

    def __str__(self):
        return " ".join([str(self.career), str(self.skills), str(self.modifier)])


class CharacterSheet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ego = models.ForeignKey(Ego, related_name="character_ego", on_delete=models.CASCADE)
    morph = models.ForeignKey(
        Morph, related_name="character_morph", on_delete=models.CASCADE
    )
    background = models.ForeignKey(
        Background, related_name="character_background", on_delete=models.CASCADE
    )
    career = models.ForeignKey(
        Career, related_name="character_career", on_delete=models.CASCADE
    )

    def __str__(self):
        return " ".join([str(self.ego), str(self.morph)])
