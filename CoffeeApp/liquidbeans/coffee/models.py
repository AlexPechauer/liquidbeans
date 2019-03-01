from django.db import models

class Orders(models.Model):
    drink = models.CharField(max_length=50)
    picture = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    flavor1 = models.CharField(max_length=10)
    flavor2 = models.CharField(max_length=10)
    flavor3 = models.CharField(max_length=10)
    flavor4 = models.CharField(max_length=10)

    def __str__(self):
        return self.drink
