# Use a lightweight Python image as the base
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js and npm for the frontend
RUN apt-get update && apt-get install -y nodejs npm
RUN npm install -g yarn

# Copy the frontend and backend code into the container
COPY frontend /app/frontend
COPY backend /app/backend

# Install the frontend dependencies and build the production bundle
WORKDIR /app/frontend
RUN yarn install --verbose && yarn build --verbose

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

# Start the app with gunicorn and nginx
CMD ["gunicorn", "-c", "/app/gunicorn.conf", "backend.wsgi:application"]
