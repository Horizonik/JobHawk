# Use a lightweight Python image as the base
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /app

# Get env variables from github actions secrets
ARG ENV_VARIABLES

# Set the values of ENV variables to the ARG values
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
ENV DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}
ENV DJANGO_DEBUG=${DJANGO_DEBUG}
ENV DJANGO_SECURE_SSL_REDIRECT=${DJANGO_SECURE_SSL_REDIRECT}
ENV DJANGO_SESSION_COOKIE_HTTPONLY=${DJANGO_SESSION_COOKIE_HTTPONLY}

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js and npm for the frontend
RUN apt-get update && apt-get install -y nodejs npm

# Copy the frontend and backend code into the container
COPY frontend /app/frontend
COPY backend /app/backend

# Install the frontend dependencies and build the production bundle
WORKDIR /app/frontend
RUN npm install && npm run build

# Copy the production bundle to the backend
WORKDIR /app/backend
RUN mkdir -p static && cp -r ../frontend/build/* static/

# Expose the port used by nginx
EXPOSE 80
EXPOSE 443

# Install nginx and configure it to serve the app with HTTPS
RUN apt-get update && apt-get install -y nginx openssl
COPY nginx.conf /etc/nginx/nginx.conf
COPY certs/ssl.crt /etc/ssl/certs/nginx.crt
COPY certs/ssl.key /etc/ssl/private/nginx.key
RUN rm /etc/nginx/sites-enabled/default

# Copy the gunicorn configuration file into the container
COPY gunicorn.conf /app/gunicorn.conf

# Copy the start script into the container
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Start the app with the start script
CMD ["/app/start.sh"]