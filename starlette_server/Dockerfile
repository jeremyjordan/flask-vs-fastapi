FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install -r starlette_server/requirements.txt
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8002", "starlette_server.server:app"]
EXPOSE 8002