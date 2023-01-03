from django.urls import include, path
from rest_framework.routers import DefaultRouter
from snapshots.api import views as snapshots_views


router = DefaultRouter()
router.register(r'snapshots', snapshots_views.SnapshotViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]
