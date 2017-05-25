from django import forms
from django.forms import ModelForm, Textarea, TextInput, ChoiceField
from .models import Time, Activity, Feeling, Memo

class TimeForm(ModelForm):
    category = forms.ChoiceField(choices=Feeling.CATEGORY_CHOICES)
    class Meta:
        model = Time
        fields = (
            "name",
            "activity",
            "memo"
        )
        widgets = {
            "name": TextInput(attrs={"class":"form-control"}),
            "activity": TextInput(attrs={"class":"form-control"}),
            "memo": Textarea(attrs={"class":"form-control"}),
            # "category": ChoiceField(attrs={"class":"form-control"}),
        }
