from rest_framework import viewsets
from transactions.models import Transaction
from transactions.api.serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from transactions.api.permissions import IsContainedInOwnedPortfolios
from transactions.api.filters import OwnedPortfoliosFilter


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsContainedInOwnedPortfolios]
    filter_backends = [OwnedPortfoliosFilter]

    def perform_create(self, serializer):
        serializer.save()
