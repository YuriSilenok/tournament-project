import imp
from django.db import models

class Tournament(models.Model):
    name = models.CharField('Tournament name', max_length = 75)
    start_date = models.DateTimeField('Date fo start')
    status = models.BooleanField('Status')

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
