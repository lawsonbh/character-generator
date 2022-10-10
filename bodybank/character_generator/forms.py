from django.forms import ModelForm, Form, ModelChoiceField
from character_generator.models import Ego, Morph, Background, Career


class EgoForm(ModelForm):
    class Meta:
        model = Ego
        fields = ["name", "cog", "inte", "ref", "sav", "som", "wil"]


class CharacterSheetForm(Form):
    ego = ModelChoiceField(queryset=Ego.objects.all())
    morph = ModelChoiceField(queryset=Morph.objects.all())
    background = ModelChoiceField(queryset=Background.objects.all())
    career = ModelChoiceField(queryset=Career.objects.all())
