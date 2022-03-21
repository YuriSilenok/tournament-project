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
    surname = models.CharField('Surname', max_length = 50)
    name = models.CharField('Name', max_length = 50)
    patronymic = models.CharField('Patronymic', max_length = 50)
    year_of_birth = models.DateField('Year')
    gender = models.BinaryField("Gender")
    
    class Meta:
    
        verbose_surname = "Фамилия"
        verbose_name_plural_surname = "Фамилии"
        verbose_name = "Имя"
        verbose_name_plural = "Имена"
        verbose_patronymic = "Отчество"
        verbose_year_of_birth = "Год рождения"
        verbose_gender = "Пол"
    
    def __str__(self, a):
       
        if a == "surname":
            return self.surname

        elif a == "name":
            return self.name

        elif a == "patronymic":
            return self.patronymic

        elif a == "year_of_birth":
            return self.year_of_birth

        elif a == "gender":
            return self.gender
        else:
            pass

