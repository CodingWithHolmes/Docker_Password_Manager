# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application
COPY main.py .

# Create a directory for persistent data
RUN mkdir /app/data

# Set the working directory as our data directory
WORKDIR /app/data

# Command to run your application
CMD ["python", "/app/main.py"]
