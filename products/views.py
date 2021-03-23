from rest_framework import generics, permissions
from .serializers import ProductSerializer, CategorySerializer
from products.models import Category, Product

# List of the product
class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.pk
        return Product.objects.filter(product_owner=user)

# For Retrieve only product ,update or delete.
class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.pk
        return Product.objects.filter(product_owner=user)

# Adding the products
class ProductCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.pk
        return Product.objects.filter(product_owner=user)

    def perform_create(self,serializer):
        serializer.save(product_owner=self.request.user.pk)


# List of the category
class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()

# Add the new category
class CategoryCreate(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()

    def perform_create(self,serializer):
        serializer.save()

# For retrieve only category ,update, delete
class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()
