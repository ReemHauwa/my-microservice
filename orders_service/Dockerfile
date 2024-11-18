# Dockerfile for Order Service
## Save as: orders_service/Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY orders_service/orders_service.py .
CMD ["python", "orders_service.py"]