# Use Python official image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /tests

# Copy requirements.txt and install dependencies
COPY requirements.txt /tests/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test script to the container
COPY uat.py /tests

# Wait for Flask app to be ready
CMD ["sh", "-c", "sleep 10 && python uat.py"]