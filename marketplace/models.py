from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200) # اسم المنتج (كتاب، لاب توب، إلخ)
    description = models.TextField()         # وصف بسيط
    price = models.DecimalField(max_digits=10, decimal_places=2) # السعر
    created_at = models.DateTimeField(auto_now_add=True) # تاريخ الإضافة تلقائياً

    def __str__(self):
        return self.name
