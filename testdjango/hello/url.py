from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jun", views.jun, name="jun"),
    path("<str:name>", views.greet, name="greet")
]