from django import forms
from .models import Contestant

class ContestantForm(forms.ModelForm):
    class Meta:
        model = Contestant
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'pronouns': forms.Select(),  # <-- use Select instead of CheckboxSelectMultiple
            'social_handles': forms.Textarea(attrs={'rows': 3}),
            'how_did_you_hear': forms.Textarea(attrs={'rows': 2}),
            'employer_feelings': forms.Textarea(attrs={'rows': 2}),
            'know_anyone': forms.Textarea(attrs={'rows': 2}),
            'prior_url': forms.URLInput(attrs={'placeholder': 'If yes, paste URL'}),
        }
