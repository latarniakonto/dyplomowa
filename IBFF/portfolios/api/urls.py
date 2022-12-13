from django.urls import include, path
from rest_framework.routers import DefaultRouter
from portfolios.api import views


router = DefaultRouter()
router.register(r"portfolios", views.PortfolioViewSet)

urlpatterns = [
    path("", include(router.urls))
]
