from django.contrib import admin
from . import models


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available', 'admin_photo')
    fields = ('admin_photo', 'product_name', 'slug', 'price', 'stock', 'category', 'is_available', 'image'),
    readonly_fields = ('admin_photo',)

    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(models.Product, ProductAdmin)
