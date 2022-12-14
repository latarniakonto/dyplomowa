from rest_framework import viewsets
from portfolios.models import Portfolio
from portfolios.api.serializers import PortfolioSerializer
from rest_framework.permissions import IsAuthenticated
from portfolios.api.permissions import IsPortfolioOwner
from portfolios.api.filters import IsOwnerFilter


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsPortfolioOwner]
    filter_backends = [IsOwnerFilter]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
