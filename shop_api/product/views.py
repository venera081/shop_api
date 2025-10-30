from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategoryListSerializer, ProductsListSerializer, ReviewsListSerializer
from .serializers import CategoryDelailSerializer, ProductDetailSerializer, ReviewDetailSerializer, ProductWithReviewsSerializer


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'Category not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = CategoryDelailSerializer(category).data
    return Response(data=data)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product).data
    return Response(data=data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    data = CategoryListSerializer(instance=categories, many=True).data

    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def products_list_api_view(request):
    products = Product.objects.all()
    data = ProductsListSerializer(instance=products, many=True).data

    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewsListSerializer(instance=reviews, many=True).data

    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def products_with_reviews_api_view(request):
    products = Product.objects.all()
    data = ProductWithReviewsSerializer(products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)