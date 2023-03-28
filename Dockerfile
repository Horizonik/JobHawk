# Stage 1: Build React frontend
FROM node:14 as frontend-builder
WORKDIR /app/frontend
COPY ./frontend/package*.json ./
RUN npm ci
COPY ./frontend .
RUN npm run build

# Stage 2: Build Django backend
FROM python:3.10.10-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

RUN useradd --create-home appuser
WORKDIR $APP_HOME

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev openssl && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY ./backend/requirements.txt $APP_HOME/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend $APP_HOME
COPY --from=frontend-builder /app/frontend/build $APP_HOME/static

# Generate a self-signed SSL certificate
RUN openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -subj "/C=US/ST=CA/L=SF/O=YourOrg/OU=YourOU/CN=localhost" -nodes
RUN mkdir certs && mv key.pem cert.pem certs

# Change the ownership of the app directory to the non-root user
RUN chown -R appuser:appuser $APP_HOME
USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--certfile", "certs/cert.pem", "--keyfile", "certs/key.pem", "backend.wsgi:application"]