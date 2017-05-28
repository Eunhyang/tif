from django import forms
from django.forms import ModelForm, Textarea, TextInput, ChoiceField
from .models import Time, Activity, Feeling, Memo

class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = (
            "title",
            "content"
        )
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "content": Textarea(attrs={"class":"form-control"}),
        }
