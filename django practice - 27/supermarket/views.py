from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .models import Product


@api_view(['POST'])
def create_product(request):
    name = request.data.get('name')
    price = request.data.get('price')

    if not name or not price:
        return Response({'error': 'name and price are required'}, status=status.HTTP_400_BAD_REQUEST)

    product = Product.objects.create(name=name, price=price)

    return Response({
        "message": "new product added successfully",
        "product": {
            "name": product.name,
            "price": product.price
        }
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    return Response({
        'name': product.name,
        'price': product.price
    }, status=status.HTTP_200_OK)
