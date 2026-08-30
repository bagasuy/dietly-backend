from rest_framework import serializers

from .models import Prediction


class PredictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prediction
        fields = (
            "id",
            "user",
            "predicted_change",
            "predicted_weight",
            "prediction_date",
            "created_at",
        )

        read_only_fields = (
            "id",
            "user",
            "predicted_change",
            "predicted_weight",
            "prediction_date",
            "created_at",
        )