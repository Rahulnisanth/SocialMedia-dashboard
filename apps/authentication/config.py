from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = "apps.authentication"
    label = "apps_authentication"

    # NEEDED FOR SIGNALS MODULE :
    def ready(self):
        from . import signals
