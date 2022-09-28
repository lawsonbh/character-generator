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

class Morph(models.Model):
    name = models.CharField(max_length=50)
    mtype = models.CharField("Morph Type",max_length=50)
    cost = models.IntegerField()
    avail = models.IntegerField("Availability")
    wt = models.IntegerField("Wound Threshold")
    dur = models.IntegerField("Durability")
    dr = models.IntegerField("Death Rating")
    ins = models.IntegerField("Insight")
    mox = models.IntegerField("Moxie")
    vig = models.IntegerField("Vigor")
    flex = models.IntegerField()
    movtype = models.CharField("Movement System",max_length=20)
    mov_base = models.IntegerField("Movement Base Rate")
    mov_full = models.IntegerField("Movement Full Rate")

class Item(models.Model):
    name = models.CharField(max_length=100)
    complexity_gp = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

