FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create necessary directories
RUN mkdir -p /app/data/raw_contracts /app/outputs /app/uploads

# Copy the rest of the application
COPY . .

# Expose the port Hugging Face expects (7860)
EXPOSE 7860

# Run FastAPI using uvicorn on port 7860
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
