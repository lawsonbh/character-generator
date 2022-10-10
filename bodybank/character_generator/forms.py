from django.forms import ModelForm, Form, ModelChoiceField
from character_generator.models import CharacterSheet, Ego, Morph, Background, Career


class EgoForm(ModelForm):
    class Meta:
        model = Ego
        fields = ["name", "cog", "inte", "ref", "sav", "som", "wil"]


class CharacterSheetForm(ModelForm):
    class Meta:
        model = CharacterSheet
        fields = ["ego", "morph", "background", "career"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")  # do before calling super()
        super().__init__(*args, **kwargs)
        self.fields["ego"].queryset = Ego.objects.filter(user=self.user)
