from django.urls import path

from.views import doc_json

urlpatterns = [
    path("", doc_json, name="home"),
]