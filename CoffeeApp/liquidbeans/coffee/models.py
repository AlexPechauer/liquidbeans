from django.db import models
from PIL import Image


class Orders(models.Model):
    drink = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='coffee_pics')
    description = models.CharField(max_length=140)
    flavor1 = models.CharField(max_length=20)
    flavor2 = models.CharField(max_length=20)
    flavor3 = models.CharField(max_length=20)
    flavor4 = models.CharField(max_length=20)

    def __str__(self):
        return self.drink

    def __save__(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class DrinkChoice(models.Model):
    choice = models.CharField(max_length=50)
    select_date = models.DateTimeField()
    name = models.CharField(max_length=20)
    keyword = models.CharField(max_length=20)
    flavor_choice = models.CharField(max_length=10)
    customize = models.CharField(max_length=140)

    def __str__(self):
        return "On {} at {} order a {}".format(str(self.select_date)[5:16], self.name, self.choice)

class Keyword(models.Model):
    keyword = models.CharField(max_length=10)

    def __str__(self):
        return self.keyword
