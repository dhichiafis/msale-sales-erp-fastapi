FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the application code
COPY . /app

# Expose port 8000
EXPOSE 8000

# Create a directory for Gunicorn logs (Optional)
RUN mkdir /app/logs

# Add command to run migrations before starting Gunicorn
CMD ["sh", "-c", "alembic upgrade head && gunicorn main:app --workers 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --log-level error --access-logfile /app/logs/access.log --error-logfile /app/logs/error.log"]
