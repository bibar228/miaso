from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', "id"]

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', "id", 'price', "unit", 'available', "img", "category"]
    list_filter = ['available']
    list_editable = ['price', 'available']


admin.site.register(Product, ProductAdmin)