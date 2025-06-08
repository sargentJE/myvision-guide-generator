# Step 2: Development Environment Setup Complete Beginner Guide
*Preparing Your Mac for Professional Python Development - Zero Experience Required*

## 🎯 What You'll Accomplish in Step 2

By the end of this guide, you will have:
- ✅ A professional Python development environment on your Mac
- ✅ All necessary tools installed and working correctly
- ✅ A clean, isolated workspace for your project
- ✅ Confidence using the Terminal (command line)
- ✅ A validated setup ready for building your AI tool

**Time Investment:** 20-30 minutes
**Next Step Preview:** Creating your first project files

## 🔍 Pre-flight Check

Before starting, verify you have:
- ✅ A Mac computer (any macOS version from 2019 onwards)
- ✅ Administrator access (can install software)
- ✅ Internet connection
- ✅ About 500MB of free disk space

**Don't worry if you've never:**
- Used Terminal or command line before
- Installed development tools
- Worked with virtual environments
- Set up programming environments

We'll guide you through every single step!

## 🤔 Why This Environment Setup Matters

### The Development Environment Analogy

Think of setting up a development environment like **preparing a professional kitchen before cooking:**

**Bad Kitchen Setup:**
```
Mixed utensils everywhere → Hard to find what you need
Old, inconsistent ingredients → Unreliable results  
No organization → Recipes fail randomly
Shared with others → Tools go missing
```

**Professional Kitchen Setup:**
```
Dedicated workspace → Everything has its place
Fresh, known ingredients → Consistent results
Organized workflow → Recipes work perfectly
Your own space → Nothing gets lost
```

**Your Development Environment Will Be:**
- **Isolated:** Your project won't interfere with system software
- **Clean:** Only the tools you need, nothing extra
- **Consistent:** Same setup works for all future projects
- **Professional:** Industry-standard tools and practices

### What We're Installing and Why

**1. Python 3.8+ (Programming Language)**
- **Purpose:** The language your tool is written in
- **Why this version:** Compatible with all the AI libraries we'll use
- **Installation:** From official Python.org for reliability

**2. Virtual Environment (Project Isolation)**
- **Purpose:** Keeps your project's dependencies separate
- **Why needed:** Prevents conflicts with other Python projects
- **Analogy:** Like having a separate toolbox for each project

**3. Text Editor with Python Support**
- **Purpose:** Where you'll view and edit your code
- **Why important:** Syntax highlighting makes code readable
- **Options:** We'll set up VS Code (beginner-friendly)

## 📚 Understanding Your Mac's Development Environment

### Current State Analysis - Let's See What You Have

