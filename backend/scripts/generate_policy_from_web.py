import json
import sys
import os
from pathlib import Path
import base64
import time
from datetime import datetime, timedelta

# Add the parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from src.templates import PolicyTemplate
from scripts.generate_policy_from_input import PolicyGenerator
from jinja2 import Template
from src.document_converter import DocumentConverter
import tempfile
from pathlib import Path
from src.framework_mapper import FrameworkMapper

# Get base URL from environment variable with fallback for local development
BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')

# Set up paths
BACKEND_DIR = Path(__file__).parent.parent
STATIC_DIR = BACKEND_DIR / 'static'
TEMPLATES_DIR = BACKEND_DIR / 'templates'

app = Flask(__name__, 
           static_folder=str(STATIC_DIR),
           template_folder=str(TEMPLATES_DIR),
           static_url_path='/static')

# Configure Swagger UI
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI
API_YAML_URL = '/static/openapi.yaml'  # Our API YAML file

# Create Swagger UI blueprint
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_YAML_URL,
    config={
        'app_name': "Adobe CCF Document Generator API"
    }
)

# Register Swagger UI blueprint
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Configure CORS to allow local development
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:5000", "http://127.0.0.1:5000", BASE_URL],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

# Debug print to verify paths
print("Static folder path:", app.static_folder)
print("Template folder path:", app.template_folder)

# After creating the Flask app
PolicyTemplate.load_templates()

# Debug logging for static files
@app.after_request
def after_request(response):
    print(f"Request: {request.path} -> Status: {response.status_code}")
    return response

# Update security headers to use BASE_URL
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # Use BASE_URL in CSP
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        f"connect-src 'self' {BASE_URL}; "
        "script-src 'self' 'unsafe-inline' cdnjs.cloudflare.com cdn.jsdelivr.net; "
        "style-src 'self' 'unsafe-inline' cdnjs.cloudflare.com; "
        "font-src 'self' cdnjs.cloudflare.com"
    )
    
    # Handle CORS headers
    origin = request.headers.get('Origin')
    if origin == BASE_URL:
        response.headers['Access-Control-Allow-Origin'] = origin
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
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
    try:
        return send_from_directory(app.static_folder, 'index.html')
    except Exception as e:
        print(f"Error serving index.html: {str(e)}")
        return f"Error: {str(e)}", 500

@app.route('/framework-mapping')
def framework_mapping():
    try:
        return send_from_directory(app.static_folder, 'framework-mapping.html')
    except Exception as e:
        print(f"Error serving framework-mapping.html: {str(e)}")
        return f"Error: {str(e)}", 500

@app.route('/template-editor')
def serve_template_editor():
    try:
        return send_from_directory(app.static_folder, 'template_editor.html')
    except Exception as e:
        print(f"Error serving template_editor.html: {str(e)}")
        return f"Error: {str(e)}", 500

@app.route('/generate', methods=['POST'])
def generate_policy_endpoint():
    try:
        config_data = request.json
        output_format = request.args.get('format', 'md').lower()
        print(f"\n=== Starting Generate Request ===")
        print(f"Config data: {config_data}")
        print(f"Output format: {output_format}")
        
        # Check if this is a framework-only mapping request
        if 'selected_frameworks' in config_data and 'policy_standard' not in config_data:
            try:
                print("\n=== Framework Mapping Flow ===")
                
                # Create framework mapper instead of policy generator
                mapper = FrameworkMapper()
                print("FrameworkMapper initialized successfully")
                
                converter = DocumentConverter()
                print("DocumentConverter initialized successfully")
                
                # Generate markdown content
                print(f"\nGenerating mapping for frameworks: {config_data['selected_frameworks']}")
                markdown_content = mapper.generate_mapping(
                    selected_frameworks=config_data['selected_frameworks']
                )
                print("Markdown content generated successfully")
                
                if output_format == 'docx':
                    print("\n=== DOCX Conversion Flow ===")
                    # Create temporary markdown file
                    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_md:
                        temp_md.write(markdown_content)
                        temp_md_path = Path(temp_md.name)
                        print(f"Temporary markdown file created: {temp_md_path}")
                    
                    # Convert to DOCX using existing converter
                    docx_path = converter.markdown_to_docx(temp_md_path)
                    print(f"DOCX file generated: {docx_path}")
                    
                    # Read the generated DOCX
                    with open(docx_path, 'rb') as f:
                        docx_content = f.read()
                    print("DOCX content read successfully")
                    
                    # Clean up temporary files
                    temp_md_path.unlink()
                    docx_path.unlink()
                    print("Temporary files cleaned up")
                    
                    return jsonify({
                        "success": True,
                        "content": base64.b64encode(docx_content).decode(),
                        "format": "docx",
                        "filename": f"framework_mapping_{datetime.now().strftime('%Y%m%d')}.docx"
                    })
                else:
                    print("\nReturning markdown content")
                    return jsonify({
                        "success": True,
                        "content": markdown_content,
                        "format": "md"
                    })
            except Exception as e:
                print(f"\n=== Error in Framework Mapping ===")
                print(f"Error type: {type(e)}")
                print(f"Error message: {str(e)}")
                print(f"Error location: {e.__traceback__.tb_frame.f_code.co_filename}:{e.__traceback__.tb_lineno}")
                return jsonify({"error": str(e)})
        
        # Handle regular policy generation
        if output_format not in ['md', 'docx']:
            return jsonify({"error": "Invalid format. Use 'md' or 'docx'"})
        
        result = generate_policy_from_web_config(config_data, output_format)
        return jsonify(result)
    except Exception as e:
        print(f"\n=== Error in Generate Endpoint ===")
        print(f"Error type: {type(e)}")
        print(f"Error message: {str(e)}")
        print(f"Error location: {e.__traceback__.tb_frame.f_code.co_filename}:{e.__traceback__.tb_lineno}")
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
    return jsonify({
        'baseUrl': os.getenv('BASE_URL', 'http://localhost:5000')
    })

# Serve OpenAPI specification
@app.route('/static/openapi.yaml')
def serve_swagger_spec():
    return send_from_directory(BACKEND_DIR, 'openapi.yaml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)