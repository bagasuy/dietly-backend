from django.conf import settings
from django.db import models


class Prediction(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="predictions"
    )

    predicted_change = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )

    predicted_weight = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True
    )

    prediction_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.email} - {self.predicted_change}"