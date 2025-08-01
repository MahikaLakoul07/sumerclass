from django.utils import timezone
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price =models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    stock = models.IntegerField(default=1)
    status = models.BooleanField(default=0)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)   
    product_image = models.ImageField(upload_to='photos/products', blank=True) 

    def __str__(self):
        return self.name
    