from decimal import Decimal


def generate_mock_prediction(weight):
    """
    Temporary mock prediction.

    This function will be replaced by the actual
    machine learning inference logic later.
    """

    weight = Decimal(str(weight))

    predicted_change = Decimal("-0.50")
    predicted_weight = weight + predicted_change

    return {
        "predicted_change": predicted_change,
        "predicted_weight": predicted_weight,
    }