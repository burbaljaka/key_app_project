from django.db import models
from rest_framework_api_key.models import AbstractAPIKey


# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class ApplicationKey(AbstractAPIKey):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='api_keys')
