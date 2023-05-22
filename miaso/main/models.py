from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название продукта", max_length=100)
    description = models.TextField(blank=True)
    unit = models.CharField(verbose_name="Ед. измерения", max_length=20)
    price = models.DecimalField(verbose_name="Цена", max_digits=7, decimal_places=2, null=True)
    img = models.FileField(upload_to='privet/', default="", blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return self.name


