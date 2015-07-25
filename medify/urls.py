from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^pharmacies/$", views.pharmacies, name="pharmacies"),
    url(r"^$", views.index, name="index"),
]
