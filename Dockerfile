FROM python:3.11.4-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system dependencies
RUN apt-get update

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install gunicorn
RUN pip install django 
RUN pip install django-allauth 
RUN pip install pillow 
RUN pip install channels 
RUN pip install channels-redis 
RUN pip install python-magic 
RUN pip install python-magic-bin 
RUN pip install whitenoise 


COPY . /app

# Use Uvicorn as the entrypoint
ENTRYPOINT ["gunicorn", "BauDoMestre.wsgi", "--timeout", "180"]
