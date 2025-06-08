# Step 3: Creating Your First Files Complete Beginner Guide
*Building the Foundation Files for Your AI CLI Tool - Zero Experience Required*

## 🎯 What You'll Accomplish in Step 3

By the end of this guide, you will have:
- ✅ Created all essential foundation files for your project
- ✅ Set up secure configuration management for your AI API key
- ✅ Established proper Python package structure
- ✅ Installed all required dependencies successfully
- ✅ Tested that all components can import and connect properly

**Time Investment:** 15-20 minutes of careful file creation
**Next Step Preview:** Building the AI logic that powers your tool

## 🔍 Pre-flight Check

Before starting, verify you have:
- ✅ Completed Step 2 (Development Environment Setup)
- ✅ Virtual environment activated (you see `(venv)` in your Terminal prompt)
- ✅ VS Code installed and working
- ✅ Located in your project directory

**To verify you're ready:**
```bash
# Check you're in the right place with venv activated
pwd
# Should show: /Users/[username]/projects/myvision-guide-generator

# Verify virtual environment is active
echo $VIRTUAL_ENV
# Should show: /Users/[username]/projects/myvision-guide-generator/venv
```

**If either check fails:** Go back to Step 2 and complete the environment setup first.

## 🤔 Why File Structure Matters

### The Foundation Files Analogy

Think of these files like **building a house foundation:**

**Bad Foundation (Random Files):**
```
mycode.py           ← Everything mixed together
stuff.txt           ← No organization  
random_config       ← Hard to find anything
notes.doc           ← Impossible to maintain
```

**Professional Foundation (Organized Structure):**
```
myvision-guide-generator/
├── requirements.txt        ← "Shopping list" of needed tools
├── .env                   ← Secure settings (API keys)
├── .env.example           ← Template for other users
├── src/                   ← All your code lives here
│   └── myvision_guides/   ← Your main Python package
│       ├── __init__.py    ← Makes it a proper package
│       └── config.py      ← Manages all settings
└── venv/                  ← Virtual environment (already created)
```

**Benefits of Good Structure:**
- ✅ **Easy to find:** Everything has a logical place
- ✅ **Professional:** Industry-standard organization
- ✅ **Secure:** Sensitive data properly protected
- ✅ **Maintainable:** Easy to update and modify
- ✅ **Collaborative:** Others can understand your project

## 📚 Understanding Each File's Purpose

### File Creation Order (Important!)

We'll create files in dependency order to avoid import errors:

```
1. requirements.txt     → Defines what libraries we need
2. .env.example        → Template for secure configuration  
3. .env                → Your actual secure settings
4. src/ directory      → Code organization
5. __init__.py         → Makes Python package
6. config.py           → Settings management system
```

### File Dependencies Explained

```
requirements.txt  →  pip install  →  Libraries Available
        ↓
.env files  →  Environment Variables  →  Secure Configuration
        ↓
Python Package Structure  →  Organized Code  →  Importable Modules
        ↓
config.py  →  Settings Management  →  Ready for AI Integration
```

## 🛠️ Step-by-Step File Creation Process

### Step 1: Create requirements.txt (Your Dependency Shopping List)

**What this file does:**
- Lists all external Python libraries your project needs
- Specifies version numbers for consistency
- Enables one-command installation of everything

**Create the file:**
```bash
# Make sure you're in project root with venv activated
cd ~/projects/myvision-guide-generator

# Create requirements.txt
touch requirements.txt
```

**Open in VS Code and add this content:**
```bash
# Open the file in VS Code
code requirements.txt
```

**Copy and paste this exactly:**
```txt
# MyVision Guide Generator Dependencies
# AI Integration
anthropic>=0.18.0

# Command Line Interface  
click>=8.1.0

# Beautiful Terminal Output
rich>=13.0.0

# Word Document Creation
python-docx>=0.8.11

# Environment Variable Management
python-dotenv>=1.0.0

# Enhanced Date/Time Handling
python-dateutil>=2.8.2
```

**Save the file** (`Cmd+S`)

**Understanding Each Dependency:**
- `anthropic`: Official library for Claude AI
- `click`: Professional command-line interface framework
- `rich`: Beautiful, colorful terminal output
- `python-docx`: Creates Microsoft Word documents
- `python-dotenv`: Loads settings from .env files
- `python-dateutil`: Better date/time handling

### Step 2: Install Dependencies

**Install everything at once:**
```bash
# This reads requirements.txt and installs all listed packages
pip3 install -r requirements.txt
```

