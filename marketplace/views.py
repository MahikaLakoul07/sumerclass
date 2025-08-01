from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category, Product
from blogs.models import BlogCategory, Blogs

def home(request):
    products = Product.objects.all()
    blogs = Blogs.objects.all()

    return render(request, 'home/home1.html', 
    {
        'products': products,
        'blogs' : blogs
    })

