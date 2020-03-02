from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Employee(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
 
    def __str__(self):
        return self.name


class HR(models.Model):

    class Rate(models.IntegerChoices):
        AAA = 1
        AA = 2
        A = 3
        BBB = 4
        BB = 5
        B = 6 

    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    # https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    rating = models.IntegerField(
        choices=Rate.choices, 
        validators=[MaxValueValidator(6), MinValueValidator(1)]
        )

    class Meta:
        verbose_name = "HR"
        verbose_name_plural = "HR"
 
    def __str__(self):
        return self.name

class Employer(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Employer"
        verbose_name_plural = "Employers"
 
    def __str__(self):
        return self.name