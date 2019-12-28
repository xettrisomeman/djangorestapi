from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass



class Theory(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now=False, auto_now_add=False)
    created_with = models.ManyToManyField('Scientist',blank=True)
    based_on = models.CharField(max_length=50)
    details = models.TextField()
    related_url = models.URLField(max_length=300)

    def __str__(self):
        return self.name 

class Scientist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    theories = models.ManyToManyField(Theory)
    birth_place = models.CharField(max_length=50)
    death = models.DateField(blank=True, auto_now=False, auto_now_add=False)
    is_dead = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    

    