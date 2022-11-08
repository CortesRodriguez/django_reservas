from dataclasses import fields
from django import forms
from gestion_APP.models import Reserva

class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'