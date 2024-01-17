from django import forms
from django.core.exceptions import ValidationError
from django.forms import Select

from myapp.models import Passangers_and_Flights
class TicketForm(forms.ModelForm):
    class Meta:
        model = Passangers_and_Flights
        fields = ("with_baggage","baggage_weight","id_flight","extra_service")
    def clean_baggage_weight(self):
        baggage_weight = self.cleaned_data['baggage_weight']
        with_bagggage = self.cleaned_data['with_baggage']
        if with_bagggage==False and baggage_weight>0:
            raise ValidationError("Please, tick the baggage YES ")
        elif with_bagggage==True and baggage_weight == 0:
            raise ValidationError("Please, type the weight of your baggage")
        else:
            return self.cleaned_data['baggage_weight']