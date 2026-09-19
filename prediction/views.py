from django.utils import timezone
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from diet.models import DietEntry, WeightHistory

from .models import Prediction
from .serializers import PredictionSerializer
from .services.predictor import generate_prediction


class PredictionListCreateView(generics.ListCreateAPIView):
    serializer_class = PredictionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Prediction.objects.filter(
            user=self.request.user
        ).order_by("-created_at")

    def perform_create(self, serializer):
        user = self.request.user

        # Get the most recent weight record
        latest_weight = (
            WeightHistory.objects
            .filter(user=user)
            .order_by("-recorded_at")
            .first()
        )

        if latest_weight is None:
            raise ValidationError({
                "weight": (
                    "Please record your weight before generating "
                    "a prediction."
                )
            })

        # Get the most recent weight record from an earlier date
        previous_weight_record = (
            WeightHistory.objects
            .filter(
                user=user,
                recorded_at__date__lt=latest_weight.recorded_at.date(),
            )
            .order_by("-recorded_at")
            .first()
        )

        if previous_weight_record is None:
            raise ValidationError({
                "weight": (
                    "Please record your weight on at least "
                    "two different dates before generating "
                    "a prediction."
                )
            })

        current_weight = latest_weight.weight
        previous_weight = previous_weight_record.weight

        historical_weight_change = (
            current_weight - previous_weight
        )

        # Get recent dietary records
        diet_entries = (
            DietEntry.objects
            .filter(user=user)
            .order_by("-consumed_at")[:20]
        )

        dietary_parts = []

        for entry in diet_entries:
            dietary_parts.append(
                f"{entry.meal_type} {entry.food_name}"
            )

        dietary_text = " ".join(dietary_parts)

        # Generate ML prediction
        result = generate_prediction(
            previous_weight=previous_weight,
            weight=current_weight,
            historical_weight_change=historical_weight_change,
            dietary_text=dietary_text,
        )

        predicted_weight = result["predicted_weight"]
        predicted_change = result["predicted_change"]

        serializer.save(
            user=user,
            predicted_change=predicted_change,
            predicted_weight=predicted_weight,
            prediction_date=timezone.localdate(),
        )