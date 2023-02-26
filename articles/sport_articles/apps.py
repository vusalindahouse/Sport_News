from django.apps import AppConfig


class SportArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sport_articles'
    verbose_name = "Спортивные статьи"

    def ready(self):
        from .jobs import updater
        updater.start()