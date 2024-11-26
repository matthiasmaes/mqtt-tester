FROM python:3.9-slim
WORKDIR /app
COPY sender.py .
RUN pip install --no-cache-dir paho-mqtt
CMD ["python", "-u", "./sender.py"]