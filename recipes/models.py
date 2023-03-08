from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField("Título", max_length=100)
    ingredients = models.TextField("Ingredientes")
    preparation_method = models.TextField("Modo de preparo")
    chef = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
