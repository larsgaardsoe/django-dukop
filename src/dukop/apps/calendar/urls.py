from django.urls import path

from . import views


app_name = 'calendar'

urlpatterns = [
    path("", views.index),
    path("event/create", views.EventCreate.as_view(), name="event_create"),
]
