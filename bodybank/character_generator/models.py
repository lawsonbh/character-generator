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
    morph = models.ForeignKey("Morph",null=True,on_delete=models.CASCADE)
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
        (WALKER, 'Walker'),
        (WINGED, 'Winged'),
        (SWIM, 'Swim'),
        (THRUST_VECTOR, 'Thrust Vector'),
        (HOPPER, 'Hopper'),
        (ROTOR, 'Rotor'),
        (IONIC, 'Ionic'),
        (WHEELED, 'Wheeled')
    ]
    name = models.CharField("Movement Name", max_length=30, choices=MOVEMENT_NAME_CHOICES, default=WALKER)
    base = models.IntegerField(default=0)
    full = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Morph(models.Model):
    name = models.CharField(max_length=50,null=True)
    desc = models.TextField("Morph Description",default="")
    COMMON = "Common"
    POD = "Pod"
    UPLIFT = "Uplift"
    SYNTHMORPH = "Synth"
    INFOMORPH = "Info"
    MORPH_TYPE_CHOICES = [
        (COMMON, 'Common'),
        (POD, 'Pod'),
        (UPLIFT, 'Uplift'),
        (SYNTHMORPH, 'Synth Morph'),
        (INFOMORPH, 'Info Morph')
    ]
    mtype = models.CharField("Morph Type",max_length=30,choices=MORPH_TYPE_CHOICES,default=COMMON)
    cost = models.IntegerField(default=0)
    avail = models.IntegerField("Availability",default=0)
    wt = models.IntegerField("Wound Threshold",default=0)
    dur = models.IntegerField("Durability",default=0)
    dr = models.IntegerField("Death Rating",default=0)
    ins = models.IntegerField("Insight",default=0)
    mox = models.IntegerField("Moxie",default=0)
    vig = models.IntegerField("Vigor",default=0)
    flex = models.IntegerField(default=0)
    movtype = models.ManyToManyField(Movement, related_name='movement_systems')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    complexity_gp = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
