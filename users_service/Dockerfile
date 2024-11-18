FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY users_service/users_service.py .
CMD ["python", "users_service.py"]