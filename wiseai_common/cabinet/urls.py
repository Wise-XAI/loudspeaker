from django.urls import path
from .views import index_template_view

app_name = "cabinet"

urlpatterns = [
    path("", index_template_view, name="index"),
]