from django.utils import timezone
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from .models import Prediction
from .serializers import PredictionSerializer
from .services.predictor import generate_mock_prediction


class PredictionListCreateView(generics.ListCreateAPIView):
    serializer_class = PredictionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Prediction.objects.filter(
            user=self.request.user
        ).order_by("-created_at")

    def perform_create(self, serializer):
        weight = self.request.data.get("weight")

        if weight is None:
            raise ValidationError({
                "weight": "This field is required."
            })

        result = generate_mock_prediction(weight)

        serializer.save(
            user=self.request.user,
            predicted_change=result["predicted_change"],
            predicted_weight=result["predicted_weight"],
            prediction_date=timezone.localdate(),
        )
