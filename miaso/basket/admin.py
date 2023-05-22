from django.contrib import admin

from basket.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "id", "comment", "paid", 'created', 'updated')
    #list_display_links = ("id", "name")
    #search_fields = ("id", "name", "description")
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)