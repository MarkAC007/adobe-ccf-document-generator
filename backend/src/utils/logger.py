"""
Logger Utility Module
====================

Provides centralized logging configuration and utilities for the application.

Future Improvements:
- Add log rotation
- Implement structured logging
- Add log filtering capabilities
- Support multiple log destinations
- Add log analysis utilities
- Implement log compression
- Add log shipping to external systems

Architecture Notes:
- Could be split into:
    - LoggerFactory (creates loggers)
    - LogFormatter (formats log messages)
    - LogHandler (handles log output)
    - LogAnalyzer (analyzes log data)
- Add observer pattern for log events
- Implement chain of responsibility for log filtering
"""

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
