# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy entrypoint.sh to the container
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# Copy the rest of the project files to the container
COPY . /app/

# Run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
