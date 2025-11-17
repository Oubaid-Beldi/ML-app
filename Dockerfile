# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY models/ ./models/

# Create directory for models if it doesn't exist
RUN mkdir -p models

# Set Python path
ENV PYTHONPATH=/app

# Default command
CMD ["python", "src/train.py"]
