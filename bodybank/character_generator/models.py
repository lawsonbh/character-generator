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
    background = models.ForeignKey("Background",null=True, blank=True)

    def __str__(self):
        return self.name


class Movement(models.Model):
    name = models.CharField(max_length=128)
    base = models.IntegerField(default=0)
    full = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Morph(models.Model):
    name = models.CharField(max_length=50,null=True)
    desc = models.TextField("Morph Description",default="")
    mtype = models.CharField("Morph Type",max_length=50,default="")
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


class Ego2Morph(models.Model):
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    ego = models.ForeignKey(Ego, related_name='ego_history', on_delete=models.CASCADE)
    morph = models.ForeignKey(Morph, related_name='morph_history', null=True, on_delete=models.deletion.SET_NULL)

class Background(models.Model):
    pass

class Skill(models.Model):
    pass


class Background2Skills(models.Model):
    background = models.ForeignKey(Background, related_name='background_to_skill', on_delete=models.CASCADE)
    skills = models.ForeignKey(Skill, related_name='skill_to_background', on_delete=models.CASCADE)
    modifier = models.PositiveIntegerField(default=0)
