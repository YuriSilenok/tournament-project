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

    class Surname:
        surname = models.CharField('Surname', max_length = 50)

        class Meta:
            verbose_name = "Фамилия"
            verbose_name_plural = "Фамилии"

        def __str__(self):
            return self.surname
    
    class Name:
        name = models.CharField('Name', max_length = 50)

        class Meta:
            verbose_name = "Имя"
            verbose_name_plural = "Имена"

        def __str__(self):
            return self.name

    class Patronymic:
        patronymic = models.CharField('Patronymic', max_length = 50)

        class Meta:
            verbose_name = "Отчество"

        def __str__(self):
            return self.patronymic

    class Year:
        year = models.IntegerField('Year')

        class Meta:
            verbose_name = "Год"

        def __str__(self):
            return self.year

    class Gender:
        gender = models.BinaryField("Gender")

        class Meta:
            verbose_name = "Пол"

        def __str__(self):
            return self.gender

