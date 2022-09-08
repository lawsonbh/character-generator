from django.db import models

class Ego(models.Model):
    ego_name = models.CharField(max_length=50)
    ego_cog_apt = models.IntegerField("Cognition (COG)")
    ego_int_apt = models.IntegerField("Intuition (INT)")
    ego_ref_apt = models.IntegerField("Reflex (REF)")
    ego_sav_apt = models.IntegerField("Savy (SAV)")
    ego_som_apt = models.IntegerField("Somatics (SOM)")
    ego_wil_apt = models.IntegerField("Willpower (WIL)")
    ego_flex = models.IntegerField("Ego Flex Bonus")
    ego_a_rep = models.IntegerField("@-rep")
    ego_c_rep = models.IntegerField("c-rep")
    ego_f_rep = models.IntegerField("f-rep")
    ego_g_rep = models.IntegerField("g-rep")
    ego_i_rep = models.IntegerField("i-rep")
    ego_r_rep = models.IntegerField("r-rep")
    ego_x_rep = models.IntegerField("x-rep")

class Morph(models.Model):
    egos = models.ManyToManyField(Ego)
    morph_name = models.CharField(max_length=50)
    morph_type = models.CharField(max_length=50)
    morph_cost = models.IntegerField()


class Item(models.Model):
    egos = models.ManyToManyField(Ego)
    item_name = models.CharField(max_length=100)
    item_complexity_gp = models.CharField(max_length=20)
    item_description = models.CharField(max_length=200)

class Character_Sheet(models.Model):
    ego = models.ForeignKey(Ego, on_delete=models.CASCADE)
    initiative = models.IntegerField("Initiative (INIT)")
    wound_threshold = models.IntegerField("Wound Threshold (WT)")
    durability = models.IntegerField("Durability (DUR)")
    death_rating = models.IntegerField("Death Rating (DR)")
    trauma_threshold = models.IntegerField("Trauma Threshold (TT)")
    lucidity = models.IntegerField("Lucidity (LUC)")
    insanity_rating = models.IntegerField("Insanity Rating (IR)")
    insight_pool = models.IntegerField()
    moxie_pool = models.IntegerField()
    vigor_pool = models.IntegerField()
    flex_pool = models.IntegerField()
    infection_rating = models.IntegerField("Infection Rating")
