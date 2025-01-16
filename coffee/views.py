from django.shortcuts import render
from .models import CoffeeProduct

def home(request):
    # Get all coffee products from the database
    products = CoffeeProduct.objects.all()

    # Pass the products to the template context
    return render(request, 'coffee/home.html', {'products': products})
