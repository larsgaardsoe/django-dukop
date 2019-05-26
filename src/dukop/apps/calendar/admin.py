from django.contrib import admin

from . import models


class EventTimeInline(admin.TabularInline):
    model = models.EventTime


class EventImageInlineAdmin(admin.TabularInline):
    model = models.EventImage


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [EventTimeInline, EventImageInlineAdmin]


class EventInlineAdmin(admin.TabularInline):
    model = models.Event


@admin.register(models.Interval)
class IntervalAdmin(admin.ModelAdmin):

    inlines = [EventInlineAdmin]
