from rest_framework import viewsets
from assets.models import Asset
from assets.api.serializers import AssetSerializer
from rest_framework.permissions import IsAuthenticated
from assets.api.permissions import IsAssetOwner
from assets.api.filters import IsOwnerFilter


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsAssetOwner]
    filter_backends = [IsOwnerFilter]

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request):
        return super().list(request)
