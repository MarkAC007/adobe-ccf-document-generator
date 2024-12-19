import json
import sys
import os
from pathlib import Path
import base64
import time
from datetime import datetime, timedelta

# Add the parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from src.templates import PolicyTemplate
from scripts.generate_policy_from_input import PolicyGenerator
from jinja2 import Template

app = Flask(__name__, 
           static_folder=str(Path(__file__).parent.parent / 'static'),
           static_url_path='/static')
# Define allowed origins
ALLOWED_ORIGINS = [
    'http://localhost:5000',
    'https://adobe-ccf-demo.compliancegenie.io'
]

# Configure CORS with environment-aware settings
CORS(app, resources={
    r"/*": {
        "origins": ALLOWED_ORIGINS,
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"],
        "expose_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True,
        "max_age": 3600
    }
})

# Debug print to verify paths
print("Static folder path:", app.static_folder)

# After creating the Flask app
PolicyTemplate.load_templates()

# Debug logging for static files
@app.after_request
def after_request(response):
    print(f"Request: {request.path} -> Status: {response.status_code}")
    return response

# Add security headers middleware
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # Build CSP connect-src with all allowed origins
    connect_src = " ".join(["'self'"] + ALLOWED_ORIGINS)
    
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        f"connect-src {connect_src}; "
        "script-src 'self' 'unsafe-inline' cdnjs.cloudflare.com cdn.jsdelivr.net; "
        "style-src 'self' 'unsafe-inline' cdnjs.cloudflare.com; "
        "font-src 'self' cdnjs.cloudflare.com"
    )
    
    # Handle CORS headers
    origin = request.headers.get('Origin')
    if origin in ALLOWED_ORIGINS:
        response.headers['Access-Control-Allow-Origin'] = origin
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
    
    return response

def generate_policy_from_web_config(config_data, output_format='md'):
    try:
        print(f"Received config: {config_data}")  # Debug log
        generator = PolicyGenerator()
        output_file = generator.generate_policy(config_data, output_format)
        
        print(f"Generated file: {output_file}")  # Debug log
        
        # Get the filename from the output path
        filename = Path(output_file).name
        
        try:
            with open(output_file, 'rb' if output_format == 'docx' else 'r') as f:
                content = f.read()
        except PermissionError:
            # If permission error, add small delay and retry
            time.sleep(0.5)
            with open(output_file, 'rb' if output_format == 'docx' else 'r') as f:
                content = f.read()
        
        return {
            "success": True,
            "content": content if output_format == 'md' else base64.b64encode(content).decode(),
            "format": output_format,
            "filename": filename,
            "message": f"Successfully generated policy for {config_data['policy_standard']} using template {config_data.get('template_id', 'standard')}"
        }
    except Exception as e:
        print(f"Error generating policy: {str(e)}")  # Debug log
        return {"error": str(e)}

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/generate', methods=['POST'])
def generate_policy_endpoint():
    try:
        config_data = request.json
        output_format = request.args.get('format', 'md').lower()
        
        if output_format not in ['md', 'docx']:
            return jsonify({"error": "Invalid format. Use 'md' or 'docx'"})
        
        result = generate_policy_from_web_config(config_data, output_format)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/templates', methods=['GET'])
def get_templates():
    """Return available templates with metadata"""
    templates = PolicyTemplate.get_available_templates()
    # Add section information for each template
    for template_id, template in templates.items():
        sections = PolicyTemplate.get_template_sections(template_id)
        template['sections'] = sections
    return jsonify(templates)

@app.route('/template-editor')
def serve_template_editor():
    return app.send_static_file('template_editor.html')

@app.route('/api/templates', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_templates():
    if request.method == 'GET':
        templates = PolicyTemplate.get_available_templates()
        return jsonify(templates)
    
    elif request.method == 'POST':
        # Create new template
        template_data = request.json
        try:
            # Ensure required fields are present
            if not template_data.get('name'):
                raise ValueError("Template name is required")
            
            # Generate ID if not provided
            if not template_data.get('id'):
                template_data['id'] = template_data['name'].lower().replace(' ', '_')
            
            PolicyTemplate.add_template(
                template_id=template_data['id'],
                name=template_data['name'],
                description=template_data.get('description', ''),
                sections=template_data.get('sections', [])
            )
            return jsonify({"message": "Template created successfully"})
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    
    elif request.method == 'PUT':
        # Update existing template
        template_data = request.json
        try:
            if not template_data.get('id'):
                raise ValueError("Template ID is required for updates")
            
            PolicyTemplate.update_template(
                template_id=template_data['id'],
                updates={
                    'name': template_data.get('name'),
                    'description': template_data.get('description'),
                    'sections': template_data.get('sections', [])
                }
            )
            return jsonify({"message": "Template updated successfully"})
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    
    elif request.method == 'DELETE':
        # Delete template
        template_id = request.args.get('id')
        try:
            PolicyTemplate.delete_template(template_id)
            return jsonify({"message": "Template deleted successfully"})
        except Exception as e:
            return jsonify({"error": str(e)}), 400

@app.route('/api/templates/sections', methods=['GET'])
def get_available_sections():
    """Return available section types and their configurations"""
    return jsonify(PolicyTemplate.AVAILABLE_SECTIONS)

@app.route('/api/templates/<template_id>', methods=['GET'])
def get_template(template_id):
    """Get specific template details"""
    try:
        template = PolicyTemplate.get_template_details(template_id)
        return jsonify(template)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/templates/preview', methods=['POST'])
def preview_template():
    """Generate preview of template"""
    try:
        template_data = request.json
        if not template_data or 'name' not in template_data or 'sections' not in template_data:
            raise ValueError("Invalid template data")

        content = PolicyTemplate._generate_template_content(template_data['sections'])
        
        # Add sample data for preview
        preview_data = {
            "policy_standard": template_data['name'],
            "policy_standard_lower": template_data['name'].lower(),
            "current_date": datetime.now().strftime("%Y-%m-%d"),
            "next_review_date": (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d"),
            "control_sections": "Sample control section content...",
            "framework_references": "| CCF-1 | ISO 27001 | A.5.1 |\n| CCF-2 | NIST CSF | ID.AM-1 |",
            "reverse_framework_references": "| ISO 27001 | A.5.1 | CCF-1, CCF-3 |\n| NIST CSF | ID.AM-1 | CCF-2 |",
            "version": "1.0",
            "classification": "Internal",
            "owner": "Information Security Team"
        }
        
        try:
            rendered = Template(content).safe_substitute(preview_data)
            return jsonify({"content": rendered})
        except Exception as e:
            raise ValueError(f"Template rendering error: {str(e)}")
            
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/test-static')
def test_static():
    """Test route to verify static file serving"""
    return """
        <html>
            <head>
                <link rel="stylesheet" href="/static/css/styles.css">
            </head>
            <body>
                <h1>Static File Test</h1>
                <p>If you see this text in Arial font with red header background, CSS is working.</p>
            </body>
        </html>
    """

# Update the frontend API URL based on environment
@app.route('/config')
def get_config():
    api_url = os.environ.get('API_URL', 'http://localhost:5000')
    return jsonify({
        'apiUrl': api_url
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)