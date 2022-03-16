from django.db import models
from django.utils import timezone

class Tournament(models.Model):
    name = models.CharField('Tournament name', max_length = 75)
    start_date = models.DateTimeField('Date of start', default=timezone.now())
    completeness = models.BooleanField('Completeness of tournament', default=False)

    class Meta:
        verbose_name = "Турнир"
        verbose_name_plural = "Турниры"
        
    def __str__(self):
        return self.name