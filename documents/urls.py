from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, UserLoginViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='documents')
router.register(r'users', UserLoginViewSet, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
]
