# flask-vs-fastapi
An exploration comparing Flask with FastAPI.


Running Flask.
```
docker build -t flask-image -f flask_server/Dockerfile .
docker run -it --rm -p 8000:8000 flask-image
```

Running FastAPI.
```
docker build -t fastapi-image -f fastapi_server/Dockerfile .
docker run -it --rm -p 8001:8001 fastapi-image
```
