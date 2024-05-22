from django.urls import path
from . import views


app_name = 'social'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('user/', views.redirect_to_index),
    path('user/<str:username>/', views.UserView.as_view(), name='user'),
]