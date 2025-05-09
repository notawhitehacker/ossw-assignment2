FROM python:3.12.1-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=project.settings

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && pip install --no-cache-dir -r django

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app/

# Expose the port Django will run on
EXPOSE 8000

# Run Django commands
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]