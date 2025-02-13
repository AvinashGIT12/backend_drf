"""drfecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  drfecommerce.product import views  # Make sure views is correctly imported
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
router = DefaultRouter()
router.register(r'category', views.CategoryView, basename='category')  # Ensure CategoryView is defined and imported
router.register(r'brand',views.BrandView,basename="brand")
router.register(r'product',views.ProductView,basename="product")
urlpatterns = [path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path("api/schema/",SpectacularAPIView.as_view(),name="schema"),
    path("api/schema/docs/",SpectacularSwaggerView.as_view(url_name="schema")),
]

  