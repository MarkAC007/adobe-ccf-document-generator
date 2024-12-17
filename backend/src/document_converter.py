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