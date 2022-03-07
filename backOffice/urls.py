from . import views
from django.urls import path


urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>', views.SingleProduct.as_view())
]