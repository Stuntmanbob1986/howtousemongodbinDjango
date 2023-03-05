from django import forms
from django.forms import ModelForm
from .models import binanceData


class DateInput(forms.DateInput):
    input_type = 'date'


class PromiseForm(ModelForm):
    class Meta:
        model = binanceData
        fields = ['coinpair', 'accuracy', 'start', 'end']
        widgets = {
            'start': DateInput(),
            'end': DateInput()
        }
