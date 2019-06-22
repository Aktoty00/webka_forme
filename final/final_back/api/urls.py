from django.urls import path
from api import views

urlpatterns = [
    path('products', views.ProductList.as_view()),
    path('user_products', views.User_products.as_view()),
    path('user_products/<int:pk>/', views.User_productsNUM.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
]