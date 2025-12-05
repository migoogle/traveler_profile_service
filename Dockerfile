# Use the official Python image as a base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the application will listen on
EXPOSE 8080

# Define environment variable for port
ENV PORT 8080

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--log-file=-", "--enable-stdio-inheritance", "app:app"]