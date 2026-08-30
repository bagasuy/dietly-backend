from rest_framework import serializers

from .models import DietEntry


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
        