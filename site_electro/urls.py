from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:id>/', views.category_detail, name='category_detail'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'), # << ВАША ФУНКЦІЯ product_detail
    path('photos/', views.photos, name='photos'),
    path('reviews/', views.reviews_page, name='reviews_page'),
]