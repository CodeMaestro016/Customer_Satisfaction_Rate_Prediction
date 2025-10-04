# Use official Python image
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements first to leverage caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . .

# Expose Flask default port
EXPOSE 5000

# Command to run your app
CMD ["python", "website/app.py"]
