from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('items', views.list_item, name="item_list")
]
