from rest_framework import serializers

from api import models


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cap
        exclude = ['initial_stock']


class CapListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cap
        exclude = ['initial_stock']


class TShirtListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TShirt
        exclude = ['initial_stock']
