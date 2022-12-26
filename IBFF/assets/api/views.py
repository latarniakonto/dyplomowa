from rest_framework import viewsets
from assets.models import Asset
from assets.api.serializers import AssetSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from portfolios.models import Portfolio
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

    def list(self, request, p_slug=None):
        if p_slug is None:
            return super().list(request)
        else:
            portfolio = get_object_or_404(Portfolio, slug=p_slug, owner=request.user)
            queryset = portfolio.assets.filter(total__gt=0)

        serializer = AssetSerializer(queryset, many=True)
        return Response(serializer.data)
