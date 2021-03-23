from django.urls import path,include
from . import views
urlpatterns = [
    path('products',views.ProductList.as_view()),
    path('category',views.CategoryList.as_view()),
    path('products/add',views.ProductCreate.as_view()),
    path('category/add',views.CategoryCreate.as_view()),
    path('products/<int:pk>',views.ProductRetrieveUpdateDestroy.as_view()),
    path('auth',include('rest_framework.urls')),

]
