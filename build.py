#!/usr/bin/env python3
"""
Vial GUI Build Script
Replaces fbs functionality for building standalone executables with PyInstaller.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def build_executable():
    """Build standalone executable using PyInstaller"""
    
    # Get project root directory
    project_root = Path(__file__).parent
    main_script = project_root / 'src' / 'main' / 'python' / 'main.py'
    
    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        '--name', 'Vial',
        '--icon', 'src/main/icons/Icon.ico' if os.path.exists('src/main/icons/Icon.ico') else '',
        '--add-data', 'src/main/resources:resources',
        '--hidden-import', 'PyQt6.QtCore',
        '--hidden-import', 'PyQt6.QtGui', 
        '--hidden-import', 'PyQt6.QtWidgets',
        '--hidden-import', 'hidapi',
        '--hidden-import', 'keyboard',
        '--hidden-import', 'certifi',
        str(main_script)
    ]
    
    # Remove empty icon parameter if no icon exists
    cmd = [arg for arg in cmd if arg]
    
    print("Building Vial executable...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, cwd=project_root)
        print("Build completed successfully!")
        print(f"Executable created in: {project_root / 'dist' / 'Vial'}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error: {e}")
        return False
    except FileNotFoundError:
        print("PyInstaller not found. Please install it with: pip install pyinstaller")
        return False

def clean_build():
    """Clean build artifacts"""
    project_root = Path(__file__).parent
    
    # Directories to clean
    clean_dirs = ['build', 'dist', '__pycache__']
    
    for dir_name in clean_dirs:
        dir_path = project_root / dir_name
        if dir_path.exists():
            print(f"Removing {dir_path}")
            shutil.rmtree(dir_path)
    
    # Remove .spec files
    for spec_file in project_root.glob('*.spec'):
        print(f"Removing {spec_file}")
        spec_file.unlink()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'clean':
        clean_build()
    else:
        build_executable()