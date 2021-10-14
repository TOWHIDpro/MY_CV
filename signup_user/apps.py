from django.apps import AppConfig


class SignupUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signup_user'

    def ready(self):
        import signup_user.signals
