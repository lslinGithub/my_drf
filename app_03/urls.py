from django.urls import path
from . import views
urlpatterns = [
    path('userinfo_list/', views.userinfo_list, name='user-list'),
    path('userinfo_detail/<int:pk>/', views.userinfo_detail, name='userinfo-detail'),
    path('users_detail/<int:pk>/', views.UserDetail.as_view(), name='users-detail'),
    path('users_list/', views.UserList.as_view(), name='users-list'),
]