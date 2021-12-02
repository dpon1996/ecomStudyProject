from django.db import models
from category.models import Category
from django.utils.safestring import mark_safe
from django.urls import reverse


class BasicProductData(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Product(BasicProductData):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    image = models.ImageField(upload_to='photos/product')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.product_name
