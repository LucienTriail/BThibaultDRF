from . import views
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#    path('auth/', include('rest_framework.urls')),

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>', views.SingleProduct.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('rest_framework.urls')),



]
