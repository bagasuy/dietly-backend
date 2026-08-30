from rest_framework import serializers

from .models import DietEntry, WeightHistory


class DietEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = DietEntry
        fields = (
            "id",
            "user",
            "food_name",
            "meal_type",
            "calories",
            "protein",
            "carbohydrates",
            "fat",
            "consumed_at",
            "created_at",
        )

        read_only_fields = (
            "id",
            "user",
            "created_at",
        )
class WeightHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = WeightHistory
        fields = (
            "id",
            "user",
            "weight",
            "recorded_at",
            "created_at",
        )

        read_only_fields = (
            "id",
            "user",
            "created_at",
        )