from pydantic import BaseModel , Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category : str = Field(
        ...,
        description="The predicted insurance premium category",
        example="High"
    )

    confidence : float = Field(
        ...,
        description="The confidence score of the prediction (between 0 and 1)",
        example=0.8432
    )

    class_probabilities : Dict[str, float] = Field(
        ...,
        description="A dictionary containing the probabilities for each insurance premium category",
        example={"Low": 0.01, "Medium": 0.15, "High": 0.84}
    )

