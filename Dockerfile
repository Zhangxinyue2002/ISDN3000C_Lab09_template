# Start from a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files from FlaskApp directory
COPY FlaskApp/app.py .
COPY FlaskApp/init_db.py .
COPY FlaskApp/schema.sql .
COPY FlaskApp/templates ./templates

# Inform Docker that the container listens on port 5000
EXPOSE 5000

RUN python init_db.py

# Define the command to run the application when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]