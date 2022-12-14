from rest_framework.filters import BaseFilterBackend
from portfolios.models import Portfolio
from django.db.models import Q


class OwnedPortfoliosFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_portfolios = Portfolio.objects.filter(owner=request.user)
        query = Q()
        for user_portfolio in user_portfolios:
            query |= Q(portfolio=user_portfolio.id)

        return queryset.filter(query)
