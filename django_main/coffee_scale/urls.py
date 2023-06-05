from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_dummy_data, name="index"),
    path("get_weight/", views.get_weight_dummy, name="get_weight"),
]
