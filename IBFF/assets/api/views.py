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

    def list(self, request, slug=None):
        if slug is None:
            return super().list(request)
        else:
            user_portfolio = get_object_or_404(Portfolio, owner=request.user, slug=slug)
            queryset = user_portfolio.assets

        serializer = AssetSerializer(queryset, many=True)
        return Response(serializer.data)
