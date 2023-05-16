from django.db import models

from main.models import Copch, Cold, Poly


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    comment = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Данные заказчика'

    def __str__(self):
        return f'Заказ №{self.id} от {self.first_name} - {self.email}. Общая стоимость: {self.get_total_cost()} руб.'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    copch_product = models.ForeignKey(Copch, related_name='order_items', on_delete=models.SET_NULL, null=True, blank=True)
    cold_product = models.ForeignKey(Cold, related_name='order_items', on_delete=models.SET_NULL, null=True, blank=True)
    poly_product = models.ForeignKey(Poly, related_name='order_items', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity