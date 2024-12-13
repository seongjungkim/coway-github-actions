FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY src/main.py /app/main.py
COPY src/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint
ENTRYPOINT ["python", "/app/main.py"]
