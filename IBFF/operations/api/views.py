from rest_framework import viewsets
from operations.models import Dividend
from operations.api.serializers import DividendSerializer
from rest_framework.permissions import IsAuthenticated
from operations.api.permissions import IsPortfolioOwner
from operations.api.filters import OwnedPortfolioFilter
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class DividendViewSet(viewsets.ModelViewSet):
    queryset = Dividend.objects.all()
    serializer_class = DividendSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsPortfolioOwner]
    filter_backends = [OwnedPortfolioFilter]

    def perform_create(self, serializer):
        serializer.save()
