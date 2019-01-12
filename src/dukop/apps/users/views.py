from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy


class PasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('users:password_reset_complete')


class PasswordChangeView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('users:password_change_done')
