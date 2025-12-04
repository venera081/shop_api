from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Category, Product, Review
from common.validators import validate_age

class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(source='product_set.count', read_only=True)

    class Meta:
        model = Category
        fields = 'id name products_count'.split()

        def validate(self, attrs):
            user = self.context['request'].user
            validate_age(user)
            return attrs



class ProductsListSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id reviews title description price'.split()

    def get_reviews(self, product):
        return [r.text for r in product.reviews.all()]
    
    def validate(self, attrs):
        user = self.context['request'].user
        validate_age(user)
        return attrs


class ReviewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class ProductWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewsListSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id title description price reviews rating'.split()

    def get_rating(self, obj):
        return obj.average_rating()


class CategoryDelailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=2, max_length=150)


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=2, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True, default='No description')
    price = serializers.IntegerField(min_value=1)
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        if not Category.objects.filter(id=category_id).exists():
            raise ValidationError('Category does not exist!')
        return category_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, min_length=2, max_length=300)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        if not Product.objects.filter(id=product_id).exists():
            raise ValidationError('Product does not exist!')
        return product_id
