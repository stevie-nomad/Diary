from django.db import models
from django.utils import timezones


class Entry(models.Model):
    title = models.Charfield(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"    



