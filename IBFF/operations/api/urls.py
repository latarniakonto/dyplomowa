from django.urls import include, path
from rest_framework.routers import DefaultRouter
from operations.api import views as operations_views


router = DefaultRouter()
router.register(r'dividends', operations_views.DividendViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]
