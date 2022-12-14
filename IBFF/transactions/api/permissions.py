from rest_framework import permissions
from portfolios.models import Portfolio


class IsContainedInOwnedPortfolios(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user_portfolios = Portfolio.objects.filter(owner=request.user)

        for user_portfolio in user_portfolios:
            if user_portfolio.id == obj.portfolio.id:
                return True
        
        return False
