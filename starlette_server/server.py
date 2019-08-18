from starlette.applications import Starlette
from starlette.responses import JSONResponse
import uvicorn

from model import load_model

app = Starlette()
model = load_model()


@app.route("/", methods=["GET"])
async def index(request):
    return JSONResponse(f"Serving a {model.__class__.__name__} model using Starlette.")


@app.route("/predict", methods=["POST"])
async def predict(request):
    body = await request.json()
    prediction = model.predict(body["X"])
    return JSONResponse({"y": prediction.tolist()})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
