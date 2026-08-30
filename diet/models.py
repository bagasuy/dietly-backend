from django.conf import settings
from django.db import models


class DietEntry(models.Model):

    MEAL_TYPES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
        ("snack", "Snack"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="diet_entries"
    )

    food_name = models.CharField(max_length=200)

    meal_type = models.CharField(
        max_length=20,
        choices=MEAL_TYPES
    )

    calories = models.PositiveIntegerField()

    protein = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    carbohydrates = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    fat = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    consumed_at = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.food_name} - {self.user.email}"


class WeightHistory(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="weight_history"
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    recorded_at = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["recorded_at"]

    def __str__(self):
        return f"{self.user.email} - {self.weight} kg"