"""
URL configuration for yolki_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path
from Scrapping_API.views import SignupAPIView , LoginAPIView 
from rest_framework import permissions
from drf_yasg import openapi

handler404 = 'Scrapping_API.views.custom_404'


schema_view = get_schema_view(
    openapi.Info(
        title="Yolki Rest Backend",
        default_version='v3',
        description="API description",
        terms_of_service="---",
        contact=openapi.Contact(email="---"),
        license=openapi.License(name="---"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignupAPIView(), name='signup'),
    path('login/' , LoginAPIView() ,name='login'),   
]
