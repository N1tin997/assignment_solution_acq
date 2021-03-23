from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Product(models.Model):

    name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    product_owner = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    # To keep the recenty data first
    class Meta:
        ordering = ['-expiry_date']
