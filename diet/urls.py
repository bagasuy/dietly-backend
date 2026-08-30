from django.urls import path

from .views import (
    DietDetailView, 
    DietListCreateView,
    WeightHistoryListCreateView,
)


urlpatterns = [
    path(
        "",
        DietListCreateView.as_view(),
        name="diet-list-create",
    ),

 path(
        "weight/",
        WeightHistoryListCreateView.as_view(),
        name="weight-list-create",
    ),

    path(
        "<int:pk>/",
        DietDetailView.as_view(),
        name="diet-detail",
    ),
]