from django import forms
from django.forms import inlineformset_factory
from .models import Round, HoleStat, Putt


class RoundForm(forms.ModelForm):
    class Meta:
        model = Round
        fields = ["date", "course_name", "tee_name", "notes"]


class HoleStatForm(forms.ModelForm):
    class Meta:
        model = HoleStat
        fields = [
            "par",
            "distance_in_yards",
            "gir_hit",
        ]
        widgets = {
            "par": forms.NumberInput(attrs={"class": "form-control"}),
            "distance_in_yards": forms.NumberInput(attrs={"class": "form-control"}),
            "gir_hit": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


PuttFormSet = inlineformset_factory(
    HoleStat,
    Putt,
    fields=["putt_number", "distance_ft", "made"],
    extra=3,
    can_delete=False
)