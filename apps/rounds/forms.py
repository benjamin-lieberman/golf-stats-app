from django import forms
from django.forms import inlineformset_factory
from .models import Round, HoleStat, Putt
from apps.reference.models import Club


class RoundForm(forms.ModelForm):
    class Meta:
        model = Round
        fields = ["date", "course_name", "tee_name", "notes"]

        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "course_name": forms.TextInput(attrs={"class": "form-control"}),
            "tee_name": forms.TextInput(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class HoleStatForm(forms.ModelForm):
    class Meta:
        model = HoleStat
        fields = [
            "par",
            "distance_in_yards",
            "gir_hit",
            "pin_position",
        ]

        widgets = {
            "par": forms.NumberInput(attrs={"class": "form-control"}),
            "distance_in_yards": forms.NumberInput(attrs={"class": "form-control"}),
            "gir_hit": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "pin_position": forms.Select(attrs={"class": "form-select"}),
        }


PuttFormSet = inlineformset_factory(
    HoleStat,
    Putt,
    fields=["putt_number", "distance_ft", "made"],
    extra=3,
    can_delete=False,
    widgets={
        "putt_number": forms.NumberInput(attrs={"class": "form-control"}),
        "distance_ft": forms.NumberInput(attrs={"class": "form-control"}),
        "made": forms.CheckboxInput(attrs={"class": "form-check-input"}),
    }
)