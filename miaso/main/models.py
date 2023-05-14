from django.db import models

# Create your models here.
class Copch(models.Model):
    name_prod = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    copch_file = models.FileField(upload_to='privet/', default=None)

    def __str__(self):
        return self.name_prod

class Poly(models.Model):
    name_prod = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    def __str__(self):
        return self.name_prod

class Cold(models.Model):
    name_prod = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    def __str__(self):
        return self.name_prod