from django.contrib import admin
from django.utils.html import format_html

from . import models


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    fields = ('admin_photo', 'category_name', 'slug', 'cat_image')
    list_display = ('category_name', 'slug', 'admin_photo',)
    readonly_fields = ('admin_photo',)


admin.site.register(models.Category, CategoryAdmin)
