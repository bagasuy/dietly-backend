from django.urls import path

from .views import PredictionListCreateView


urlpatterns = [
    path(
        "",
        PredictionListCreateView.as_view(),
        name="prediction-list-create",
    ),
]