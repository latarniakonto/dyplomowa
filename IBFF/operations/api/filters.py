from rest_framework.filters import BaseFilterBackend


class OwnedPortfolioFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(asset__portfolio__owner=request.user)
