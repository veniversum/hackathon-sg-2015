from django.conf.urls import url

from . import views

urlpatterns = [
    # Templates
    url(r"^pharmacies/$", views.pharmacies, name="pharmacies"),
    url(r"^$", views.index, name="index"),

    # AJAX stuff
    url(r"^search/$", views.omni_search2, name="ajax_search"),
    url(r"^advanced_search/$", views.adv_search, name="ajax_search"),
]
