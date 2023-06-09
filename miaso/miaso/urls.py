"""
URL configuration for miaso project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from basket import urls
from main.views import CopchViewSet, ColdViewSet, PolyViewSet

from miaso import settings
from users.views import RegistrUserView, base, LoginView

schema_view = get_schema_view(
    openapi.Info(
        title="Django miaso",
        default_version="v2",
        description="Description",
        license=openapi.License(name="BSD License"),
    ),
    public=True
)


urlpatterns = [
    path("goods/copch/", CopchViewSet.as_view({'get': 'list'})),
    path("goods/cold/", ColdViewSet.as_view({'get': 'list'})),
    path("goods/poly/", PolyViewSet.as_view({'get': 'list'})),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path('admin/', admin.site.urls),
    #path("auth/", include("djoser.urls")),
    re_path("auth/", include("djoser.urls.authtoken")),
    path('api-auth', include('rest_framework.urls')),
    path('auth/registr/', RegistrUserView.as_view(), name='registr'),
    #path("", telega),
    path("", base),
    #path("accounts/", include("django.contrib.auth.urls")),
    path("auth/log/", LoginView.as_view())
]

urlpatterns += urls.urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)