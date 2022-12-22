from django.urls import include, path
from rest_framework.routers import DefaultRouter
from assets.api import views as assets_views


router = DefaultRouter()
router.register(r'assets', assets_views.AssetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
