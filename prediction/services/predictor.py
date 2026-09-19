from decimal import Decimal
from pathlib import Path

import joblib
import pandas as pd
from scipy.sparse import hstack


MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "ml_models"
    / "dietly_weight_model.joblib"
)


model_bundle = joblib.load(MODEL_PATH)

model = model_bundle["model"]
tfidf = model_bundle["tfidf"]


def generate_prediction(
    previous_weight,
    weight,
    historical_weight_change,
    dietary_text,
):
    """
    Generate a future-weight prediction using the trained
    DietDiary Ridge Regression model.

    Parameters
    ----------
    previous_weight : Decimal or float
        Previous recorded weight in kilograms.

    weight : Decimal or float
        Current recorded weight in kilograms.

    historical_weight_change : Decimal or float
        Difference between current and previous weight.

    dietary_text : str
        Combined dietary information from the user's meal records.

    Returns
    -------
    dict
        Contains predicted weight and predicted change.
    """

    if previous_weight is None:
        raise ValueError("Previous weight is required.")

    if weight is None:
        raise ValueError("Current weight is required.")

    if historical_weight_change is None:
        raise ValueError(
            "Historical weight change is required."
        )

    if dietary_text is None:
        dietary_text = ""

    numeric_features = pd.DataFrame(
        [[
            float(previous_weight),
            float(weight),
            float(historical_weight_change),
        ]],
        columns=[
            "previous_weight",
            "weight",
            "historical_weight_change",
        ],
    ).values

    text_features = tfidf.transform(
        [str(dietary_text)]
    )

    final_features = hstack([
        numeric_features,
        text_features,
    ])

    prediction = model.predict(final_features)[0]

    predicted_weight = Decimal(
        str(round(float(prediction), 2))
    )

    current_weight = Decimal(str(weight))

    predicted_change = (
        predicted_weight - current_weight
    )

    return {
        "predicted_weight": predicted_weight,
        "predicted_change": predicted_change,
    }