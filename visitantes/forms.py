from django import forms
from .models import Visitante
from typing_extensions import Required


class VisitanteForm(forms.ModelForm):
    's'