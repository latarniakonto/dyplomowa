from django.urls import include, path
from rest_framework.routers import DefaultRouter
from assets.api import views as assets_views
from transactions.api import views as transactions_views


router = DefaultRouter()
router.register(r'assets', assets_views.AssetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'assets/<slug:a_slug>/transactions/',
        transactions_views.TransactionViewSet.as_view({'get': 'list'}),
        name='transactions-list',
    ),
]
