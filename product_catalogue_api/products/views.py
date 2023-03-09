from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser


@api_view(['GET', 'POST'])
@parser_classes([ MultiPartParser])
@permission_classes([IsAuthenticated])
def product_list_create_view(request, pk=None, *args, **kwargs):
  method = request.method
  
  if method == 'GET':
    if pk is not None:
      product = get_object_or_404(Product, pk=pk)
      data = ProductSerializer(product).data
      return Response(data, status=status.HTTP_200_OK)
    
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data, status=status.HTTP_200_OK)
  
  if method == 'POST':
    serialized_data = ProductSerializer(data=request.data)
    
    if serialized_data.is_valid(raise_exception=True):
      serialized_data.save()
      return Response(serialized_data.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@parser_classes([ MultiPartParser])
@permission_classes([IsAuthenticated])
def product_update_delete_view(request, pk=None, *args, **kwargs):
  method = request.method
  if method == 'DELETE':
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return Response({'message': f'Product with ID {pk} is successfully deleted.'}, status=status.HTTP_200_OK)
  
  if method == 'PUT':
    product = get_object_or_404(Product, pk=pk)
    serialized_data = ProductSerializer(instance=product, data=request.data)
    
    if serialized_data.is_valid(raise_exception=True):
      serialized_data.save()
    return Response(serialized_data.data, status=status.HTTP_200_OK)