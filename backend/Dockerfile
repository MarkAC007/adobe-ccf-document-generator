FROM python:3.10-slim

# Install pandoc for document conversion
RUN apt-get update && \
    apt-get install -y pandoc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/backend

# Copy requirements and install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend files
COPY ./scripts ./scripts
COPY ./src ./src
COPY ./data ./data
COPY ./index.html .

# Create output directory
RUN mkdir -p output/policies

# Set environment variables
ENV PYTHONPATH=/app/backend

# Expose port
EXPOSE 5000

# Start the application
CMD ["python", "scripts/generate_policy_from_web.py"] 