from django.contrib.auth import views as auth_views


class PasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
