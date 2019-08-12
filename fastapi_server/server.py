from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from model import load_model


class Observation(BaseModel):
    X: List[float]


app = FastAPI()
model = load_model()


@app.get("/")
async def index():
    return f'Serving a {model.__class__.__name__} model using FastAPI.'


@app.post('/predict')
async def predict(observation: Observation):
    prediction = model.predict(observation.X)
    return {'y': prediction.tolist()}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
