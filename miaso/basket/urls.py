
from django.urls import path
from . import views
from .views import OrderView

urlpatterns = [

    path("order/", OrderView.as_view({'get': 'list'}))
]