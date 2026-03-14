from django.shortcuts import render
from .models import Product
from django.db.models import Q

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()
    
    return render(request, 'marketplace/product_list.html', {'products': products})