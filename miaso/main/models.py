from django.db import models

# Create your models here.
class Copch(models.Model):
    name_prod = models.CharField(verbose_name="Название продукта", max_length=100)
    unit = models.CharField(verbose_name="Ед. измерения", max_length=20)
    price = models.DecimalField(verbose_name="Цена", max_digits=7, decimal_places=2, null=True)
    img = models.FileField(upload_to='privet/', default="", blank=True)

    def __str__(self):
        return self.name_prod




class Poly(models.Model):
    name_prod = models.CharField(verbose_name="Название продукта", max_length=100)
    unit = models.CharField(verbose_name="Ед. измерения", max_length=20)
    price = models.DecimalField(verbose_name="Цена", max_digits=7, decimal_places=2, null=True)
    img = models.FileField(upload_to='privet/', default="", blank=True)

    def __str__(self):
        return self.name_prod

class Cold(models.Model):
    name_prod = models.CharField(verbose_name="Название продукта", max_length=100)
    unit = models.CharField(verbose_name="Ед. измерения", max_length=20)
    price = models.DecimalField(verbose_name="Цена", max_digits=7, decimal_places=2, null=True)
    img = models.FileField(upload_to='privet/', default="", blank=True)

    def __str__(self):
        return self.name_prod