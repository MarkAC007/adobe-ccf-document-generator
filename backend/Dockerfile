FROM python:3.13-slim

# Install pandoc and essential build tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    pandoc \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd -m -r appuser

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --upgrade pip setuptools

# Copy the backend code
COPY src/ ./src/
COPY scripts/ ./scripts/
COPY data/ ./data/
COPY templates/ ./templates/

# Copy static files
COPY static/ ./static/
COPY index.html ./static/
COPY template_editor.html ./static/

# Create necessary directories and set permissions
RUN mkdir -p output/policies && \
    chown -R appuser:appuser /app

# Set environment variables with localhost as default
ENV PYTHONPATH=/app
ENV BASE_URL=http://localhost:5000

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "scripts/generate_policy_from_web.py"] 