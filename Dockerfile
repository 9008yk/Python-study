FROM python:3.13-slim

WORKDIR /app

RUN mkdir -p /app/data

COPY week02/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TODOS_DB=/app/data/todos.db
ENV SECRET_KEY=dev-secret-key-change-me-please-32-bytes-min
ENV CORS_ORIGINS=*

EXPOSE 8000

CMD ["uvicorn", "week03.main:app", "--host", "0.0.0.0", "--port", "8000"]
