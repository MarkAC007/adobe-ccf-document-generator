import logging
import sys
from pathlib import Path

def setup_logging(log_path: Path):
    """Configure logging to both file and console"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path / 'debug.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
