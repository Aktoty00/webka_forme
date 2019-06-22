from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Product, UserProduct
from api.serializers import ProductSerializer, UserProductSerializer2

class User_products(APIView):
    def get(self, request):
        user_products = UserProduct.objects.all()
        serializer = UserProductSerializer2(user_products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserProductSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("asdasdasdasd")
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class User_productsNUM(APIView):
    def get_object(self, pk):
        try:
            return UserProduct.objects.get(id=pk)
        except UserProduct.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user_products = self.get_object(pk)
        serializer = UserProductSerializer2(user_products)
        return Response(serializer.data)

    def delete(self, request, pk):
        user_products = self.get_object(pk)
        user_products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
