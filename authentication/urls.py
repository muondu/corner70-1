from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [    
    path('', views.home, name="home"),
    # path('signup',views.signup, name="signup"),
    path('signin',views.signin, name="signin"),
    path('contribution',views.contribution, name="contribution"),
    path('signout',views.signout, name="signout"),
]
