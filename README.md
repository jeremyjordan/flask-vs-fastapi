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