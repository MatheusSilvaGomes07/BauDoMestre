FROM python:3.11.4-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system dependencies
RUN apt-get update

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

# Use Uvicorn as the entrypoint
ENTRYPOINT ["uvicorn", "BauDoMestre.wsgi:application", "--host", "0.0.0.0" "--port", "4040"]
