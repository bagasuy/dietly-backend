from django.contrib import admin
from .models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "predicted_change",
        "predicted_weight",
        "prediction_date",
        "created_at",
    )

    list_filter = (
        "prediction_date",
    )

    search_fields = (
        "user__username",
        "user__email",
    )