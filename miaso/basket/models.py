from django.core.validators import RegexValidator
from django.db import models

from main.models import Product
from users.models import User


class Order(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Номер заказа", unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    address = models.CharField(max_length=250)
    phoneNumberRegex = RegexValidator(regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=11, blank=False)
    comment = models.CharField(max_length=500, blank=True, verbose_name="Комментарий к заказу")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создание заказа")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновление заказа")
    paid = models.BooleanField(default=False, verbose_name="Статус оплаты")

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Данные заказчика'

    def __str__(self):
        return f'Заказ №{self.id} от {self.user}. Общая стоимость: {self.get_total_cost()} руб.'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    class Meta:
        ordering = ('order',)
        verbose_name_plural = 'Заказ'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
