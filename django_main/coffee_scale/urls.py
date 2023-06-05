from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_dummy_data, name="index"),
]
