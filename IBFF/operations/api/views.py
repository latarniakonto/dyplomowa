from rest_framework import viewsets
from operations.models import Dividend
from assets.models import Asset
from portfolios.models import Portfolio
from operations.api.serializers import DividendSerializer
from rest_framework.permissions import IsAuthenticated
from operations.api.permissions import IsPortfolioOwner
from operations.api.filters import OwnedPortfolioFilter
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q


class DividendViewSet(viewsets.ModelViewSet):
    queryset = Dividend.objects.all()
    serializer_class = DividendSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsPortfolioOwner]
    filter_backends = [OwnedPortfolioFilter]

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, a_slug=None, p_slug=None):
        if a_slug is None and p_slug is None:
            return super().list(request)

        elif p_slug:
            portfolio = get_object_or_404(Portfolio, slug=p_slug, owner=request.user)
            queryset = Dividend.objects.none()
            assets = portfolio.assets.all()
            for asset in assets:
                queryset |= asset.dividends.all()
            
        elif a_slug:
            asset = get_object_or_404(Asset, slug=a_slug, portfolio__owner=request.user)
            queryset = asset.dividends

        serializer = DividendSerializer(queryset, many=True)
        return Response(serializer.data)
