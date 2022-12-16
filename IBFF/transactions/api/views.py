from rest_framework import viewsets
from transactions.models import Transaction
from portfolios.models import Portfolio
from transactions.api.serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from transactions.api.permissions import IsContainedInOwnedPortfolios
from transactions.api.filters import OwnedPortfoliosFilter
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsContainedInOwnedPortfolios]
    filter_backends = [OwnedPortfoliosFilter]

    def perform_create(self, serializer):
        portfolio = get_object_or_404(Portfolio, slug=self.request.data['slug'])
        serializer.save(portfolio=portfolio)

    def list(self, request, slug=None):
        if slug is None:
            return super().list(request)
        else:
            user_portfolio = get_object_or_404(Portfolio, owner=request.user, slug=slug)
            queryset = user_portfolio.transactions

        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)
