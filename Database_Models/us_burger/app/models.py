from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.IntegerField()
    measurement = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    ingredients = models.ManyToManyField(Ingredient)
    def __str__(self):
        return self.name