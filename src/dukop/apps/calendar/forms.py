from django import forms
from django.forms.formsets import formset_factory

from . import models


class EventForm(forms.ModelForm):

    class Meta:
        model = models.Event
        fields = ('name', 'description', 'host', 'venue_name', 'street', 'zip_code', 'city')


class EventTimeForm(forms.ModelForm):

    class Meta:
        model = models.EventTime
        fields = ('start', 'end')


EventTimeFormSet = formset_factory(EventTimeForm, extra=5, max_num=5)
