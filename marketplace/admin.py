from django.contrib import admin

# Register your models here.
from .models import Product #استدعاء model

admin.site.register(Product)