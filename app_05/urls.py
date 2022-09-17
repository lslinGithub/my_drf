from django.urls import path, include
from . import views
from rest_framework.authtoken import views as token_views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('cars/', views.CarsView.as_view(), name='cars-list'),
    # path('api-token-auth/', token_views.obtain_auth_token),
    path('api-token-auth/', obtain_jwt_token),
]
