FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install -r flask_server/requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:8000", "flask_server.server:app"]
EXPOSE 8000