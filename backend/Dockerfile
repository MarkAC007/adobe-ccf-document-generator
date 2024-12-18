FROM python:3.9-slim

# Install pandoc for document conversion
RUN apt-get update && \
    apt-get install -y pandoc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY src/ ./src/
COPY scripts/ ./scripts/
COPY data/ ./data/
COPY templates/ ./templates/

# Copy static files
COPY static/ ./static/
COPY index.html ./static/
COPY template_editor.html ./static/

# Create necessary directories
RUN mkdir -p output/policies

# Set environment variables
ENV PYTHONPATH=/app

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "scripts/generate_policy_from_web.py"] 