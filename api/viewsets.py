from rest_framework import viewsets, permissions

from api import serializers, models


class CapViewSet(viewsets.ModelViewSet):
    queryset = models.Cap.objects.all()
    serializer_class = serializers.CapListSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class TShirtViewSet(viewsets.ModelViewSet):
    queryset = models.TShirt.objects.all()
    serializer_class = serializers.TShirtListSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
