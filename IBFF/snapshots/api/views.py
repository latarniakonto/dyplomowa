from rest_framework import viewsets
from snapshots.models import Snapshot, get_or_create_snapshot
from snapshots.api.serializers import SnapshotSerializer
from rest_framework.permissions import IsAuthenticated
from snapshots.api.permissions import IsPortfolioOwner
from snapshots.api.filters import IsOwnerFilter
from django.shortcuts import get_object_or_404
from portfolios.models import Portfolio
from rest_framework.response import Response


class SnapshotViewSet(viewsets.ModelViewSet):
    queryset = Snapshot.objects.all()
    serializer_class = SnapshotSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsPortfolioOwner]
    filter_backends = [IsOwnerFilter]

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, p_slug=None):
        if p_slug is None:
            return super().list(request)

        portfolio = get_object_or_404(Portfolio, slug=p_slug, owner=request.user)
        queryset = portfolio.snapshots
        serializer = SnapshotSerializer(queryset, many=True)
        return Response(serializer.data)


class SnapshotUOCViewSet(viewsets.ModelViewSet):
    queryset = Snapshot.objects.all()
    serializer_class = SnapshotSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsPortfolioOwner]
    filter_backends = [IsOwnerFilter]

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, p_slug):
        portfolio = get_object_or_404(Portfolio, slug=p_slug, owner=request.user)
        snapshot = get_or_create_snapshot(portfolio)        
        serializer = SnapshotSerializer(snapshot)
        return Response(serializer.data)
