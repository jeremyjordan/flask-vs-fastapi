FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install -r fastapi_server/requirements.txt
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8001", "fastapi_server.server:app"]
EXPOSE 8001