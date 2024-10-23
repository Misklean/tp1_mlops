from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Initialize the FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load("regression.joblib")

# Define a request body structure using Pydantic
class HouseData(BaseModel):
    size: float
    bedrooms: int
    garden: int

# Define the /predict endpoint
@app.post("/predict")
async def predict_price(data: HouseData):
    # Extract data from the request
    input_data = [[data.size, data.bedrooms, data.garden]]
    
    # Get prediction from the model
    prediction = model.predict(input_data)
    
    # Return the prediction result
    return {"predicted_price": prediction[0]}
