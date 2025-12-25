from pathlib import Path
from typing import Optional
import pypandoc

class DocumentConverter:
    def markdown_to_docx(self, source_path: Path, output_path: Optional[Path] = None) -> Path:
        """Convert markdown file to Word document using pandoc"""
        # Security: Validate source path
        source_path = Path(source_path).resolve()
        if not source_path.exists():
            raise FileNotFoundError(f"Source file not found: {source_path}")
        if not source_path.is_file():
            raise ValueError(f"Source path is not a file: {source_path}")
        if source_path.suffix.lower() not in ['.md', '.markdown']:
            raise ValueError(f"Source file must be a markdown file: {source_path}")

        if output_path is None:
            output_path = source_path.with_suffix('.docx')
        else:
            output_path = Path(output_path).resolve()

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