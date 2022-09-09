from django.db import models

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

class Morph(models.Model):
    name = models.CharField(max_length=50)
    mtype = models.CharField(max_length=50)
    cost = models.IntegerField()

class Item(models.Model):
    name = models.CharField(max_length=100)
    complexity_gp = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
