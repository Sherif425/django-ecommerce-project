from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer, CategorySerializer                           

class ProductListCreateView(generics.ListCreateAPIView):
    """
    GET: List all products
    POST: Create a new product (authenticated users only)
    """
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically associate the product with the logged-in user
        serializer.save(owner=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve product by ID
    PUT/PATCH: Update product (owner or admin)
    DELETE: Delete product (owner or admin)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
