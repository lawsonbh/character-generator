from django.forms import ModelForm
from character_generator.models import Ego

class EgoForm(ModelForm):
    class Meta:
        model = Ego
        fields = ['name','cog','inte','ref','sav','som','wil']