**Expected output:**
```
Collecting anthropic>=0.18.0
  Downloading anthropic-0.18.1-py3-none-any.whl
Collecting click>=8.1.0
  Downloading click-8.1.3-py3-none-any.whl
[... more download messages ...]
Successfully installed anthropic-0.18.1 click-8.1.3 rich-13.4.2 python-docx-0.8.11 python-dotenv-1.0.0 python-dateutil-2.8.2
```

**If you see errors:** Don't panic! Common solutions:
```bash
# If you see "Permission denied":
# Make sure venv is activated (you should see (venv) in prompt)

# If you see "No module named pip":
python3 -m ensurepip --default-pip

# Try installation again:
pip3 install -r requirements.txt
```

### Step 3: Create Secure Configuration Files

**Why we need these files:**
Your Claude AI API key is like a password - it needs to be kept secret but accessible to your code.

**Create .env.example (Template for Others):**
```bash
# Create the template file
touch .env.example
```

**Open and add content:**
```bash
code .env.example
```

**Copy and paste:**
```bash
# MyVision Guide Generator Configuration Template
# Copy this file to .env and fill in your actual values

# Claude AI API Key (get from console.anthropic.com)
ANTHROPIC_API_KEY=your_api_key_here

# Organization Settings
MYVISION_ORG_NAME=MyVision Oxfordshire
MYVISION_CONTACT_EMAIL=info@myvision.org.uk
MYVISION_WEBSITE=www.myvision.org.uk

# Document Formatting (18pt minimum for large print accessibility)
MYVISION_BODY_FONT_SIZE=18
MYVISION_H1_FONT_SIZE=24
MYVISION_H2_FONT_SIZE=22
MYVISION_H3_FONT_SIZE=20
```

**Create .env (Your Actual Settings):**
```bash
# Copy the template to create your actual config
cp .env.example .env
```

**Edit your .env file:**
```bash
code .env
```

