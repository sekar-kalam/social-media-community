from django.apps import AppConfig


class CommunityappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'communityApp'

    def ready(self):
        import communityApp.signals 
