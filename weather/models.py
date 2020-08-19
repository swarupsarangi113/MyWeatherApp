from django.db import models
from django.utils import timezone

class City(models.Model) :
    city_name = models.CharField(max_length=25)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return f"{self.city_name} data"

    class Meta :
        verbose_name_plural = 'Cities'