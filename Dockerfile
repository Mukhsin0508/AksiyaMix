FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Create a non-root user
# RUN adduser --disabled-password --gecos '' celery-user

COPY ./src /app

# Change the ownership of the application to the created user
# RUN chown -R celery-user:celery-user /app

# Switch to the non-root user
#USER celery-user
