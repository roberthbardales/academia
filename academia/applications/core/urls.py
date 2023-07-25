from django.contrib import admin
from django.urls import path

from .views import HomeView, PricingView

app_name = "core_app"

urlpatterns = [
    path('',
        HomeView.as_view(),
        name='home'
    ),
    path('pricing/',
        PricingView.as_view(),
        name='pricing'
    ),

]


