from django import forms
from iplapp.models import Team

class ModelTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'owner' : forms.TextInput(attrs={'class' : 'form-control'}),
            'home_city' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

