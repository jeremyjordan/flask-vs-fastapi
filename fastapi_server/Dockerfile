FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install -r fastapi_server/requirements.txt
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8001", "fastapi_server.server:app"]
EXPOSE 8001
