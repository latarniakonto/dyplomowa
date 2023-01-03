from rest_framework import viewsets
from snapshots.models import Snapshot
from snapshots.api.serializers import SnapshotSerializer
from rest_framework.permissions import IsAuthenticated
from snapshots.api.permissions import IsPortfolioOwner
from snapshots.api.filters import IsOwnerFilter


class SnapshotViewSet(viewsets.ModelViewSet):
    queryset = Snapshot.objects.all()
    serializer_class = SnapshotSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsPortfolioOwner]
    filter_backends = [IsOwnerFilter]

    def perform_create(self, serializer):
        serializer.save()
