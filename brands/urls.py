from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandsViewSet


router = DefaultRouter()
router.register(r'brands',BrandsViewSet)
urlpatterns = [
        path('',include(router.urls)),
    ]
