from django.urls import path
from . import views

urlpatterns = [
    path("", views.bio_page, name="bio_page"),
]
