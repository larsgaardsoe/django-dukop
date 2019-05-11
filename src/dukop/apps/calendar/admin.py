from django.contrib import admin

from . import models


class EventTimeInline(admin.TabularInline):
    model = models.EventTime


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [EventTimeInline]


class EventInlineAdmin(admin.TabularInline):
    model = models.Event
    list_display = ("name",)


@admin.register(models.Interval)
class IntervalAdmin(admin.ModelAdmin):

    inlines = [EventInlineAdmin]
