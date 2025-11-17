#!/usr/bin/env python3
"""
FastAPI application for Iris classifier
Provides REST API endpoints for predictions
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict
import uvicorn
import os

from model import IrisClassifier
from data_loader import get_target_names


# Pydantic models for request/response
class IrisFeatures(BaseModel):
    sepal_length: float = Field(..., description="Sepal length in cm", ge=0)
    sepal_width: float = Field(..., description="Sepal width in cm", ge=0)
    petal_length: float = Field(..., description="Petal length in cm", ge=0)
    petal_width: float = Field(..., description="Petal width in cm", ge=0)

    class Config:
        json_schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }


class PredictionResponse(BaseModel):
    prediction: str
    class_id: int
    probabilities: Dict[str, float]
    features: List[float]


class BatchPredictionRequest(BaseModel):
    instances: List[IrisFeatures]


class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]
    count: int


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    target_classes: List[str]

    class Config:
        protected_namespaces = ()


# Initialize FastAPI app
app = FastAPI(
    title="Iris Classifier API",
    description="REST API for Iris flower classification using Logistic Regression",
    version="1.0.0"
)

# Global variables for model
classifier = None
target_names = None
model_loaded = False


def load_model():
    """Load the trained model at startup"""
    global classifier, target_names, model_loaded
    try:
        model_path = os.getenv('MODEL_PATH', 'models/iris_classifier.pkl')
        classifier = IrisClassifier()
        classifier.load_model(model_path)
        target_names = get_target_names()
        model_loaded = True
        print(f"✅ Model loaded successfully from {model_path}")
        return True
    except FileNotFoundError:
        print("⚠️ Model not found. Please train the model first.")
        model_loaded = False
        return False
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        model_loaded = False
        return False


def predict_species(features: List[float]) -> PredictionResponse:
    """Make a prediction for given features"""
    if classifier is None or target_names is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please train the model first."
        )

    try:
        # Make prediction
        prediction = classifier.predict([features])[0]
        probabilities = classifier.model.predict_proba([features])[0]

        # Format response
        prob_dict = {
            target_names[i]: float(prob)
            for i, prob in enumerate(probabilities)
        }

        return PredictionResponse(
            prediction=target_names[prediction],
            class_id=int(prediction),
            probabilities=prob_dict,
            features=features
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Startup event
@app.on_event("startup")
async def startup_event():
    """Load model when application starts"""
    load_model()


# API Endpoints
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Iris Classifier API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "predict": "/predict",
            "batch_predict": "/predict/batch",
            "docs": "/docs"
        }
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy" if model_loaded else "unhealthy",
        model_loaded=model_loaded,
        target_classes=list(target_names) if target_names is not None and len(target_names) > 0 else []
    )


@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict(features: IrisFeatures):
    """
    Make a prediction for a single iris flower.

    Parameters:
    - sepal_length: Length of the sepal in cm
    - sepal_width: Width of the sepal in cm
    - petal_length: Length of the petal in cm
    - petal_width: Width of the petal in cm

    Returns prediction with probabilities for each class.
    """
    feature_list = [
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]
    return predict_species(feature_list)


@app.post(
    "/predict/batch",
    response_model=BatchPredictionResponse,
    tags=["Prediction"]
)
async def predict_batch(request: BatchPredictionRequest):
    """
    Make predictions for multiple iris flowers.

    Accepts a list of iris flower measurements and returns
    predictions for each instance.
    """
    predictions = []
    for instance in request.instances:
        feature_list = [
            instance.sepal_length,
            instance.sepal_width,
            instance.petal_length,
            instance.petal_width
        ]
        pred = predict_species(feature_list)
        predictions.append(pred)

    return BatchPredictionResponse(
        predictions=predictions,
        count=len(predictions)
    )


# Run the application
if __name__ == "__main__":
    # Load model before starting server
    load_model()

    # Start server
    port = int(os.getenv('PORT', 8000))
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
