from django.shortcuts import render

# Create your views here.
from .models import Product # استدعاء جدول المنتجات

def product_list(request):
    # جلب كل المنتجات من قاعدة البيانات
    products = Product.objects.all() 
    #إرسال المنتجات لصفحة HTML 
    return render(request, 'marketplace/product_list.html', {'products': products})