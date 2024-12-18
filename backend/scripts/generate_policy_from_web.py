import json
import sys
import os
from pathlib import Path
import base64
import time

# Add the parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from src.templates import PolicyTemplate
from scripts.generate_policy_from_input import PolicyGenerator

app = Flask(__name__, 
           static_folder=str(Path(__file__).parent.parent),  # Set to backend directory
           static_url_path='')
CORS(app)

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
def serve_index():
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)