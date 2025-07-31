from django.apps import AppConfig


class DrawingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drawings'
    verbose_name = "Site Manager"

    def ready(self):
        import drawings.signals
