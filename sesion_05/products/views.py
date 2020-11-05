"""Products app views"""

# Stardard library

# Django imports
# from django.shortcuts import get_object_or_404

# Third party apps
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status, generics
from rest_framework import viewsets

# Local apps
from .models import Product
from .serializers import ProductSerializer


# Viewsets

class ProductViewset(viewsets.ModelViewSet):
    """Product CRUD views"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Generic View

# class ProductList(generics.ListCreateAPIView):
#     """Gets and creates products"""
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductRetrieve(generics.RetrieveUpdateDestroyAPIView):
#     """Retrieves, updates and deletes a single product"""
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# API Views

# class ProductsView(APIView):
#     """Shows and creates products"""

#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductView(APIView):
#     """Show, updates and deletes products"""

#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         product.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
