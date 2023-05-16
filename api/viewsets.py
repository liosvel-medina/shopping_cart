from rest_framework import viewsets, permissions, response, status

from api import serializers, models

import datetime


class CapViewSet(viewsets.ModelViewSet):
    queryset = models.Cap.objects.all().filter(is_deleted=False)
    serializer_class = serializers.CapListSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.deleted_date = datetime.date.today()
        instance.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class TShirtViewSet(viewsets.ModelViewSet):
    queryset = models.TShirt.objects.all().filter(is_deleted=False)
    serializer_class = serializers.TShirtListSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.deleted_date = datetime.date.today()
        instance.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Product.objects.all().filter(is_deleted=False)
    serializer_class = serializers.ProductListSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