**Step 1: Open Terminal (Don't Panic!)**

Terminal is just a way to type commands instead of clicking. Here's how to open it:

1. Press `Cmd + Space` (opens Spotlight search)
2. Type "Terminal" 
3. Press Enter
4. A black window opens - this is Terminal!

**What you'll see:**
```
jamiesargent@MacBook-Pro ~ %
```
This is your "prompt" - it's ready for commands.

**Step 2: Check Your Current Python Setup**

Copy and paste each command (one at a time) and press Enter:

```bash
# Check if Python 3 is available
python3 --version
```

**Possible Results:**
```
✅ GOOD: Python 3.11.2 (or any 3.8+)
❌ BAD: command not found: python3
❌ BAD: Python 2.7.x (too old)
```

```bash
# Check where Python is installed
which python3
```

**Possible Results:**
```
✅ GOOD: /usr/bin/python3 (system Python)
✅ GOOD: /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
❌ BAD: python3 not found
```

```bash
# Check if pip (package installer) is available
pip3 --version
```

**Possible Results:**
```
✅ GOOD: pip 23.0.1 (or any recent version)
❌ BAD: command not found: pip3
```

### Installation Plan Based on Your Results

**If all commands worked:** Great! Skip to Virtual Environment Setup
**If any failed:** Follow the installation steps below

## 🛠️ Step-by-Step Installation Process
**Solution:** Use virtual environments (never install with sudo!)

**Issue 3: Multiple Python Versions**
```bash
which python
which python3
# Different locations, potential conflicts
```
**Solution:** Always use `python3` explicitly, set up proper aliases

## Virtual Environment Deep Dive

### What Virtual Environments Actually Do

**File System Isolation:**
```
myvision-guide-generator/
└── venv/                              # Virtual environment folder
    ├── bin/                           # Executables
    │   ├── python3 -> Python executable
    │   ├── pip3 -> Package installer
    │   └── activate -> Environment activation script
    ├── lib/                           # Installed packages
    │   └── python3.x/
    │       └── site-packages/         # Your project dependencies
    └── include/                       # Header files
```

**Environment Variables When Activated:**
```bash
# Before activation
echo $PATH
# /usr/bin:/bin:/usr/sbin:/sbin

# After activation (source venv/bin/activate)
echo $PATH  
# /Users/you/project/venv/bin:/usr/bin:/bin:/usr/sbin:/sbin
#                           ↑ Your virtual environment comes first

echo $VIRTUAL_ENV
# /Users/you/project/venv

echo $PS1
# (venv) user@computer:~$    # Prompt shows active environment
```

### Virtual Environment Commands Explained

**Create Virtual Environment:**
```bash
python3 -m venv venv
```
**Breakdown:**
- `python3`: Use Python 3 interpreter
- `-m venv`: Run the venv module
- `venv`: Name of directory to create (convention)

**Activate Virtual Environment:**
```bash
source venv/bin/activate
```
**What this does:**
- Modifies PATH to prioritize venv/bin/
- Sets VIRTUAL_ENV environment variable
- Changes prompt to show (venv)
- Makes pip install to virtual environment

**Deactivate Virtual Environment:**
```bash
deactivate
```
**What this does:**
- Restores original PATH
- Removes VIRTUAL_ENV variable
- Restores original prompt
- Returns to system Python

### Virtual Environment Best Practices

**1. One Environment Per Project:**
```bash
# Good:
project_a/venv/
project_b/venv/
myvision/venv/

# Bad:
shared_venv/  # Used by multiple projects
```

**2. Consistent Naming:**
```bash
# Standard names (choose one):
venv/          # Most common
.venv/         # Hidden folder
env/           # Alternative
virtualenv/    # Explicit
```

**3. Environment in Project Root:**
```bash
myvision-guide-generator/
├── venv/                  # ✓ Virtual environment
├── src/                   # ✓ Source code
├── requirements.txt       # ✓ Dependencies
└── setup.py              # ✓ Installation config
```

**4. Never Commit venv/ to Git:**
```bash
# .gitignore file should contain:
venv/
.venv/
env/
*.pyc
__pycache__/
```

## Project Directory Structure Strategy

### Why Structure Matters

**Poor Structure (Common Beginner Mistake):**
```
my_project/
├── script1.py
├── script2.py
├── config_stuff.py
├── utils.py
├── test_something.py
├── requirements.txt
└── random_notes.txt
```
**Problems:** No clear organization, hard to find files, testing difficulties

**Professional Structure:**
```
myvision-guide-generator/           # Project root
├── src/                           # Source code
│   └── myvision_guides/           # Package
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       ├── guide_generator.py
│       └── file_manager.py
├── tests/                         # Test files
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_guide_generator.py
├── docs/                          # Documentation
│   ├── README.md
│   ├── installation.md
│   └── user_guide.md
├── templates/                     # Document templates
│   ├── myvision_template.docx
│   └── logo.png
├── venv/                          # Virtual environment
├── requirements.txt               # Dependencies
├── setup.py                       # Package installation
├── .env.example                   # Environment variables template
├── .gitignore                     # Git ignore rules
└── README.md                      # Main documentation
```

### Directory Purpose Explanation

**src/ Directory:**
- **Purpose:** Contains all source code
- **Benefit:** Clear separation between code and everything else
- **Import advantage:** Prevents relative import issues
- **Testing benefit:** Can test installed package vs development code

**tests/ Directory:**
- **Purpose:** All test files and test data
- **Convention:** Mirror src/ structure with test_ prefix
- **Integration:** Works with pytest and other testing frameworks
- **Coverage:** Easy to measure what's tested vs not tested

**docs/ Directory:**
- **Purpose:** All documentation files
- **Formats:** Markdown, reStructuredText, or Sphinx
- **Organization:** User guides, API docs, tutorials
- **Generation:** Can auto-generate from code comments

**templates/ Directory:**
- **Purpose:** Document templates, logos, static assets
- **Usage:** Word templates, image files, CSS stylesheets
- **Access:** Code reads templates to generate documents
- **Version control:** Track template changes over time

## Dependency Management Deep Dive

### Understanding requirements.txt

**Basic Format:**
```txt
# Core dependencies
anthropic>=0.18.0
click>=8.1.0
rich>=13.0.0

# Document generation
python-docx>=0.8.11

# Configuration
python-dotenv>=1.0.0

# Date handling
python-dateutil>=2.8.2
```

**Version Specifier Syntax:**
```txt
package==1.0.0     # Exact version (risky for compatibility)
package>=1.0.0     # Minimum version (recommended)
package~=1.0.0     # Compatible release (1.0.x but not 1.1.0)
package>=1.0,<2.0  # Version range
package!=1.5.0     # Exclude specific version
```

**Advanced Requirements Features:**
```txt
# Comments and organization
# === Core Dependencies ===
anthropic>=0.18.0          # AI model integration
click>=8.1.0               # CLI framework

# === Development Dependencies ===
pytest>=7.0.0              # Testing framework
black>=22.0.0              # Code formatting

# === Conditional Dependencies ===
pywin32>=227; sys_platform == "win32"    # Windows only
```

### Dependency Resolution Process

**Installation Order Matters:**
```bash
pip install -r requirements.txt
```

**What pip does:**
1. **Read requirements.txt:** Parse all package specifications
2. **Resolve dependencies:** Find compatible versions of all packages and their dependencies
3. **Download packages:** Get wheel files or source code
4. **Install in dependency order:** Install prerequisites first
5. **Verify installation:** Check that all imports work

**Common Dependency Conflicts:**
```
Package A requires numpy>=1.20.0
Package B requires numpy<1.19.0
Result: Impossible to satisfy both requirements
```

**Resolution Strategies:**
- Update packages to compatible versions
- Use alternative packages with compatible requirements
- Create separate environments for conflicting requirements

### pip Command Reference

**Basic Commands:**
```bash
# Install from requirements.txt
pip install -r requirements.txt

# Install specific package
pip install anthropic

# Install with version constraint
pip install "anthropic>=0.18.0"

# Upgrade package
pip install --upgrade anthropic

# List installed packages
pip list

# Show package information
pip show anthropic

# Freeze current environment
pip freeze > requirements.txt

# Uninstall package
pip uninstall anthropic
```

**Advanced Commands:**
```bash
# Install in editable mode (development)
pip install -e .

# Install from git repository
pip install git+https://github.com/user/repo.git

# Install with extra dependencies
pip install "package[extra,features]"

# Install offline from downloaded wheels
pip install --no-index --find-links ./wheels package

# Check for security vulnerabilities
pip audit
```

## Environment Validation and Testing

### Verification Checklist

**1. Python Installation Verification:**
```bash
# Version check
python3 --version
# Should show 3.8.0 or higher

# Module availability
python3 -c "import sys; print(sys.executable)"
# Should show Python executable path

# pip functionality
pip3 --version
# Should show pip version and location
```

**2. Virtual Environment Verification:**
```bash
# Environment creation
python3 -m venv test_env
cd test_env
source bin/activate

# Isolation test
which python
# Should show test_env/bin/python

# Package installation test
pip install requests
python -c "import requests; print('Success!')"

# Cleanup
deactivate
cd ..
rm -rf test_env
```

**3. Project Structure Verification:**
```bash
# Directory creation test
mkdir test_project
cd test_project
mkdir -p src/test_package tests docs templates
touch src/test_package/__init__.py
touch requirements.txt setup.py README.md

# Structure validation
find . -type f -name "*.py" | head -5
find . -type d | sort

# Cleanup
cd ..
rm -rf test_project
```

### Common Environment Issues

**Issue 1: Permission Errors**
```bash
pip install package
# ERROR: Could not install packages due to an EnvironmentError
```
**Diagnosis:**
```bash
ls -la $(which pip3)
# Check if pip is in system location
```
**Solution:**
```bash
# Use virtual environment
python3 -m venv venv
source venv/bin/activate
pip install package  # Now installs to venv
```

**Issue 2: Wrong Python/pip Version**
```bash
python --version   # Python 2.7.x
pip --version      # pip from Python 2.7
```
**Solution:**
```bash
# Always use explicit versions
python3 --version
pip3 --version

# Or create aliases in ~/.zshrc
alias python=python3
alias pip=pip3
```

**Issue 3: PATH Issues**
```bash
pip install package
python -c "import package"  # ImportError
```
**Diagnosis:**
```bash
which python
which pip
# If different locations, PATH is misconfigured
```
**Solution:**
```bash
# Check PATH
echo $PATH

# Ensure virtual environment is activated
source venv/bin/activate
which python && which pip  # Should be same directory
```

**Issue 4: Outdated Tools**
```bash
pip install package
# WARNING: You are using pip version X.X.X; however, version Y.Y.Y is available
```
**Solution:**
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Upgrade setuptools
pip install --upgrade setuptools

# Check versions
pip --version
```

## Development Tools Setup

### Text Editor Configuration

**VS Code (Recommended):**
```bash
# Install VS Code from website or:
brew install --cask visual-studio-code

# Essential Python extensions:
# - Python (Microsoft)
# - Python Docstring Generator
# - Python Type Hint
# - Black Formatter
```

**VS Code Settings for Python:**
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        "**/venv": true
    }
}
```

**Alternative Editors:**
- **PyCharm:** Full-featured IDE, excellent for large projects
- **Sublime Text:** Fast, extensible, good Python support
- **Vim/Neovim:** Powerful for keyboard-focused developers
- **Emacs:** Highly customizable, steep learning curve

### Terminal Enhancement

**Homebrew Installation:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Useful Terminal Tools:**
```bash
# Better shell with plugins
brew install zsh-syntax-highlighting zsh-autosuggestions

# Tree command for directory visualization
brew install tree

# Better ls with colors and icons
brew install exa

# Git with enhanced features
brew install git

# JSON processor for API testing
brew install jq
```

**Terminal Aliases for Python Development:**
```bash
# Add to ~/.zshrc
alias python=python3
alias pip=pip3
alias ll='ls -la'
alias tree='tree -I "__pycache__|*.pyc|venv"'
alias activate='source venv/bin/activate'
```

## Git Version Control Setup

### Git Configuration

**Initial Git Setup:**
```bash
# Configure identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Configure editor
git config --global core.editor "code --wait"

# Configure line endings (Mac/Linux)
git config --global core.autocrlf input

# Configure default branch name
git config --global init.defaultBranch main
```

**Python-Specific .gitignore:**
```bash
# Create .gitignore in project root
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environments
venv/
.venv/
env/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project Specific
.env
*.log
temp/
EOF
```

### Repository Initialization

**Initialize Git Repository:**
```bash
cd myvision-guide-generator
git init
git add .gitignore
git commit -m "Initial commit: Add .gitignore"
```

**Branch Strategy:**
```bash
# Create development branch
git checkout -b develop

# Create feature branches from develop
git checkout -b feature/cli-interface

# Merge back to develop when complete
git checkout develop
git merge feature/cli-interface

# Merge to main for releases
git checkout main
git merge develop
```

## Security and API Key Management

### Environment Variable Security

**Why .env Files:**
- **Security:** API keys not in code or git history
- **Flexibility:** Different keys for development/production
- **Sharing:** Team members use their own keys
- **Rotation:** Easy to change keys without code changes

**Create .env File:**
```bash
# In project root
touch .env
chmod 600 .env  # Restrict permissions

# Add to .env
echo "ANTHROPIC_API_KEY=your_actual_api_key_here" >> .env
```

**Create .env.example Template:**
```bash
# .env.example (safe to commit)
cat > .env.example << EOF
# Required: Get from https://console.anthropic.com/
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Optional: Custom output directory
MYVISION_OUTPUT_DIR=/custom/path/to/guides

# Optional: Organization customization
MYVISION_ORG_NAME=Your Organization Name
MYVISION_CONTACT_EMAIL=your-email@example.com
EOF
```

**Loading Environment Variables:**
```python
# In config.py
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access variables
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable required")
```

### API Key Security Best Practices

**1. Never Commit API Keys:**
```bash
# Always check before committing
git status
git diff --cached

# If accidentally added:
git reset HEAD .env
```

**2. Use Key Rotation:**
```bash
# Regularly generate new API keys
# Update .env file
# Test application with new key
# Deactivate old key
```

**3. Monitor Key Usage:**
- Check Anthropic console for usage patterns
- Set up billing alerts for unexpected usage
- Monitor for unauthorized access patterns

**4. Environment Separation:**
```bash
# Development
.env                    # Local development key

# Production  
.env.production        # Production key (different)

# Testing
.env.test             # Testing key (limited quota)
```

## Testing Your Environment

### Complete Environment Test

**Create test script:**
```bash
cat > test_environment.py << 'EOF'
#!/usr/bin/env python3
"""
Environment validation script for MyVision Guide Generator
"""

import sys
import subprocess
import importlib

def test_python_version():
    """Test Python version is 3.8+"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} (need 3.8+)")
        return False

def test_pip_available():
    """Test pip is available and working"""
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ pip available: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ pip failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ pip error: {e}")
        return False

def test_virtual_env():
    """Test if we're in a virtual environment"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print(f"✅ Virtual environment active: {sys.prefix}")
        return True
    else:
        print("⚠️  Not in virtual environment (recommended)")
        return False

def test_package_installation():
    """Test required packages can be imported"""
    packages = [
        'anthropic',
        'click', 
        'rich',
        'docx',
        'dotenv'
    ]
    
    all_good = True
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} not installed")
            all_good = False
    
    return all_good

def test_environment_variables():
    """Test environment variable loading"""
    try:
        from dotenv import load_dotenv
        import os
        
        load_dotenv()
        api_key = os.getenv("ANTHROPIC_API_KEY")
        
        if api_key:
            print(f"✅ ANTHROPIC_API_KEY loaded ({len(api_key)} characters)")
            return True
        else:
            print("❌ ANTHROPIC_API_KEY not found in environment")
            return False
    except Exception as e:
        print(f"❌ Environment variable test failed: {e}")
        return False

def main():
    """Run all environment tests"""
    print("🔍 Testing MyVision Guide Generator Environment\n")
    
    tests = [
        test_python_version,
        test_pip_available,
        test_virtual_env,
        test_package_installation,
        test_environment_variables
    ]
    
    results = []
    for test in tests:
        results.append(test())
        print()
    
    passed = sum(results)
    total = len(results)
    
    print(f"📊 Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 Environment ready for development!")
        return 0
    else:
        print("⚠️  Some tests failed. Please address issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
EOF

# Make executable and run
chmod +x test_environment.py
python3 test_environment.py
```

### Manual Verification Steps

**1. Directory Structure:**
```bash
tree -a -I 'venv' myvision-guide-generator
```

**2. Virtual Environment:**
```bash
source venv/bin/activate
echo $VIRTUAL_ENV
which python
```

**3. Package Installation:**
```bash
pip list | grep -E "(anthropic|click|rich|docx|dotenv)"
```

**4. Environment Variables:**
```bash
python3 -c "import os; from dotenv import load_dotenv; load_dotenv(); print('API Key:', bool(os.getenv('ANTHROPIC_API_KEY')))"
```

**5. Import Test:**
```bash
python3 -c "
try:
    import anthropic, click, rich, docx, dotenv
    print('✅ All packages import successfully')
except ImportError as e:
    print(f'❌ Import error: {e}')
"
```

## Troubleshooting Common Issues

### macOS-Specific Issues

**Issue 1: Xcode Command Line Tools Missing**
```bash
# Error: xcrun: error: invalid active developer path
```
**Solution:**
```bash
xcode-select --install
```

**Issue 2: SSL Certificate Errors**
```bash
# Error: SSL: CERTIFICATE_VERIFY_FAILED
```
**Solution:**
```bash
# Update certificates
/Applications/Python\ 3.x/Install\ Certificates.command

# Or install via Homebrew Python
brew install python
```

**Issue 3: PATH Issues with Multiple Pythons**
```bash
# Check what's in PATH
echo $PATH | tr ':' '\n' | grep python

# Fix in ~/.zshrc
export PATH="/Library/Frameworks/Python.framework/Versions/3.x/bin:$PATH"
```

### Environment Resolution Strategies

**Strategy 1: Clean Slate**
```bash
# Remove everything and start over
rm -rf venv/
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements.txt
```

**Strategy 2: Alternative Python**
```bash
# Try different Python installation
which python3
/usr/bin/python3 -m venv venv_alt
source venv_alt/bin/activate
```

**Strategy 3: Manual Package Installation**
```bash
# Install packages one by one to isolate issues
pip install anthropic
pip install click
pip install rich
# ... continue until error found
```

## Best Practices Summary

### Development Environment
1. **Always use virtual environments** - Never install packages globally
2. **One environment per project** - Avoid dependency conflicts
3. **Document requirements clearly** - Include version constraints
4. **Test environment setup** - Verify before starting development
5. **Use consistent structure** - Follow Python packaging conventions

### Security
1. **Never commit secrets** - Use .env files and .gitignore
2. **Rotate API keys regularly** - Monitor usage and update keys
3. **Restrict file permissions** - chmod 600 .env
4. **Use environment separation** - Different keys for dev/prod
5. **Monitor key usage** - Watch for unexpected API calls

### Workflow
1. **Activate environment first** - Always source venv/bin/activate
2. **Install before coding** - Set up dependencies completely
3. **Test incrementally** - Verify each step works
4. **Document configuration** - README with setup instructions
5. **Version control setup** - Initialize git early

---

*This environment setup guide provides the foundation for reliable Python development. A properly configured environment prevents 90% of common development issues and enables professional software development practices.*