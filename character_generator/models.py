from django.db import models


class User(models.Model):
    ##TODO: A user has many egos
    pass

class Ego(models.Model):
    ##TODO: An Ego has many morphs and many items
    pass

class Morph(models.Model):
    ##TODO: A morph has many egos
    pass

class Item(models.Model):
    ##TODO: An item has many egos
