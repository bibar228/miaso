
from django.urls import path
from . import views
from .views import OrderView, CreateOrderView, CreateOrderItemView

urlpatterns = [
    path("order_create/", CreateOrderView.as_view()),
    path("order/", OrderView.as_view({'get': 'list'})),
    path("orderitem_create/", CreateOrderItemView.as_view())
    #path("jopka/", jopka)
]