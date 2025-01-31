"""
Document Converter Module
========================

Handles conversion between different document formats, currently supporting Markdown to DOCX
conversion using pandoc.

Future Improvements:
- Add support for additional formats (PDF, HTML)
- Implement template-based styling for DOCX output
- Add configuration options for pandoc parameters
- Create format-specific converter classes
- Add document validation
- Implement caching for repeated conversions
- Add error recovery and retry mechanisms

Architecture Notes:
- Could be split into:
    - BaseConverter (abstract class)
    - MarkdownConverter
    - DocxConverter
    - PdfConverter
- Add factory pattern for converter creation
- Implement strategy pattern for different conversion options
"""

from pathlib import Path
from typing import Optional
import pypandoc

class DocumentConverter:
    def markdown_to_docx(self, source_path: Path, output_path: Optional[Path] = None) -> Path:
        """Convert markdown file to Word document using pandoc"""
        if output_path is None:
            output_path = source_path.with_suffix('.docx')
        
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convert markdown to docx using pandoc
        pypandoc.convert_file(
            str(source_path),
            'docx',
            outputfile=str(output_path),
            extra_args=[
                '--standalone',
                '--from', 'markdown-raw_html',
                '--wrap=none'
            ]
        )
        
        return output_path