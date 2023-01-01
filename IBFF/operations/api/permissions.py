from rest_framework import permissions


class IsPortfolioOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.asset.portfolio.owner == request.user
