from rest_framework import permissions
from portfolios.models import Portfolio


class IsAssetOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.portfolio.owner == request.user
