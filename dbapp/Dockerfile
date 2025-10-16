# Use official lightweight Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files (app, model, templates, etc.)
COPY . .

# Expose Flask port
EXPOSE 8001

# Run app
CMD ["python", "app.py"]
