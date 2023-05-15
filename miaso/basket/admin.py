from django.contrib import admin

from basket.models import Order, OrderItem

# Register your models here.
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "copch_product", "cold_product", "poly_product", "price")
    #list_display_links = ("id", "name")
    #search_fields = ("id", "name", "description")

admin.site.register(Order)
admin.site.register(OrderItem, OrderItemAdmin)