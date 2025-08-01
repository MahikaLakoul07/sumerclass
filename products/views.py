from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from products.models import Product


def products(request):
    #return HttpResponse("This is Products Page")
    all_products = Product.objects.all()
    return render(request, 'extending/products.html', {'products': all_products})

#def productDetails(request):
    #return HttpResponse("This is product details.")

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'extending/product_details.html', {'product': product})
    