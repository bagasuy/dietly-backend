from django.contrib import admin
from .models import DietEntry, WeightHistory


@admin.register(DietEntry)
class DietEntryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "food_name",
        "meal_type",
        "calories",
        "protein",
        "carbohydrates",
        "fat",
        "consumed_at",
    )

    list_filter = (
        "meal_type",
        "consumed_at",
    )

    search_fields = (
        "food_name",
        "user__email",
    )


@admin.register(WeightHistory)
class WeightHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "weight",
        "recorded_at",
    )

    list_filter = (
        "recorded_at",
    )

    search_fields = (
        "user__email",
    )