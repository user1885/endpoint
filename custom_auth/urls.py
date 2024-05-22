from django.urls import path
from . import views


app_name = 'custom_auth'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sign-up', views.SignUpView.as_view(), name='sign-up'),
    path('sign-in', views.SignInView.as_view(), name='sign-in'),
]
