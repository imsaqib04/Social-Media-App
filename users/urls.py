from django.urls import path
from django.contrib.auth import views as auth_view
from . import views


urlpatterns = [

    path("login/",views.user_login,name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
]
