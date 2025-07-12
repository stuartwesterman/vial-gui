#!/usr/bin/env python3
"""
Vial GUI - Modern Python 3.13+ Entry Point
Replaces fbs functionality for running the application directly.
"""

import sys
import os

# Add the source directory to Python path
src_dir = os.path.join(os.path.dirname(__file__), 'src', 'main', 'python')
sys.path.insert(0, src_dir)

if __name__ == '__main__':
    from main import main
    main()