# flask-vs-fastapi
An exploration comparing Flask with FastAPI.


Running Flask.
```
docker build -t flask-image -f flask_server/Dockerfile .
docker run -it --rm -p 8000:8000 flask-image
locust -f load_testing/locustfile.py --host=http://127.0.0.1:8000
```

Running FastAPI.
```
docker build -t fastapi-image -f fastapi_server/Dockerfile .
docker run -it --rm -p 8001:8001 fastapi-image
locust -f load_testing/locustfile.py --host=http://127.0.0.1:8001
```

Both servers have two basic routes (index and predict) and are load tested with Locust.

Some nice features in FastAPI:

- Data validation on input posted to the server.
- Automatic documentation found in `/docs`.
- Slight performance boost over using Flask with Gunicorn.

## Automatic data validation based on Python types

One really nice thing about FastAPI is that we don't have to perform checks to ensure the input is in the expected format. FastAPI uses the type hints to make sure that data posted is in the proper format, or else it will return an informative error. 

Run the FastAPI server. The predict route expects a body with one attribute `X` containing a list of list of floats. 

```
>>> import requests
>>> import numpy as np 
>>> payload = {"X": np.random.randn(2, 13).tolist()}
>>> r = requests.post('http://127.0.0.1:8001/predict', json=payload)
>>> r.json()
{'y': [45.140628195389766, 36.78772305402535]}
```

Now let's intentionally mess up the body to contain `x` instead of `X`. Now the server complains that the posted body is missing a required attribute `X`. 

```
>>> # now pass in data in an unexpected format
>>> payload = {"x": np.random.randn(2, 13).tolist()}
>>> r = requests.post('http://127.0.0.1:8001/predict', json=payload)
>>> r.json()
{'detail': [{'loc': ['body', 'observation', 'X'], 'msg': 'field required', 'type': 'value_error.missing'}]}
```

If we pass in an improper data type, we'll similarly get a useful error response from the server.

```
>>> payload = {"X": [['testing', 'data', 'validation']]}
>>> r = requests.post('http://127.0.0.1:8001/predict', json=payload)
>>> r.json()
{'detail': [{'loc': ['X', 0, 0], 'msg': 'value is not a valid float', 'type': 'type_error.float'}, {'loc': ['X', 0, 1], 'msg': 'value is not a valid float', 'type': 'type_error.float'}, {'loc': ['X', 0, 2], 'msg': 'value is not a valid float', 'type': 'type_error.float'}]}
```

## Exploring Starlette

FastAPI uses Starlette under the hood, so I also made a complementary server in Starlette to see what kind of performance hit we take for all of FastAPI's nice features.

```
docker build -t starlette-image -f starlette_server/Dockerfile .
docker run -it --rm -p 8002:8002 starlette-image
locust -f load_testing/locustfile.py --host=http://127.0.0.1:8002
```