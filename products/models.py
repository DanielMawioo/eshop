from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price =models.FloatField()
    stock = models.IntegerField()
    thumbnail = models.ImageField()


    def __str__(self):
        return self.title


class Offer(models.Model):
    code = models.CharField(max_length=12)
    description = models.CharField(max_length=200)
    discount = models.FloatField()

    def __str__(self):
        return self.code