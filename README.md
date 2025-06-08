# MyVision Guide Generator

*Professional CLI tool for creating assistive technology learning guides using AI*

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview

MyVision Guide Generator is a command-line tool that leverages Anthropic Claude AI to instantly create professional learning guides for assistive technology topics. Designed specifically for MyVision Oxfordshire and accessibility professionals, it transforms hours of manual documentation into seconds of automated generation.

### What It Does

- **🚀 Instant Guide Generation:** Type a topic, get a professional learning guide in 30 seconds
- **📝 Two Input Methods:** Quick topic-based guides or personalized guides from training session transcripts
- **📄 Professional Output:** Word documents with MyVision branding or markdown for technical users
- **🎯 Accessibility Focus:** Specialized for screen readers, magnification, voice control, and assistive technologies
- **🔄 Organized Workflow:** Automatically saves guides to organized desktop folders with timestamps

### Example Usage

```bash
# Generate a VoiceOver guide
myvision guide "VoiceOver rotor navigation basics"

# Create JAWS setup instructions  
myvision guide "Setting up JAWS on Windows" --format docx

# Quick shortcuts for common topics
myvision voiceover-basics
myvision jaws-setup

# Test accessibility features with logo
myvision accessibility-test --format docx

# List recent guides
myvision list
```

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Guide](#usage-guide)
- [Configuration](#configuration)
- [Guide Examples](#guide-examples)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

### 🤖 AI-Powered Content Generation
- **Expert Knowledge:** Claude AI trained on assistive technology concepts
- **MyVision Methodology:** Incorporates empathetic, step-by-step teaching approach
- **Structured Output:** Consistent guide format with learning objectives, prerequisites, instructions, practice activities, troubleshooting, and next steps
- **Professional Branding:** Automatic MyVision logo and organizational branding in all documents

### 📋 Multiple Input Methods
- **Topic-Based Generation:** Create guides from simple topic strings
- **Session Analysis:** Generate personalized guides from training session transcripts (planned feature)
- **Quick Shortcuts:** Pre-defined commands for common assistive technology topics

### 📄 Professional Output Formats
- **Microsoft Word (.docx):** Professionally formatted documents with MyVision branding and logo
- **Markdown (.md):** Lightweight format for version control and technical users
- **Automatic Organization:** Guides saved to organized desktop folders with timestamps

### 🎯 Assistive Technology Specialization
- **Screen Readers:** VoiceOver, JAWS, NVDA, TalkBack
- **Magnification Tools:** ZoomText, built-in OS magnification
- **Voice Control:** Dragon, built-in voice commands
- **Mobile Accessibility:** iPhone, iPad, Android accessibility features
- **Desktop Tools:** Windows, macOS accessibility settings

### Professional CLI Experience
- **Beautiful Terminal Output:** Colored text, progress bars, status indicators
- **Error Handling:** Graceful failures with helpful error messages
- **Input Validation:** Prevents common mistakes with clear guidance
- **Cross-Platform:** Works on macOS, Windows, and Linux
- **Accessibility Testing:** Built-in accessibility validation with `myvision accessibility-test`

## Installation

### Prerequisites

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **Anthropic API key** - [Get API key](https://console.anthropic.com/)
- **macOS, Windows, or Linux**

### Step 1: Clone or Download

```bash
# Option A: Clone with git
git clone https://github.com/myvision/guide-generator.git
cd guide-generator

# Option B: Download and extract ZIP file
# Then navigate to extracted folder
```

### Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies and Tool

```bash
# Install required packages
pip install -r requirements.txt

# Install the CLI tool
pip install -e .
```

### Step 4: Configure API Key

```bash
# Set your Anthropic API key
export ANTHROPIC_API_KEY="your-api-key-here"

# On Windows:
set ANTHROPIC_API_KEY=your-api-key-here

# Or create .env file in project root:
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env
```

### Step 5: Verify Installation

```bash
# Test the installation
myvision --help

# Generate your first guide
myvision guide "VoiceOver basics for beginners"
```

## Quick Start

### Your First Guide

```bash
# Generate a basic VoiceOver guide
myvision guide "VoiceOver navigation basics"
```

This creates a professional Word document on your desktop:
`~/Desktop/MyVision_Guides/Learning_Guides/voiceover_navigation_basics_learning_guide_20241215_143022.docx`

### Try Different Formats

```bash
# Generate as Markdown
myvision guide "iPhone accessibility overview" --format markdown

# Use quick shortcuts
myvision voiceover-basics --format docx
myvision jaws-setup --format markdown
```

### View Your Guides

```bash
# List recent guides
myvision list

# Show more guides
myvision list --limit 20
```

## Usage Guide

### Basic Command Structure

```bash
myvision [COMMAND] [OPTIONS] [ARGUMENTS]
```

### Commands

#### `guide` - Generate Topic-Based Guides

```bash
myvision guide "TOPIC" [--format FORMAT]
```

**Examples:**
```bash
# Basic usage
myvision guide "VoiceOver rotor basics"

# Specific format
myvision guide "JAWS virtual cursor navigation" --format docx
myvision guide "Android TalkBack gestures" --format markdown

# Complex topics
myvision guide "Setting up screen magnification for low vision users"
myvision guide "Voice control setup for motor impairments"
```

#### `list` - View Recent Guides

```bash
myvision list [--limit NUMBER]
```

**Examples:**
```bash
myvision list                # Show 10 most recent
myvision list --limit 5      # Show 5 most recent  
myvision list --limit 50     # Show 50 most recent
```

#### Quick Shortcuts

```bash
myvision voiceover-basics [--format FORMAT]    # VoiceOver basics guide
myvision jaws-setup [--format FORMAT]          # JAWS setup guide
```

#### Accessibility Testing

```bash
myvision accessibility-test [--format FORMAT]  # Generate comprehensive accessibility test document
```

### Options

- `--format [markdown|docx]` - Output format (default: docx)
- `--help` - Show command help
- `--version` - Show version information

### Output Organization

```
Desktop/MyVision_Guides/
├── Learning_Guides/          # Topic-based guides
│   ├── voiceover_basics_learning_guide_20241215_143022.docx
│   ├── jaws_setup_learning_guide_20241215_144033.md
│   └── ...
└── Session_Guides/           # Session-based guides (future)
    └── ...
```

## Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `ANTHROPIC_API_KEY` | Your Anthropic Claude API key | Yes | None |
| `MYVISION_OUTPUT_DIR` | Custom output directory | No | `~/Desktop/MyVision_Guides` |

### Configuration File

Create `.env` file in project root:

```env
# Required
ANTHROPIC_API_KEY=your_api_key_here

# Optional customization
MYVISION_OUTPUT_DIR=/custom/path/to/guides
MYVISION_ORG_NAME=Your Organization Name
MYVISION_CONTACT_EMAIL=your-email@example.com
```

### Customizing Output

The tool creates guides with MyVision Oxfordshire branding by default. To customize:

1. **Organization Name:** Set `MYVISION_ORG_NAME` environment variable
2. **Contact Email:** Set `MYVISION_CONTACT_EMAIL` environment variable
3. **Output Directory:** Set `MYVISION_OUTPUT_DIR` environment variable
4. **Logo Integration:** Place your logo as `assets/myvision_Logo.png` in the project root

### Logo Requirements

For optimal results with logo integration:
- **Supported formats:** PNG, JPEG, GIF (PNG recommended)
- **Recommended size:** 300x100 pixels for professional appearance
- **Aspect ratio:** Maintain original proportions for best results
- **File location:** `assets/myvision_Logo.png` in project root directory

## Guide Examples

### Generated Guide Structure

Every guide follows this professional structure:

```markdown
# Topic Name - Learning Guide

## Learning Objectives
- Clear, measurable learning outcomes
- Skills the user will gain

## Prerequisites  
- What users should know beforehand
- Required software or hardware setup

## Step-by-Step Instructions
1. Detailed, numbered steps
2. Specific commands and gestures
3. Clear explanations of why each step matters

## Practice Activities
- Hands-on exercises to reinforce learning
- Real-world scenarios to try

## Troubleshooting
- Common issues and solutions
- When to ask for help

## Next Steps
- Building on this foundation
- Related topics to explore
```

### Sample Topics That Work Well

**Screen Reader Guides:**
- "VoiceOver rotor navigation on iPhone"
- "JAWS reading modes in Microsoft Word"
- "NVDA browse mode vs focus mode"
- "TalkBack gesture shortcuts for Android"

**Magnification Guides:**
- "Setting up ZoomText for daily use"
- "macOS zoom features for low vision"
- "Windows Magnifier keyboard shortcuts"

**Voice Control Guides:**
- "Dragon NaturallySpeaking basic commands"
- "macOS Voice Control setup and training"
- "Windows Speech Recognition for document editing"

**Mobile Accessibility:**
- "iPhone accessibility settings overview"
- "Android accessibility feature setup"
- "Voice assistant setup for blind users"

### Generated Content Quality

- **Expert-Level Knowledge:** Accurate information about assistive technologies
- **Empathetic Tone:** Encouraging and supportive language
- **Practical Focus:** Real-world applications and examples
- **Safety Considerations:** Warnings about common pitfalls
- **MyVision Values:** Reflects organizational teaching philosophy

## Development

### Project Structure

```
myvision-guide-generator/
├── src/myvision_guides/          # Main package
│   ├── __init__.py               # Package initialization
│   ├── cli.py                    # Command-line interface
│   ├── config.py                 # Configuration management
│   ├── guide_generator.py        # AI integration
│   └── file_manager.py           # File operations
├── templates/                    # Word document templates
├── tests/                        # Test suite
├── requirements.txt              # Python dependencies
├── setup.py                      # Package installation
├── .env.example                  # Environment template
└── README.md                     # This file
```

### Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/myvision/guide-generator.git
cd guide-generator

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Set up pre-commit hooks (optional)
pip install pre-commit
pre-commit install
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=myvision_guides

# Run specific test file
python -m pytest tests/test_guide_generator.py
```

### Code Style

This project uses:
- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Check linting
flake8 src/ tests/

# Type checking
mypy src/
```

### Adding New Features

1. **Create feature branch:** `git checkout -b feature/new-feature`
2. **Write tests first:** Add tests in `tests/` directory
3. **Implement feature:** Add code in appropriate module
4. **Test thoroughly:** Ensure all tests pass
5. **Update documentation:** Add to README and docstrings
6. **Submit pull request:** Include description and test results

## Troubleshooting

### Common Issues

#### Command Not Found

```bash
myvision --help
# bash: myvision: command not found
```

**Solutions:**
1. Ensure virtual environment is activated: `source venv/bin/activate`
2. Reinstall package: `pip install -e .`
3. Check PATH includes Python scripts directory

#### Import Errors

```bash
myvision --help
# ModuleNotFoundError: No module named 'config'
```

**Solutions:**
1. Ensure you're using relative imports (`from .config import config`)
2. Verify `__init__.py` files exist in all package directories
3. Reinstall package: `pip uninstall myvision-guides && pip install -e .`

#### API Key Issues

```bash
myvision guide "test"
# Error: ANTHROPIC_API_KEY not found
```

**Solutions:**
1. Set environment variable: `export ANTHROPIC_API_KEY="your-key"`
2. Create `.env` file with API key
3. Verify key is valid at [Anthropic Console](https://console.anthropic.com/)

#### File Permission Errors

```bash
# PermissionError: [Errno 13] Permission denied
```

**Solutions:**
1. Check desktop write permissions
2. Try custom output directory: `export MYVISION_OUTPUT_DIR=/tmp/guides`
3. Run with appropriate user permissions

#### Generation Failures

```bash
# Error generating guide: Connection timeout
```

**Solutions:**
1. Check internet connection
2. Verify API key has sufficient credits
3. Try with shorter, simpler topic
4. Check Anthropic service status

### Getting Help

1. **Check documentation:** Review this README and command help (`myvision --help`)
2. **Search issues:** Look for similar problems in project issues
3. **Create issue:** Provide error messages, steps to reproduce, and system info
4. **Contact support:** Email technical support with detailed information

### Debug Mode

Enable verbose output for troubleshooting:

```bash
# Set debug environment variable
export MYVISION_DEBUG=1

# Run command with debug info
myvision guide "test topic"
```

## Contributing

We welcome contributions from the community! Whether you're fixing bugs, adding features, or improving documentation, your help makes this tool better for everyone.

### How to Contribute

1. **Fork the repository** on GitHub
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes** with appropriate tests
4. **Commit your changes** (`git commit -m 'Add amazing feature'`)
5. **Push to the branch** (`git push origin feature/amazing-feature`)
6. **Open a Pull Request** with detailed description

### Contribution Guidelines

- **Follow code style:** Use Black, isort, and flake8
- **Write tests:** All new features need test coverage
- **Update documentation:** Include docstrings and README updates
- **Keep commits focused:** One feature/fix per commit
- **Test thoroughly:** Ensure all tests pass on your system

### Areas for Contribution

- **New output formats:** PDF, HTML, or other formats
- **Additional shortcuts:** More predefined topic guides
- **Template system:** Custom Word document templates
- **Session analysis:** Implement transcription-based guide generation
- **Internationalization:** Support for multiple languages
- **Cloud integration:** Save to Google Drive, OneDrive, etc.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**MyVision Oxfordshire**
- Website: [www.myvision.org](https://www.myvision.org)
- Email: info@myvision.org
- Support: technical-support@myvision.org

## Acknowledgments

- **Anthropic** for Claude AI technology
- **Click** for excellent CLI framework
- **Rich** for beautiful terminal output
- **python-docx** for Word document generation
- **MyVision Oxfordshire** team and clients for inspiration and feedback

---

*Built with ❤️ for the assistive technology community*