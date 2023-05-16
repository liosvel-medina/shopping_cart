from rest_framework import serializers

from api import models


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        exclude = ['initial_stock']


class CapListSerializer(serializers.ModelSerializer):
    main_color = ColorSerializer(many=False, read_only=True)
    secondary_colors = ColorSerializer(many=True, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)
    logo_color = ColorSerializer(many=False, read_only=True)

    class Meta:
        model = models.Cap
        exclude = ['initial_stock']


class TShirtListSerializer(serializers.ModelSerializer):
    main_color = ColorSerializer(many=False, read_only=True)
    secondary_colors = ColorSerializer(many=True, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = models.TShirt
        exclude = ['initial_stock']
