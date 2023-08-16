from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_initial_status(sender, **kwargs):
    from .models import StatusModel
    if not StatusModel.objects.exists():
        StatusModel.objects.create(status="new", code="#1cdb37")

class CommonappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'commonapp'

    def ready(self):
        post_migrate.connect(create_initial_status, sender=self)