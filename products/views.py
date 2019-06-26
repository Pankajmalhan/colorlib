from django.shortcuts import render
from .submodels.products import Products
from .submodels.dealofWeeks import DealsOfWeek
# Create your views here.


def home(request):
    products=Products.objects.all()
    dealsOfWeek=DealsOfWeek.objects.all()
    return render(request, 'home/home.html',{"products":products,"dealsOfWeek":dealsOfWeek})
