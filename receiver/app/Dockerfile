# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy script into the container
COPY receiver.py .

# Install dependencies if required (add your dependencies here)
RUN pip install --no-cache-dir paho-mqtt

# Run the Python script
CMD ["python" ,"-u", "receiver.py"]
