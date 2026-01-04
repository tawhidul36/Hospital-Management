FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (for Postgres, pycairo, etc.)
RUN apt-get update \
    && apt-get install -y gcc libpq-dev libcairo2-dev pkg-config python3-dev build-essential \
    && apt-get clean

# Copy requirements
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Run server
CMD ["gunicorn", "hospitalmanagement.wsgi:application", "--bind", "0.0.0.0:8000"]

