from api.serializers import ProductSerializer, UserProductSerializer2
from rest_framework import generics, filters
from api.models import Product, UserProduct
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter)

    #SearchFilter
    search_fields = ('name', 'price')

class User_products(generics.ListCreateAPIView):
    serializer_class = UserProductSerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserProduct.objects.for_user_order_by_name(self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class User_productsNUM(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProduct.objects.all()
    serializer_class = UserProductSerializer2

