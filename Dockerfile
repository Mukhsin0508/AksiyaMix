FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip --root-user-action=ignore && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/pip /root/.cache && \
    apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./src /app

# If you're creating a non-root user for security reasons, uncomment these
# Create a non-root user and change file ownership (optional)
# RUN adduser --disabled-password --gecos '' celery-user
# RUN chown -R celery-user:celery-user /app
# Switch to the non-root user (optional)
# USER celery-user

# Default command to run the Django app (or any custom command)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
