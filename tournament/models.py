from django.db import models


class Tournament(models.Model):
    name = models.CharField('Tournament name', max_length=75)
    start_date = models.DateField('Date of start', auto_now=True)
    completeness = models.BooleanField('Completeness of tournament', default=False)

    class Meta:
        verbose_name = "Турнир"
        verbose_name_plural = "Турниры"
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.TextField('Category')
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.name


class Nomination(models.Model):
    name = models.CharField('Nomination', max_length=100)
    
    class Meta:
        verbose_name = "Номинация"
        verbose_name_plural = "Номинации"
    def __str__(self):
        return self.name