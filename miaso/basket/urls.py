
from django.urls import path
from . import views
from .views import OrderView, PostOrderView

urlpatterns = [
    path("post_order/", PostOrderView.as_view()),
    path("order/", OrderView.as_view({'get': 'list'}))
]