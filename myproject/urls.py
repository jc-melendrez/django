from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('api_supply/',include('api_supply.urls')),
    path('brands/',include('brands.urls')),
    path('external_api/',include('externalapi.urls')),
    
    
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenObtainPairView.as_view(), name='token_refresh')

    
]
