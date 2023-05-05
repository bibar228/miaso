from django.contrib import admin

from .models import Copch, Poly, Cold


# Register your models here.
class CopchAdmin(admin.ModelAdmin):
    list_display = ("id", "name_prod", "unit", "price")
    #list_display_links = ("id", "name")
    #search_fields = ("id", "name", "description")

class PolyAdmin(admin.ModelAdmin):
    list_display = ("id", "name_prod", "unit", "price")
    #list_display_links = ("id", "name")
    #search_fields = ("id", "name", "description")


class ColdAdmin(admin.ModelAdmin):
    list_display = ("id", "name_prod", "unit", "price")
    #list_display_links = ("id", "name")
    #search_fields = ("id", "name", "description")


admin.site.register(Copch, CopchAdmin)
admin.site.register(Poly, PolyAdmin)
admin.site.register(Cold, ColdAdmin)