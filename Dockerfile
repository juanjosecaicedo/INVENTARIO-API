# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Definir variables de entorno por defecto
ENV DATABASE_URL=sqlite:///data/database.db
ENV PORT=8000
ENV HOST=0.0.0.0

# Copiar las dependencias instaladas
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

RUN mkdir -p /app/data

EXPOSE 8000

CMD ["sh", "-c", "uvicorn main:app --host $HOST --port $PORT --workers 2"]