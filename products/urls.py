from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index, name='index'),
    path('', views.products, name="products"),
    #path('details', views.productDetails, name='productdetails'),
    path('<int:id>/', views.product_detail, name='product_detail'),
]
