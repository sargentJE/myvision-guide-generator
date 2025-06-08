"""
MyVision Guide Generator Package

This package provides tools for generating professional assistive technology learning guides
using AI (specifically Anthropic's Claude). It's designed for trainers and educators at
MyVision Oxfordshire to create consistent, high-quality educational materials.

Package Structure:
- config.py: Central configuration management for API keys, paths, and settings
- guide_generator.py: Core AI interaction logic for content generation
- file_manager.py: File operations including filename generation and document formatting
- cli.py: Command-line interface that users interact with

Main Features:
- Generate learning guides from topic descriptions
- Save guides in both Markdown and Word document formats
- Professional formatting with MyVision branding
- Command-line interface for easy use
- Built-in file organization and naming conventions

Example Usage:
    From command line:
        myvision guide "VoiceOver basics for beginners"
        myvision guide "JAWS setup on Windows" --format markdown
    
    From Python code:
        from myvision_guides import GuideGenerator, FileManager
        generator = GuideGenerator()
        file_manager = FileManager()
        # Generate and save guides programmatically

Author: MyVision Oxfordshire
Version: 1.0.0
License: For internal use at MyVision Oxfordshire
"""

# SECTION Package Information
"""
Package version and metadata for the MyVision Guide Generator.
This information is used by setup.py and other tools to identify the package.
"""
__version__ = "1.0.0"
__author__ = "MyVision Oxfordshire"
__email__ = "info@myvision.org.uk"
__description__ = "AI-powered learning guide generator for assistive technology training"

# SECTION Public API Exports
"""
These are the main classes and functions that external code should use.
By importing them here, users can access them directly from the package:
    from myvision_guides import GuideGenerator, FileManager, config
Instead of:
    from myvision_guides.guide_generator import GuideGenerator
    from myvision_guides.file_manager import FileManager
    from myvision_guides.config import config
"""
from .guide_generator import GuideGenerator
from .file_manager import FileManager
from .config import config

# SECTION Public API Definition
"""
__all__ defines what gets imported when someone does "from myvision_guides import *"
This is considered best practice to explicitly control the public API.
"""
__all__ = [
    'GuideGenerator',    # Main AI interaction class
    'FileManager',       # File operations class
    'config',           # Configuration singleton
]