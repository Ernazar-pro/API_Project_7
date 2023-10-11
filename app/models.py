from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        ordering = ['-id']


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'


class Create(models.Model):
    title = models.CharField(blank=True, null=True, max_length=256)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    