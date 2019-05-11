from django.shortcuts import render
from django.views.generic.edit import CreateView

from . import forms
from . import models


def index(request):
    return render(request, "calendar/index.html")


class EventCreate(CreateView):

    template_name = 'calendar/event/create.html'
    model = models.Event
    form_class = forms.EventForm

    def get_context_data(self, **kwargs):
        c = CreateView.get_context_data(self, **kwargs)
        c['times'] = forms.EventTimeFormSet()
        return c
