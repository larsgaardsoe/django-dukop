from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name=_("name"),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("description"),
    )

    slug = models.SlugField(
        null=True,
        blank=True,
        verbose_name=_("slug"),
        help_text=_("The part of a URL that is displayed in dukop.dk/event/<slug>/"),
    )

    host = models.ForeignKey(
        'users.Group',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='events',
        help_text=_("A group may host an event and be displayed as the author of the event text.")
    )

    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    link1 = models.URLField(blank=True, null=True)
    link2 = models.URLField(blank=True, null=True)
    link3 = models.URLField(blank=True, null=True)
    link4 = models.URLField(blank=True, null=True)
    link5 = models.URLField(blank=True, null=True)

    is_cancelled = models.BooleanField(default=False)
    show_nb = models.BooleanField(default=False)

    venue_name = models.CharField(
        max_length=255,
        verbose_name=_("venue name"),
        blank=True,
        null=True,
        help_text=_("If left blank, will be copied from host group"),
    )
    street = models.CharField(
        max_length=255,
        verbose_name=_("street"),
        blank=True,
        null=True,
        help_text=_("If left blank, will be copied from host group"),
    )
    city = models.CharField(
        max_length=255,
        verbose_name=_("city"),
        blank=True,
        null=True,
        help_text=_("If left blank, will be copied from host group"),
    )
    zip_code = models.CharField(
        verbose_name=_("zip code"),
        blank=True,
        null=True,
        max_length=16,
        help_text=_("If left blank, will be copied from host group"),
    )

    interval = models.ForeignKey(
        'Interval',
        on_delete=models.PROTECT,
        help_text=_("Repeats the event automatically at some interval"),
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    owner_user = models.ForeignKey(
        'users.User',
        verbose_name=_("owner (user)"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='owned_events',
    )
    owner_group = models.ForeignKey(
        'users.Group',
        verbose_name=_("owner (group)"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='owned_events',
    )

    edit_secret = models.CharField(
        max_length=255,
        verbose_name=_("edit secret"),
        blank=True,
        null=True,
        editable=False,
    )

    view_secret = models.CharField(
        max_length=255,
        verbose_name=_("view secret"),
        blank=True,
        null=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("Event")


class EventTime(models.Model):
    """
    Allows an event to take place at many different times
    """

    event = models.ForeignKey(Event, related_name='times', on_delete=models.CASCADE)
    start = models.DateTimeField(
        verbose_name=_("start"),
    )
    end = models.DateTimeField(
        verbose_name=_("end"),
    )
    comment = models.CharField(
        max_length=255,
        verbose_name=_("comment"),
        help_text=_("Leave blank and nothing will be shown to readers"),
        blank=True,
        null=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Event time")
        ordering = ('start', 'end')


class EventUpdate(models.Model):

    description = models.TextField(
        blank=True,
        verbose_name=_("description"),
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Event time")
        ordering = ('created',)


class EventImage(models.Model):

    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Allowed formats: JPEG, PNG, GIF. Please upload high resolution (>1000 pixels wide).")
    )
    priority = models.PositiveSmallIntegerField(
        default=0,
        help_text=_("0=first, 1=second etc.")
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('priority',)


class Interval(models.Model):

    weekday = models.ForeignKey('Weekday', on_delete=models.CASCADE)

    every_week = models.BooleanField(default=False)
    first_week_of_month = models.BooleanField(default=False)
    second_week_of_month = models.BooleanField(default=False)
    third_week_of_month = models.BooleanField(default=False)
    last_week_of_month = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Weekday(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name=_("name"),
    )
    number = models.PositiveSmallIntegerField(default=0, unique=True)
