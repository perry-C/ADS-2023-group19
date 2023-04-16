from django.urls import path

from . import views

app_name = 'graph_vis'


urlpatterns = [
    path("", views.index, name="index"),
]
