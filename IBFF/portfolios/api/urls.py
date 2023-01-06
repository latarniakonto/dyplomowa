from django.urls import include, path
from django.contrib.auth.decorators import permission_required
from rest_framework.routers import DefaultRouter
from portfolios.api import views as portfolios_views
from transactions.api import views as transactions_views
from assets.api import views as assets_views
from operations.api import views as operations_views
from snapshots.api import views as snapshots_views


router = DefaultRouter()
router.register(r'portfolios', portfolios_views.PortfolioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'portfolios/<slug:p_slug>/transactions/',
        transactions_views.TransactionViewSet.as_view({'get': 'list'}),
        name='transactions-list',
    ),
    path(
        'portfolios/<slug:p_slug>/assets/',
        assets_views.AssetViewSet.as_view({'get': 'list'}),
        name='assets-list',
    ),
    path(
        'portfolios/<slug:p_slug>/dividends/',
        operations_views.DividendViewSet.as_view({'get': 'list'}),
        name='dividends-list',
    ),
    path(
        'portfolios/<slug:p_slug>/snapshots/',
        snapshots_views.SnapshotViewSet.as_view({'get': 'list'}),
        name='snaphot-list',
    ),
    path(
        'portfolios/<slug:p_slug>/snapshots/get_or_create/',
        snapshots_views.SnapshotUOCViewSet.as_view({'get': 'list'}),
        name='generate-snaphot-list',
    ),
]
