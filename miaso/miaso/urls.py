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
from django.urls import path
from rest_framework.routers import SimpleRouter, Route
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from main.views import CopchViewSet, PolyViewSet, ColdViewSet
from miaso import settings


class CustomReadOnlyRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [Route(url=r'{prefix}', mapping={'get': 'list'}, name='{basename}-list', detail=False, initkwargs={'suffix': 'List'})]


router = CustomReadOnlyRouter()

router.register(r"copch", CopchViewSet)
router.register(r"poly", PolyViewSet)
router.register(r"cold", ColdViewSet)

urlpatterns = [
    path('admin/', admin.site.urls)

]

urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)