**For now, keep it as the template** (we'll add your real API key in Step 4):
```bash
# MyVision Guide Generator Configuration
# Copy this file to .env and fill in your actual values

# Claude AI API Key (get from console.anthropic.com)
ANTHROPIC_API_KEY=your_api_key_here

# Organization Settings  
MYVISION_ORG_NAME=MyVision Oxfordshire
MYVISION_CONTACT_EMAIL=info@myvision.org.uk
MYVISION_WEBSITE=www.myvision.org.uk

# Document Formatting (18pt minimum for large print accessibility)
MYVISION_BODY_FONT_SIZE=18
MYVISION_H1_FONT_SIZE=24
MYVISION_H2_FONT_SIZE=22
MYVISION_H3_FONT_SIZE=20
```

**Security Note:** Never commit .env to version control! It contains secrets.

### Step 4: Create Python Package Structure

**Create the source directory:**
```bash
# Create src directory for all your code
mkdir src

# Create your main package directory
mkdir src/myvision_guides
```

**Create __init__.py (Makes it a Python Package):**
```bash
# Create the package initialization file
touch src/myvision_guides/__init__.py
```

**Open and add content:**
```bash
code src/myvision_guides/__init__.py
```

**Add this simple package definition:**
```python
"""
MyVision Guide Generator

A CLI tool for creating assistive technology learning guides using AI.
"""

__version__ = "1.0.0"
__author__ = "MyVision Oxfordshire" 
__email__ = "info@myvision.org"
```

**Save the file** (`Cmd+S`)

### Step 5: Create config.py (Settings Management)

**Create the file:**
```bash
touch src/myvision_guides/config.py
code src/myvision_guides/config.py
```

**Add this complete configuration system:**
```python
"""Configuration management for MyVision Guide Generator"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ConfigurationError(Exception):
    """Raised when configuration is invalid or missing"""
    pass

class Config:
    """Manages all application settings and configuration."""
    
    def __init__(self):
        # API Configuration
        self.anthropic_api_key = self._get_required_env("ANTHROPIC_API_KEY")
        self.default_model = os.getenv("MYVISION_MODEL", "claude-3-sonnet-20241022")
        self.max_tokens = int(os.getenv("MYVISION_MAX_TOKENS", "3000"))
        
        # File Paths
        self.desktop_path = Path.home() / "Desktop"
        output_dir = os.getenv("MYVISION_OUTPUT_DIR")
        if output_dir:
            self.output_directory = Path(output_dir)
        else:
            self.output_directory = self.desktop_path / "MyVision_Guides"
        
        # Organization Branding
        self.organization_name = os.getenv("MYVISION_ORG_NAME", "MyVision Oxfordshire")
        self.contact_email = os.getenv("MYVISION_CONTACT_EMAIL", "info@myvision.org")
        
    def _get_required_env(self, key: str) -> str:
        """Get required environment variable or raise helpful error."""
        value = os.getenv(key)
        if not value:
            raise ConfigurationError(
                f"Required setting '{key}' is not configured.\n"
                f"Please add it to your .env file: {key}=your_value_here"
            )
        return value
    
    def ensure_output_directory(self):
        """Create output directory structure if it doesn't exist."""
        try:
            self.output_directory.mkdir(parents=True, exist_ok=True)
            (self.output_directory / "Learning_Guides").mkdir(exist_ok=True)
            (self.output_directory / "Session_Guides").mkdir(exist_ok=True)
        except PermissionError:
            raise ConfigurationError(f"Permission denied: {self.output_directory}")

# Create global configuration instance
config = Config()
```

## ✅ Validation and Testing

### Test Your Package Structure

**Check file structure:**
```bash
find . -name "*.py" -o -name "*.txt" -o -name ".env*" | head -10
```

**Test package import:**
```bash
PYTHONPATH=src python3 -c "
import myvision_guides
print('✅ Package imported successfully')
print('Version:', myvision_guides.__version__)
"
```

**Test configuration:**
```bash
PYTHONPATH=src python3 -c "
from myvision_guides.config import config
print('✅ Config loaded')
print('Organization:', config.organization_name)
config.ensure_output_directory()
print('✅ Directories created')
"
```

## 🎉 Achievement Summary

You've successfully created:
- ✅ Professional Python package structure
- ✅ Secure configuration management
- ✅ Dependency management with requirements.txt
- ✅ Environment variable handling
- ✅ Organized output directories

**Next:** Step 4 - Building AI Logic with Claude API integration

**Version Constraint Options:**
```txt
# Exact version (risky - breaks with any update)
anthropic==0.18.0

# Minimum version (recommended - allows updates)
anthropic>=0.18.0

# Compatible release (allows patch updates only)
anthropic~=0.18.0     # Equivalent to >=0.18.0, <0.19.0

# Version range (maximum control)
anthropic>=0.18.0,<1.0.0

# Exclude problematic versions
anthropic>=0.18.0,!=0.19.5

# Pre-release inclusion
anthropic>=0.18.0,<1.0.0a0
```

**Best Practices for Version Constraints:**
```txt
# Production applications (strict compatibility)
anthropic>=0.18.0,<0.19.0
click>=8.1.0,<9.0.0

# Development tools (allow minor updates)
black>=22.0.0
pytest>=7.0.0

# Stable libraries (allow broader ranges)
python-dateutil>=2.8.0
```

### Advanced Requirements.txt Features

**Conditional Dependencies:**
```txt
# Platform-specific packages
pywin32>=227; sys_platform == "win32"
pyobjc-framework-Cocoa>=8.0; sys_platform == "darwin"

# Python version specific
importlib-metadata>=1.0; python_version < "3.8"
typing-extensions>=3.7.4; python_version < "3.8"

# Optional feature groups
anthropic[aws]>=0.18.0  # Include AWS-specific dependencies
```

**Development vs Production Requirements:**
```
requirements.txt         # Production dependencies
requirements-dev.txt     # Development tools
requirements-test.txt    # Testing frameworks
requirements-docs.txt    # Documentation generation
```

**Example requirements-dev.txt:**
```txt
# Testing
pytest>=7.0.0
pytest-cov>=4.0.0
pytest-mock>=3.10.0

# Code Quality
black>=22.0.0
isort>=5.11.0
flake8>=5.0.0
mypy>=1.0.0

# Development Tools
ipython>=8.0.0
pre-commit>=2.20.0
```

### Dependency Installation Process

**Basic Installation:**
```bash
# Install all requirements
pip install -r requirements.txt

# Install with development dependencies
pip install -r requirements.txt -r requirements-dev.txt

# Upgrade all packages
pip install -r requirements.txt --upgrade

# Install without cache (clean install)
pip install -r requirements.txt --no-cache-dir
```

**Verification Commands:**
```bash
# List installed packages
pip list

# Show specific package info
pip show anthropic

# Check for security vulnerabilities
pip audit

# Generate requirements from current environment
pip freeze > requirements-frozen.txt
```

## Environment Variable Management

### .env File Structure and Security

**Why .env Files Are Essential:**
- **Security:** API keys never appear in code or git history
- **Flexibility:** Different configurations for different environments
- **Team collaboration:** Each developer uses their own keys
- **Deployment:** Easy configuration changes without code modifications

### .env File Creation and Format

**Create .env File:**
```bash
# Create file with restricted permissions
touch .env
chmod 600 .env  # Only owner can read/write

# Add content (never commit this file)
cat > .env << 'EOF'
# MyVision Guide Generator Configuration
# Keep this file secure and never commit to version control

# === Required Configuration ===
ANTHROPIC_API_KEY=your_actual_api_key_here

# === Optional Customization ===
# Custom output directory (default: ~/Desktop/MyVision_Guides)
MYVISION_OUTPUT_DIR=/Users/yourname/Documents/MyVision_Guides

# Organization branding
MYVISION_ORG_NAME=MyVision Oxfordshire
MYVISION_CONTACT_EMAIL=info@myvision.org
MYVISION_WEBSITE=www.myvision.org

# === Development Settings ===
# Debug mode (true/false)
MYVISION_DEBUG=false

# Log level (DEBUG, INFO, WARNING, ERROR)
MYVISION_LOG_LEVEL=INFO

# Claude model selection
MYVISION_MODEL=claude-3-sonnet-20241022

# API settings
MYVISION_MAX_TOKENS=3000
MYVISION_TEMPERATURE=0.2
EOF
```

**Create .env.example Template:**
```bash
# Create template for other developers (safe to commit)
cat > .env.example << 'EOF'
# MyVision Guide Generator Configuration Template
# Copy this file to .env and fill in your actual values

# === Required Configuration ===
# Get your API key from: https://console.anthropic.com/
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# === Optional Customization ===
# Custom output directory (uncomment to use)
# MYVISION_OUTPUT_DIR=/path/to/your/preferred/output/directory

# Organization branding (uncomment to customize)
# MYVISION_ORG_NAME=Your Organization Name
# MYVISION_CONTACT_EMAIL=your-email@example.com
# MYVISION_WEBSITE=your-website.com

# === Development Settings ===
# Debug mode for development (uncomment to enable)
# MYVISION_DEBUG=true

# Log level for debugging (uncomment to change)
# MYVISION_LOG_LEVEL=DEBUG

# Claude model (uncomment to change default)
# MYVISION_MODEL=claude-3-sonnet-20241022

# API settings (uncomment to customize)
# MYVISION_MAX_TOKENS=3000
# MYVISION_TEMPERATURE=0.2
EOF
```

### Environment Variable Best Practices

**Naming Conventions:**
```bash
# Good naming (clear, consistent)
MYVISION_API_KEY=...
MYVISION_OUTPUT_DIR=...
MYVISION_DEBUG=...

# Poor naming (ambiguous, inconsistent)
API_KEY=...
DIR=...
DEBUG_MODE=...
```

**Value Formatting:**
```bash
# Strings (no quotes needed in .env)
MYVISION_ORG_NAME=MyVision Oxfordshire

# Paths (use absolute paths)
MYVISION_OUTPUT_DIR=/Users/jamie/Desktop/MyVision_Guides

# Booleans (use lowercase)
MYVISION_DEBUG=true
MYVISION_ENABLED=false

# Numbers (no quotes)
MYVISION_MAX_TOKENS=3000
MYVISION_TEMPERATURE=0.2

# Lists (comma-separated)
MYVISION_ALLOWED_FORMATS=markdown,docx,pdf
```

**Security Considerations:**
```bash
# File permissions (Unix/Mac)
chmod 600 .env        # Owner read/write only
chmod 644 .env.example # World readable (safe template)

# .gitignore entries (always include)
.env
.env.local
.env.*.local
*.env
```

## Python Package Structure (__init__.py)

### Understanding Python Packages

**What Makes a Directory a Package:**
```
Without __init__.py:
src/myvision_guides/
├── cli.py
└── config.py
# Just a directory with Python files

With __init__.py:
src/myvision_guides/
├── __init__.py      # ← Makes this a package
├── cli.py
└── config.py
# Now it's an importable Python package
```

**Package Import Behavior:**
```python
# Without __init__.py
import myvision_guides        # ImportError: No module named 'myvision_guides'

# With __init__.py
import myvision_guides        # Success!
from myvision_guides import cli  # Success!
```

### __init__.py Content Strategy

**Minimal __init__.py (Basic Package):**
```python
"""
MyVision Guide Generator

A CLI tool for creating assistive technology learning guides using AI.
"""

__version__ = "1.0.0"
__author__ = "MyVision Oxfordshire"
__email__ = "info@myvision.org"
```

**Comprehensive __init__.py (Full Featured):**
```python
"""
MyVision Guide Generator

A CLI tool for creating professional assistive technology learning guides
using Anthropic Claude AI.

This package provides:
- Quick topic-based guide generation
- Personalized guides from training session transcriptions  
- Professional Word document output with MyVision branding
- Organized file management and storage

Usage:
    from myvision_guides import GuideGenerator, FileManager
    
    generator = GuideGenerator()
    guide = await generator.generate_topic_guide("VoiceOver basics")
"""

# Package metadata
__version__ = "1.0.0"
__author__ = "MyVision Oxfordshire"
__email__ = "info@myvision.org"
__description__ = "CLI tool for generating assistive technology learning guides"
__url__ = "https://github.com/myvision/guide-generator"
__license__ = "MIT"

# Version information
__version_info__ = tuple(int(num) for num in __version__.split('.'))

# Import main classes for easy access
# Note: These imports will fail until the modules are created
try:
    from .guide_generator import GuideGenerator
    from .file_manager import FileManager
    from .config import config
    
    # Define what gets imported with "from myvision_guides import *"
    __all__ = [
        "GuideGenerator",
        "FileManager", 
        "config",
        "__version__",
        "__author__"
    ]
except ImportError:
    # During initial development, modules may not exist yet
    __all__ = [
        "__version__",
        "__author__"
    ]

# Package-level configuration
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
```

**Staged __init__.py Development:**
```python
# Stage 1: Minimal package (Step 3)
"""MyVision Guide Generator"""
__version__ = "1.0.0"

# Stage 2: Add config import (after creating config.py)
"""MyVision Guide Generator"""
__version__ = "1.0.0"
from .config import config

# Stage 3: Add all modules (after completing development)
"""MyVision Guide Generator"""
__version__ = "1.0.0"
from .config import config
from .guide_generator import GuideGenerator
from .file_manager import FileManager
from .cli import main
```

### Package Import Patterns

**Absolute vs Relative Imports:**
```python
# Absolute imports (from outside package)
from myvision_guides.config import config
from myvision_guides.guide_generator import GuideGenerator

# Relative imports (from inside package)
from .config import config              # Same level
from .guide_generator import GuideGenerator  # Same level
from ..utils import helper_function    # Parent package
```

**Import Organization in __init__.py:**
```python
# Standard library imports first
import os
import sys
import logging

# Third-party imports second  
import click
import rich

# Local package imports last
from .config import config
from .guide_generator import GuideGenerator
```

## Configuration Management (config.py)

### Configuration Architecture Design

**Single Configuration Class Pattern:**
```python
class Config:
    """
    Centralized configuration management for the entire application.
    
    This class uses the Singleton pattern to ensure consistent settings
    across all modules and provides validation and error handling.
    """
    
    _instance = None  # Singleton instance
    
    def __new__(cls):
        """Implement Singleton pattern"""
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
```

### Complete config.py Implementation

**Full Configuration Module:**
```python
"""
Configuration management for MyVision Guide Generator

This module handles:
- Environment variable loading and validation
- Default settings management
- File path configuration  
- API configuration
- Error handling and validation
"""

import os
import sys
from pathlib import Path
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ConfigurationError(Exception):
    """Raised when configuration is invalid or incomplete"""
    pass

class Config:
    """
    Centralized configuration management.
    
    This class manages all application settings including:
    - API keys and authentication
    - File paths and directory structure
    - Default values and preferences
    - Validation and error checking
    """
    
    _instance = None
    
    def __new__(cls):
        """Singleton pattern - only one Config instance exists"""
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Initialize configuration settings"""
        if self._initialized:
            return
        
        # API Configuration
        self._load_api_configuration()
        
        # File System Configuration
        self._load_file_configuration()
        
        # Application Settings
        self._load_application_settings()
        
        # MyVision Branding
        self._load_branding_configuration()
        
        # Mark as initialized
        self._initialized = True
    
    def _load_api_configuration(self):
        """Load API-related configuration"""
        # Anthropic API settings
        self.anthropic_api_key = self._get_required_env("ANTHROPIC_API_KEY")
        self.default_model = os.getenv("MYVISION_MODEL", "claude-3-sonnet-20241022")
        self.max_tokens = int(os.getenv("MYVISION_MAX_TOKENS", "3000"))
        self.temperature = float(os.getenv("MYVISION_TEMPERATURE", "0.2"))
        
        # API limits and timeouts
        self.api_timeout = int(os.getenv("MYVISION_API_TIMEOUT", "60"))
        self.max_retries = int(os.getenv("MYVISION_MAX_RETRIES", "3"))
    
    def _load_file_configuration(self):
        """Load file system configuration"""
        # Desktop and output paths
        self.desktop_path = Path.home() / "Desktop"
        
        # Custom output directory or default
        output_dir = os.getenv("MYVISION_OUTPUT_DIR")
        if output_dir:
            self.output_directory = Path(output_dir)
        else:
            self.output_directory = self.desktop_path / "MyVision_Guides"
        
        # Template directory (relative to package)
        self.template_directory = Path(__file__).parent.parent.parent / "templates"
        
        # Ensure paths are absolute
        self.output_directory = self.output_directory.resolve()
        self.template_directory = self.template_directory.resolve()
    
    def _load_application_settings(self):
        """Load application behavior settings"""
        # Default format and behavior
        self.default_format = os.getenv("MYVISION_DEFAULT_FORMAT", "docx")
        self.debug_mode = os.getenv("MYVISION_DEBUG", "false").lower() == "true"
        self.log_level = os.getenv("MYVISION_LOG_LEVEL", "INFO").upper()
        
        # Guide structure settings
        self.guide_sections = [
            "Learning Objectives",
            "Prerequisites", 
            "Step-by-Step Instructions",
            "Practice Activities",
            "Troubleshooting",
            "Next Steps"
        ]
        
        # File naming settings
        self.max_filename_length = int(os.getenv("MYVISION_MAX_FILENAME_LENGTH", "50"))
        self.timestamp_format = os.getenv("MYVISION_TIMESTAMP_FORMAT", "%Y%m%d_%H%M%S")
    
    def _load_branding_configuration(self):
        """Load MyVision branding settings"""
        self.organization_name = os.getenv("MYVISION_ORG_NAME", "MyVision Oxfordshire")
        self.contact_email = os.getenv("MYVISION_CONTACT_EMAIL", "info@myvision.org")
        self.website = os.getenv("MYVISION_WEBSITE", "www.myvision.org")
        
        # Document formatting
        self.document_author = self.organization_name
        self.document_title_size = 18  # Points
        self.document_org_size = 12    # Points
        self.document_date_size = 10   # Points
    
    def _get_required_env(self, key: str) -> str:
        """
        Get required environment variable or raise error.
        
        Args:
            key: Environment variable name
            
        Returns:
            Environment variable value
            
        Raises:
            ConfigurationError: If variable is not set
        """
        value = os.getenv(key)
        if not value:
            raise ConfigurationError(
                f"Required environment variable {key} is not set. "
                f"Please add it to your .env file or set it in your environment."
            )
        return value
    
    def ensure_output_directory(self):
        """
        Create output directory structure if it doesn't exist.
        
        Creates:
        - Main output directory
        - Learning_Guides subdirectory
        - Session_Guides subdirectory
        """
        try:
            # Create main directory
            self.output_directory.mkdir(parents=True, exist_ok=True)
            
            # Create subdirectories
            (self.output_directory / "Learning_Guides").mkdir(exist_ok=True)
            (self.output_directory / "Session_Guides").mkdir(exist_ok=True)
            
        except PermissionError:
            raise ConfigurationError(
                f"Permission denied creating output directory: {self.output_directory}. "
                f"Please check directory permissions or set MYVISION_OUTPUT_DIR to a writable location."
            )
        except Exception as e:
            raise ConfigurationError(
                f"Failed to create output directory: {e}"
            )
    
    def get_template_path(self, template_name: str) -> Path:
        """
        Get full path to a template file.
        
        Args:
            template_name: Name of template file
            
        Returns:
            Full path to template file
            
        Raises:
            ConfigurationError: If template doesn't exist
        """
        template_path = self.template_directory / template_name
        
        if not template_path.exists():
            raise ConfigurationError(
                f"Template file not found: {template_path}. "
                f"Please ensure templates are installed correctly."
            )
        
        return template_path
    
    def validate_configuration(self) -> tuple[bool, list[str]]:
        """
        Validate that all configuration is correct and accessible.
        
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Validate API key
        if not self.anthropic_api_key:
            errors.append("Anthropic API key not configured")
        elif len(self.anthropic_api_key) < 10:
            errors.append("Anthropic API key appears invalid (too short)")
        
        # Validate file paths
        if not self.desktop_path.exists():
            errors.append(f"Desktop path not accessible: {self.desktop_path}")
        
        # Test output directory creation
        try:
            self.ensure_output_directory()
        except ConfigurationError as e:
            errors.append(str(e))
        
        # Validate template directory
        if not self.template_directory.exists():
            errors.append(f"Template directory not found: {self.template_directory}")
        
        # Validate numeric settings
        if not (1 <= self.max_tokens <= 100000):
            errors.append(f"max_tokens ({self.max_tokens}) must be between 1 and 100000")
        
        if not (0.0 <= self.temperature <= 2.0):
            errors.append(f"temperature ({self.temperature}) must be between 0.0 and 2.0")
        
        return len(errors) == 0, errors
    
    def get_debug_info(self) -> Dict[str, Any]:
        """
        Get configuration information for debugging.
        
        Returns:
            Dictionary with configuration details (sensitive info redacted)
        """
        return {
            "api_key_configured": bool(self.anthropic_api_key),
            "api_key_length": len(self.anthropic_api_key) if self.anthropic_api_key else 0,
            "model": self.default_model,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "output_directory": str(self.output_directory),
            "template_directory": str(self.template_directory),
            "debug_mode": self.debug_mode,
            "organization": self.organization_name,
            "output_directory_exists": self.output_directory.exists(),
            "template_directory_exists": self.template_directory.exists(),
        }
    
    def __repr__(self) -> str:
        """String representation for debugging"""
        return f"Config(model={self.default_model}, debug={self.debug_mode})"

# Create global configuration instance
config = Config()

# Convenience function for validation
def validate_setup() -> tuple[bool, list[str]]:
    """
    Validate complete application setup.
    
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    return config.validate_configuration()
```

### Configuration Testing and Validation

**Create configuration test script:**
```python
# test_config.py
"""Test script for configuration validation"""

def test_config_creation():
    """Test that config can be created successfully"""
    try:
        from myvision_guides.config import config
        print("✅ Config created successfully")
        return True
    except Exception as e:
        print(f"❌ Config creation failed: {e}")
        return False

def test_environment_loading():
    """Test environment variable loading"""
    try:
        from myvision_guides.config import config
        
        # Test API key
        if config.anthropic_api_key:
            print(f"✅ API key loaded ({len(config.anthropic_api_key)} characters)")
        else:
            print("❌ API key not loaded")
            return False
        
        # Test other settings
        print(f"✅ Model: {config.default_model}")
        print(f"✅ Output directory: {config.output_directory}")
        print(f"✅ Organization: {config.organization_name}")
        
        return True
    except Exception as e:
        print(f"❌ Environment loading failed: {e}")
        return False

def test_validation():
    """Test configuration validation"""
    try:
        from myvision_guides.config import validate_setup
        
        is_valid, errors = validate_setup()
        
        if is_valid:
            print("✅ Configuration validation passed")
        else:
            print("❌ Configuration validation failed:")
            for error in errors:
                print(f"  - {error}")
        
        return is_valid
    except Exception as e:
        print(f"❌ Validation test failed: {e}")
        return False

def test_directory_creation():
    """Test output directory creation"""
    try:
        from myvision_guides.config import config
        
        config.ensure_output_directory()
        
        if config.output_directory.exists():
            print(f"✅ Output directory created: {config.output_directory}")
            
            # Check subdirectories
            learning_dir = config.output_directory / "Learning_Guides"
            session_dir = config.output_directory / "Session_Guides"
            
            if learning_dir.exists() and session_dir.exists():
                print("✅ Subdirectories created successfully")
                return True
            else:
                print("❌ Subdirectories not created")
                return False
        else:
            print("❌ Output directory not created")
            return False
    except Exception as e:
        print(f"❌ Directory creation failed: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Testing Configuration Setup\n")
    
    tests = [
        test_config_creation,
        test_environment_loading,
        test_validation,
        test_directory_creation
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
        print()
    
    passed = sum(results)
    total = len(results)
    
    print(f"📊 Configuration Tests: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 Configuration setup complete!")
    else:
        print("⚠️ Some configuration tests failed.")
```

## Integration Testing and Verification

### Complete File Structure Verification

**Directory structure check:**
```bash
# Verify complete structure
tree -a -I 'venv|__pycache__' myvision-guide-generator/
```

**Expected output:**
```
myvision-guide-generator/
├── .env                           # Secret configuration
├── .env.example                   # Configuration template
├── .gitignore                     # Git ignore rules
├── requirements.txt               # Dependencies
├── src/
│   └── myvision_guides/
│       ├── __init__.py           # Package marker
│       └── config.py             # Configuration management
└── venv/                         # Virtual environment
```

### Import Testing Sequence

**Test 1: Basic Package Import**
```bash
cd myvision-guide-generator
source venv/bin/activate
python3 -c "
import sys
print('Python executable:', sys.executable)
print('Python path:')
for path in sys.path[:3]:
    print(f'  {path}')
"
```

**Test 2: Package Recognition**
```bash
python3 -c "
import myvision_guides
print('Package location:', myvision_guides.__file__)
print('Package version:', getattr(myvision_guides, '__version__', 'Not set'))
"
```

**Test 3: Configuration Import**
```bash
python3 -c "
from myvision_guides.config import config
print('Config loaded successfully')
print('API key configured:', bool(config.anthropic_api_key))
print('Output directory:', config.output_directory)
"
```

**Test 4: Environment Variable Loading**
```bash
python3 -c "
import os
from dotenv import load_dotenv

print('Before load_dotenv:')
print('API key in env:', bool(os.getenv('ANTHROPIC_API_KEY')))

load_dotenv()

print('After load_dotenv:')
print('API key in env:', bool(os.getenv('ANTHROPIC_API_KEY')))
"
```

### Common Issues and Solutions

**Issue 1: Import Errors**
```python
# Error: ModuleNotFoundError: No module named 'myvision_guides'
```
**Diagnosis:**
```bash
# Check if __init__.py exists
ls -la src/myvision_guides/__init__.py

# Check Python path
python3 -c "import sys; print('\n'.join(sys.path))"
```
**Solution:**
```bash
# Ensure you're in the right directory
pwd  # Should show: .../myvision-guide-generator

# Ensure virtual environment is activated
which python  # Should show: .../venv/bin/python

# Add src to Python path temporarily
export PYTHONPATH="${PYTHONPATH}:${PWD}/src"
```

**Issue 2: Environment Variable Not Loading**
```python
# Error: ConfigurationError: Required environment variable ANTHROPIC_API_KEY is not set
```
**Diagnosis:**
```bash
# Check .env file exists and has content
ls -la .env
cat .env | head -5

# Check file permissions
ls -la .env  # Should show: -rw-------
```
**Solution:**
```bash
# Fix permissions
chmod 600 .env

# Verify content format
cat .env | grep ANTHROPIC_API_KEY
# Should show: ANTHROPIC_API_KEY=your_key_here (no spaces around =)
```

**Issue 3: Directory Creation Failures**
```python
# Error: PermissionError: [Errno 13] Permission denied: '/Users/jamie/Desktop/MyVision_Guides'
```
**Diagnosis:**
```bash
# Check desktop permissions
ls -la ~/Desktop/

# Check if directory already exists with wrong permissions
ls -la ~/Desktop/MyVision_Guides
```
**Solution:**
```bash
# Fix permissions
chmod 755 ~/Desktop/MyVision_Guides

# Or use custom directory
export MYVISION_OUTPUT_DIR="$HOME/Documents/MyVision_Guides"
```

## Best Practices Summary

### File Creation
1. **Create in correct order** - Dependencies before dependents
2. **Test after each file** - Verify imports work immediately
3. **Use consistent formatting** - Follow Python conventions
4. **Document thoroughly** - Include docstrings and comments
5. **Validate configuration** - Test environment variable loading

### Security
1. **Never commit .env** - Always use .gitignore
2. **Use restrictive permissions** - chmod 600 .env
3. **Provide .env.example** - Help other developers
4. **Validate API keys** - Check format and existence
5. **Handle missing config gracefully** - Provide helpful error messages

### Package Structure
1. **Always include __init__.py** - Makes directories importable
2. **Use semantic versioning** - Clear version numbering
3. **Document package purpose** - Clear docstrings
4. **Import safely** - Handle missing modules during development
5. **Follow conventions** - Standard Python package layout

### Configuration Management
1. **Centralize settings** - Single configuration class
2. **Use environment variables** - Flexible configuration
3. **Provide defaults** - Reasonable fallback values
4. **Validate early** - Check configuration at startup
5. **Support debugging** - Provide configuration introspection

---

*This foundation file guide establishes the essential structure for your CLI application. Proper setup of these files prevents common development issues and provides a solid base for building the remaining components.*