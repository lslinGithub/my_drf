from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.registry(r'games', views.GameViewSet)
urlpatterns = [
    path('', include(router.urls), name='GameViewSet'),
]