from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories')

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.cat_image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.category_name
