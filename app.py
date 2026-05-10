from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load the files
model = joblib.load('diabetes_model.pkl')
cols = joblib.load('training_columns.pkl')

# Define input schema
class Patient(BaseModel):
    AGE: float
    Urea: float
    Cr: float
    HbA1c: float
    Chol: float
    TG: float
    HDL: float
    LDL: float
    VLDL: float
    BMI: float
    Gender: str

# Serve the HTML file at the root route
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as f:
        return f.read()

@app.post("/predict")
def predict(data: Patient):
    input_dict = data.dict()
    gender_m = 1 if input_dict['Gender'].upper() == 'M' else 0
    
    features = {**input_dict, 'Gender_M': gender_m}
    del features['Gender']
    
    input_df = pd.DataFrame([features])[cols]
    prediction = model.predict(input_df)[0]
    
    res = {0: 'Normal', 1: 'Pre-diabetic', 2: 'Diabetic'}
    return {"status": res.get(prediction)}