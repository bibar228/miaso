
from django.urls import path
from . import views
from .views import order_view

urlpatterns = [

    path("order/", order_view)
]