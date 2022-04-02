from unicodedata import category
from django.db import models


class Tournament(models.Model):
    name = models.CharField('Name', max_length=75)
    start_date = models.DateField('StarDate', auto_now=True)
    completeness = models.BooleanField('Completed', default=False)

    class Meta:
        verbose_name = "Турнир"
        verbose_name_plural = "Турниры"
        
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Category', max_length=200)
    
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


class Human(models.Model):
    name = models.TextField('Name')
    surname = models.TextField('Surname')
    patronymic = models.TextField('Patronymic')
    year = models.IntegerField('Year')
    gender = models.BinaryField("Gender")

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Чебуреки"

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.TextField('Name')
    city = models.TextField('City')
    
    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"

    def __str__(self):
        return self.name

class Participant_category(models.Model):
    category = models.ForeignKey(
        Category)
    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Участник-Категория"
        verbose_name_plural = "Участники-Категории"
    
    def __str__(self):
        return self.category