from django.urls import path

from .views import DietDetailView, DietListCreateView


urlpatterns = [
    path(
        "",
        DietListCreateView.as_view(),
        name="diet-list-create",
    ),

    path(
        "<int:pk>/",
        DietDetailView.as_view(),
        name="diet-detail",
    ),
]