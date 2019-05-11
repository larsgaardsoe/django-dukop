from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """The user manager class."""

    def create_user(self, password: str = None, **kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password: str, **kwargs):
        user = self.create_user(password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(update_fields=['is_staff', 'is_superuser'])
        return user


class User(PermissionsMixin, AbstractBaseUser):

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = UserManager()

    nick = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField(
        unique=True,
        verbose_name=_('E-Mail'),
        help_text=_(
            'Your email address will be used for password resets and notification about your event/submissions.'
        ),
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self) -> str:
        """Use a useful string representation."""
        return self.get_display_name()

    def get_display_name(self) -> str:
        return self.nick if self.nick else str(_('Unnamed user'))

    class Meta:
        verbose_name = _("User")


class Group(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name=_("name"),
    )
    members = models.ManyToManyField(User, related_name='dukop_groups')

    is_restricted = models.BooleanField(
        default=False,
        help_text=_("Do not allow others to add events to this group"),
    )

    owner_email = models.EmailField(blank=True, null=True)

    link1 = models.URLField(blank=True, null=True)
    link2 = models.URLField(blank=True, null=True)
    link3 = models.URLField(blank=True, null=True)

    street = models.CharField(
        max_length=255,
        verbose_name=_("street"),
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=255,
        verbose_name=_("city"),
        blank=True,
        null=True,
    )
    zip_code = models.CharField(
        verbose_name=_("zip code"),
        blank=True,
        null=True,
        max_length=16,
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Group")
