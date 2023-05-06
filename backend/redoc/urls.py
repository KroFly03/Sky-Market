from django.urls import path

from redoc.views import redoc_json, redoc

urlpatterns = [
    path("", redoc),
    path("json/", redoc_json)
]