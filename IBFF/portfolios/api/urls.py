from django.urls import include, path
from django.contrib.auth.decorators import permission_required
from rest_framework.routers import DefaultRouter
from portfolios.api import views as portfolios_views
from transactions.api import views as transactions_views


router = DefaultRouter()
router.register(r'portfolios', portfolios_views.PortfolioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'portfolios/<slug:slug>/transactions/',
        transactions_views.TransactionViewSet.as_view({'get': 'list'}),
        name='transactions-list',
    ),
]
