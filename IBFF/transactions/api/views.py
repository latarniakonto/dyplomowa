from rest_framework import viewsets
from transactions.models import Transaction
from portfolios.models import Portfolio
from transactions.api.serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from transactions.api.permissions import IsContainedInOwnedPortfolios
from transactions.api.filters import OwnedPortfoliosFilter
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from assets.models import Asset


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsContainedInOwnedPortfolios]
    filter_backends = [OwnedPortfoliosFilter]

    def perform_create(self, serializer):
        portfolio = get_object_or_404(
            Portfolio, slug=self.request.data['portfolio_slug']
        )
        serializer.save(portfolio=portfolio)

    def list(self, request, p_slug=None, a_slug=None):
        if p_slug is None and a_slug is None:
            return super().list(request)

        elif p_slug:
            portfolio = get_object_or_404(Portfolio, slug=p_slug, owner=request.user)
            queryset = portfolio.transactions

        elif a_slug:
            asset = get_object_or_404(Asset, slug=a_slug, portfolio__owner=request.user)
            queryset = asset.portfolio.transactions.filter(ticker=asset.ticker)

        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)
