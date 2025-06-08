# Step 6: Building the Command-Line Interface - Complete Beginner Guide
*Making AI Power Accessible Through Simple Terminal Commands - Zero Experience Required*

## 🎯 What You'll Accomplish in Step 6

By the end of this guide, you will have:
- ✅ Created a professional command-line interface (CLI) for your AI guide generator
- ✅ Built intuitive commands for generating guides with simple typed instructions
- ✅ Implemented beautiful terminal output with colors, progress bars, and clear feedback
- ✅ Added comprehensive help system and error handling for users
- ✅ Tested the complete system: Type command → AI generates → Professional document created

**Time Investment:** 25-30 minutes of CLI magic
**Next Step Preview:** Packaging your tool for easy installation and distribution

## 🔍 Pre-flight Check

Before starting, verify you have:
- ✅ Completed Step 5 (File Management)
- ✅ File manager working: Documents being created successfully
- ✅ Virtual environment activated (you see `(venv)` in your Terminal prompt)
- ✅ All previous components tested and working

**To verify you're ready:**
```bash
# Test the complete AI → Document pipeline
PYTHONPATH=src python3 -c "
import asyncio
from myvision_guides.ai_service import ai_service
from myvision_guides.file_manager import file_manager

async def test():
    # Test AI
    ai_result = await ai_service.test_connection()
    print('✅ AI Service:', 'Working' if ai_result['success'] else 'Failed')
    
    # Test File Manager
    stats = file_manager.get_guide_statistics()
    print('✅ File Manager: Working')
    print(f'📁 Output directory: {stats[\"output_directory\"]}')

asyncio.run(test())
"
```

**If any test fails:** Go back to previous steps and ensure all components are working.

## 🤔 Why Command-Line Interfaces Matter

### The Power of CLI Tools

Think of CLI like **a professional control center:**

**Without CLI (Manual Process):**
```
1. Open code editor → 2. Find Python files → 3. Edit code manually → 
4. Run complex commands → 5. Check for errors → 6. Find output files
Problems: Complex, error-prone, requires programming knowledge
```

**With CLI (Professional Workflow):**
```
Type: myvision generate "VoiceOver basics"
Result: Professional guide created in 30 seconds, saved to Desktop
```

**The Complete User Experience Transformation:**
```
Before CLI:
MyVision Trainer → Spends 30 minutes coding → Maybe gets a guide

After CLI:
MyVision Trainer → Types one command → Gets perfect guide instantly
```

### Real-World CLI Examples You Know

**Every professional tool has a CLI:**
- **Git:** `git commit -m "Updated files"`  
- **NPM:** `npm install express`
- **Docker:** `docker run nginx`
- **Your MyVision Tool:** `myvision generate "iPhone accessibility"`

## 📚 Understanding CLI Architecture

### Command Flow Architecture

**How Your CLI Will Work:**
```
User Types Command
         ↓
Click Framework (Parses command and arguments)
         ↓
CLI Manager (Coordinates workflow)
         ↓
AI Service (Generates content) + File Manager (Creates documents)
         ↓
Beautiful Terminal Output + Professional Document Created
```

### Component Interaction Map

**Complete System Integration:**
```
config.py          → Settings and configuration
ai_service.py      → AI-powered content generation  
file_manager.py    → Document creation and organization
cli.py            → User interface (what we're building)
ui_helpers.py     → Beautiful terminal output
```

**Benefits of This Architecture:**
- ✅ **User-friendly:** Simple commands hide complex programming
- ✅ **Professional:** Beautiful output with progress feedback
- ✅ **Reliable:** Comprehensive error handling and help system
- ✅ **Scalable:** Easy to add new commands and features

## 🛠️ Step-by-Step CLI Creation

### Step 1: Install CLI Dependencies

**Add CLI libraries to your requirements:**
```bash
# Add to requirements.txt
echo "click==8.1.7" >> requirements.txt
echo "rich==13.7.0" >> requirements.txt

# Install the new dependencies
pip3 install -r requirements.txt
```

**What these libraries do:**
- **Click:** Framework for creating command-line interfaces with automatic help and argument parsing
- **Rich:** Beautiful terminal output with colors, progress bars, and formatting

### Step 2: Create ui_helpers.py (Beautiful Terminal Output)

**What this file does:**
- Provides colorful, professional terminal output
- Creates progress bars and status indicators
- Handles error display and success messages

**Create the file:**
```bash
touch src/myvision_guides/ui_helpers.py
code src/myvision_guides/ui_helpers.py
```

**Add this complete UI helper system:**
```python
"""
UI Helper Functions for MyVision Guide Generator CLI

This module provides beautiful, professional terminal output including:
- Colorful status messages and progress indicators
- Professional formatting for results and errors
- Progress bars for long-running operations
- Consistent branding and styling
"""

import time
from typing import Dict, Any, Optional, List
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.panel import Panel
from rich.text import Text
from rich.tree import Tree
from rich.table import Table
from rich import box

# Initialize Rich console for beautiful output
console = Console()

class UIHelpers:
    """Provides consistent, beautiful terminal output for the CLI"""
    
    @staticmethod
    def show_banner():
        """Display the MyVision Guide Generator banner"""
        banner_text = Text()
        banner_text.append("MyVision Guide Generator", style="bold blue")
        banner_text.append("\nAI-Powered Learning Guide Creation Tool", style="italic")
        
        panel = Panel(
            banner_text,
            title="🎯 Welcome",
            border_style="blue",
            padding=(1, 2)
        )
        console.print(panel)
        console.print()
    
    @staticmethod
    def show_success(message: str, details: Optional[Dict[str, Any]] = None):
        """Display success message with optional details"""
        console.print(f"✅ {message}", style="bold green")
        
        if details:
            for key, value in details.items():
                console.print(f"   📁 {key}: {value}", style="dim")
        console.print()
    
    @staticmethod
    def show_error(message: str, details: Optional[str] = None):
        """Display error message with optional details"""
        console.print(f"❌ {message}", style="bold red")
        
        if details:
            console.print(f"   💡 {details}", style="yellow")
        console.print()
    
    @staticmethod
    def show_info(message: str):
        """Display informational message"""
        console.print(f"ℹ️  {message}", style="blue")
    
    @staticmethod
    def show_warning(message: str):
        """Display warning message"""
        console.print(f"⚠️  {message}", style="yellow")
    
    @staticmethod
    def create_progress_bar(description: str):
        """Create a progress bar for long operations"""
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        )
    
    @staticmethod
    def show_guide_result(file_path: str, metadata: Dict[str, Any]):
        """Display beautiful results after guide creation"""
        
        # Create results panel
        results_text = Text()
        results_text.append("Guide Successfully Created!", style="bold green")
        results_text.append(f"\n\n📄 File: ", style="white")
        results_text.append(str(file_path), style="cyan")
        results_text.append(f"\n📝 Title: ", style="white") 
        results_text.append(metadata.get('title', 'Learning Guide'), style="cyan")
        results_text.append(f"\n🎯 Topic: ", style="white")
        results_text.append(metadata.get('topic', 'Unknown'), style="cyan")
        
        panel = Panel(
            results_text,
            title="🎉 Success",
            border_style="green",
            padding=(1, 2)
        )
        console.print(panel)
        console.print()
    
    @staticmethod
    def show_file_statistics(stats: Dict[str, Any]):
        """Display file system statistics in a table"""
        
        table = Table(title="📊 Guide Statistics", box=box.ROUNDED)
        table.add_column("Category", style="cyan", no_wrap=True)
        table.add_column("Count", style="magenta", justify="right")
        table.add_column("Location", style="green")
        
        table.add_row(
            "Learning Guides",
            str(stats.get('learning_guides_count', 0)),
            "Learning_Guides/"
        )
        table.add_row(
            "Session Guides", 
            str(stats.get('session_guides_count', 0)),
            "Session_Guides/"
        )
        table.add_row(
            "Total Guides",
            str(stats.get('total_guides', 0)),
            stats.get('output_directory', 'Unknown')
        )
        
        console.print(table)
        console.print()
    
    @staticmethod
    def show_help_examples():
        """Display helpful command examples"""
        
        examples_text = Text()
        examples_text.append("Common Commands:\n", style="bold white")
        examples_text.append("  myvision generate 'VoiceOver basics'\n", style="cyan")
        examples_text.append("  myvision session transcript.txt\n", style="cyan") 
        examples_text.append("  myvision list\n", style="cyan")
        examples_text.append("  myvision --help\n", style="cyan")
        
        examples_text.append("\nExample Topics:\n", style="bold white")
        examples_text.append("  • iPhone accessibility features\n", style="green")
        examples_text.append("  • JAWS screen reader basics\n", style="green")
        examples_text.append("  • Switch control setup\n", style="green")
        examples_text.append("  • Braille display configuration\n", style="green")
        
        panel = Panel(
            examples_text,
            title="💡 Quick Start Examples",
            border_style="yellow",
            padding=(1, 2)
        )
        console.print(panel)
    
    @staticmethod
    def prompt_confirmation(message: str) -> bool:
        """Ask user for yes/no confirmation"""
        response = console.input(f"❓ {message} (y/N): ")
        return response.lower().startswith('y')
    
    @staticmethod
    def show_loading(message: str, duration: float = 2.0):
        """Show a loading spinner for operations"""
        with console.status(f"[bold blue]{message}...", spinner="dots"):
            time.sleep(duration)

# Create global UI helpers instance
ui = UIHelpers()
```

### Step 3: Create cli.py (Main Command Interface)

**What this file does:**
- Provides the main command-line interface that users interact with
- Coordinates between AI service, file manager, and UI helpers
- Handles all user commands and provides help system

**Create the file:**
```bash
touch src/myvision_guides/cli.py
code src/myvision_guides/cli.py
```

**Add this complete CLI system:**
```python
"""
Command Line Interface for MyVision Guide Generator

This module provides the main CLI interface that users interact with.
It coordinates between all components to provide a seamless experience
for generating AI-powered accessibility guides.

Usage:
    myvision generate "VoiceOver basics"
    myvision session transcript.txt
    myvision list
    myvision --help
"""

import asyncio
import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console

from .ai_service import ai_service
from .file_manager import file_manager  
from .ui_helpers import ui
from .config import config

# Initialize console for error handling
console = Console()

class CLIError(Exception):
    """Custom exception for CLI-specific errors"""
    pass

class CLIManager:
    """
    Manages CLI workflow coordination.
    
    This class coordinates between the AI service, file manager,
    and UI helpers to provide a seamless user experience.
    """
    
    def __init__(self):
        """Initialize CLI manager"""
        self.ai_service = ai_service
        self.file_manager = file_manager
        self.ui = ui
    
    async def generate_topic_guide(self, topic: str, output_format: str = "docx") -> Dict[str, Any]:
        """
        Generate a learning guide for a specific topic.
        
        Args:
            topic: The topic to generate a guide for
            output_format: Output format ('docx' or 'md')
            
        Returns:
            Dictionary with guide creation results
        """
        try:
            # Show progress
            with self.ui.create_progress_bar("Generating guide") as progress:
                task = progress.add_task("🤖 AI generating content...", total=100)
                
                # Generate AI content
                progress.update(task, advance=30)
                guide_data = await self.ai_service.generate_topic_guide(topic)
                
                progress.update(task, advance=40, description="📄 Creating document...")
                
                # Prepare metadata
                metadata = {
                    'title': f"{guide_data['topic'].title()} - Learning Guide",
                    'topic': guide_data['topic'],
                    'guide_type': guide_data['guide_type'],
                    'generated_by': 'MyVision Guide Generator CLI'
                }
                
                # Create document
                if output_format.lower() == 'docx':
                    file_path = self.file_manager.save_word_document(guide_data['content'], metadata)
                else:
                    file_path = self.file_manager.save_markdown_file(guide_data['content'], metadata)
                
                progress.update(task, advance=30, description="✅ Guide complete!")
                
            return {
                'success': True,
                'file_path': file_path,
                'metadata': metadata,
                'content_length': len(guide_data['content'])
            }
            
        except Exception as e:
            raise CLIError(f"Failed to generate guide: {e}")
    
    async def generate_session_guide(self, transcript_file: Path, output_format: str = "docx") -> Dict[str, Any]:
        """
        Generate a session guide from a transcript file.
        
        Args:
            transcript_file: Path to transcript file
            output_format: Output format ('docx' or 'md')
            
        Returns:
            Dictionary with guide creation results
        """
        try:
            # Verify transcript file exists
            if not transcript_file.exists():
                raise CLIError(f"Transcript file not found: {transcript_file}")
            
            # Read transcript content
            with open(transcript_file, 'r', encoding='utf-8') as f:
                transcript_content = f.read()
            
            if not transcript_content.strip():
                raise CLIError("Transcript file is empty")
            
            # Show progress
            with self.ui.create_progress_bar("Generating session guide") as progress:
                task = progress.add_task("🤖 AI analyzing transcript...", total=100)
                
                # Generate AI content
                progress.update(task, advance=30)
                guide_data = await self.ai_service.generate_session_guide(transcript_content)
                
                progress.update(task, advance=40, description="📄 Creating document...")
                
                # Prepare metadata
                metadata = {
                    'title': f"Training Session Guide - {transcript_file.stem}",
                    'topic': guide_data.get('topic', transcript_file.stem),
                    'guide_type': 'session',
                    'source_file': str(transcript_file),
                    'generated_by': 'MyVision Guide Generator CLI'
                }
                
                # Create document
                if output_format.lower() == 'docx':
                    file_path = self.file_manager.save_word_document(guide_data['content'], metadata)
                else:
                    file_path = self.file_manager.save_markdown_file(guide_data['content'], metadata)
                
                progress.update(task, advance=30, description="✅ Session guide complete!")
                
            return {
                'success': True,
                'file_path': file_path,
                'metadata': metadata,
                'content_length': len(guide_data['content'])
            }
            
        except Exception as e:
            raise CLIError(f"Failed to generate session guide: {e}")
    
    def get_file_statistics(self) -> Dict[str, Any]:
        """Get current file system statistics"""
        try:
            return self.file_manager.get_guide_statistics()
        except Exception as e:
            raise CLIError(f"Failed to get file statistics: {e}")

# Create global CLI manager
cli_manager = CLIManager()

# Click command group setup
@click.group()
@click.version_option(version="1.0.0", prog_name="MyVision Guide Generator")
@click.pass_context
def main(ctx):
    """
    🎯 MyVision Guide Generator - AI-Powered Learning Guide Creation
    
    Transform accessibility topics into professional learning guides in seconds.
    Perfect for MyVision trainers and accessibility professionals.
    
    Examples:
      myvision generate "VoiceOver basics"
      myvision session transcript.txt
      myvision list
    """
    # Ensure we're running in an async context
    if ctx.invoked_subcommand is None:
        ui.show_banner()
        ui.show_help_examples()

@main.command()
@click.argument('topic', required=True)
@click.option('--format', '-f', default='docx', type=click.Choice(['docx', 'md']), 
              help='Output format (docx or md)')
@click.option('--show-content', is_flag=True, help='Display generated content in terminal')
def generate(topic: str, format: str, show_content: bool):
    """
    Generate a learning guide for any accessibility topic.
    
    TOPIC: The accessibility topic to create a guide for
    
    Examples:
      myvision generate "iPhone VoiceOver basics"
      myvision generate "JAWS screen reader setup" --format md
      myvision generate "Switch control configuration" --show-content
    """
    async def run_generate():
        try:
            ui.show_info(f"Generating learning guide for: {topic}")
            
            # Generate guide
            result = await cli_manager.generate_topic_guide(topic, format)
            
            # Show results
            ui.show_guide_result(result['file_path'], result['metadata'])
            
            # Show content if requested
            if show_content:
                console.print("📄 Generated Content:", style="bold")
                console.print("-" * 50)
                
                if format == 'docx':
                    console.print("Content saved to Word document. Use --format md to preview content.", style="yellow")
                else:
                    with open(result['file_path'], 'r') as f:
                        content = f.read()
                        console.print(content)
            
            ui.show_success("Guide generation complete!")
            
        except CLIError as e:
            ui.show_error("Generation failed", str(e))
            sys.exit(1)
        except Exception as e:
            ui.show_error("Unexpected error", f"Please check your configuration: {e}")
            sys.exit(1)
    
    # Run async function
    asyncio.run(run_generate())

@main.command()
@click.argument('transcript_file', type=click.Path(exists=True, path_type=Path))
@click.option('--format', '-f', default='docx', type=click.Choice(['docx', 'md']),
              help='Output format (docx or md)')
def session(transcript_file: Path, format: str):
    """
    Generate a session guide from a training transcript file.
    
    TRANSCRIPT_FILE: Path to the transcript file (.txt, .md, etc.)
    
    Examples:
      myvision session session_notes.txt
      myvision session "~/Desktop/training_transcript.txt" --format md
    """
    async def run_session():
        try:
            ui.show_info(f"Generating session guide from: {transcript_file.name}")
            
            # Generate session guide
            result = await cli_manager.generate_session_guide(transcript_file, format)
            
            # Show results
            ui.show_guide_result(result['file_path'], result['metadata'])
            ui.show_success("Session guide generation complete!")
            
        except CLIError as e:
            ui.show_error("Session generation failed", str(e))
            sys.exit(1)
        except Exception as e:
            ui.show_error("Unexpected error", f"Please check your transcript file: {e}")
            sys.exit(1)
    
    # Run async function
    asyncio.run(run_session())

@main.command()
@click.option('--detailed', '-d', is_flag=True, help='Show detailed file information')
def list(detailed: bool):
    """
    List all generated guides and show statistics.
    
    Examples:
      myvision list
      myvision list --detailed
    """
    try:
        ui.show_info("Retrieving guide statistics...")
        
        # Get statistics
        stats = cli_manager.get_file_statistics()
        
        # Show results
        ui.show_file_statistics(stats)
        
        if detailed and stats['total_guides'] > 0:
            ui.show_info("Detailed file listing:")
            
            # List actual files
            output_dir = Path(stats['output_directory'])
            
            if output_dir.exists():
                # Learning guides
                learning_dir = output_dir / "Learning_Guides"
                if learning_dir.exists():
                    learning_files = list(learning_dir.glob("*"))
                    if learning_files:
                        console.print("\n📚 Learning Guides:", style="bold cyan")
                        for file in sorted(learning_files):
                            console.print(f"  • {file.name}", style="green")
                
                # Session guides
                session_dir = output_dir / "Session_Guides"
                if session_dir.exists():
                    session_files = list(session_dir.glob("*"))
                    if session_files:
                        console.print("\n👥 Session Guides:", style="bold cyan")
                        for file in sorted(session_files):
                            console.print(f"  • {file.name}", style="green")
        
        if stats['total_guides'] == 0:
            ui.show_info("No guides created yet. Try: myvision generate 'VoiceOver basics'")
        
    except CLIError as e:
        ui.show_error("Failed to list guides", str(e))
        sys.exit(1)
    except Exception as e:
        ui.show_error("Unexpected error", str(e))
        sys.exit(1)

@main.command()
def test():
    """
    Test all system components and configuration.
    
    Verifies:
    - AI service connection
    - File manager setup
    - Output directory access
    - Dependencies installation
    """
    async def run_test():
        try:
            ui.show_info("Testing MyVision Guide Generator components...")
            console.print()
            
            # Test AI service
            with ui.create_progress_bar("Testing components") as progress:
                task = progress.add_task("🤖 Testing AI service...", total=100)
                
                ai_result = await ai_service.test_connection()
                progress.update(task, advance=33)
                
                if ai_result['success']:
                    ui.show_success("AI Service connection working")
                else:
                    ui.show_error("AI Service failed", ai_result.get('error', 'Unknown error'))
                    return
                
                # Test file manager
                progress.update(task, advance=33, description="📁 Testing file manager...")
                
                stats = file_manager.get_guide_statistics()
                if stats['directory_exists']:
                    ui.show_success("File manager working", {
                        'Output directory': stats['output_directory'],
                        'Learning guides': stats['learning_guides_count'],
                        'Session guides': stats['session_guides_count']
                    })
                else:
                    ui.show_error("File manager setup issue", f"Cannot access {stats['output_directory']}")
                    return
                
                progress.update(task, advance=34, description="✅ All tests complete!")
            
            ui.show_success("🎉 All components working perfectly!")
            ui.show_info("Ready to generate guides. Try: myvision generate 'VoiceOver basics'")
            
        except Exception as e:
            ui.show_error("Test failed", str(e))
            sys.exit(1)
    
    # Run async function
    asyncio.run(run_test())

# Entry point for CLI
if __name__ == '__main__':
    main()
```

### Step 4: Create Setup Entry Point

**Make your CLI easily accessible:**
```bash
# Create setup.py for easy installation
touch setup.py
code setup.py
```

**Add this setup configuration:**
```python
"""
Setup configuration for MyVision Guide Generator
"""

from setuptools import setup, find_packages

setup(
    name="myvision-guides",
    version="1.0.0",
    description="AI-powered accessibility learning guide generator",
    author="MyVision Oxfordshire",
    author_email="info@myvision.org",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "anthropic>=0.3.0",
        "python-dotenv>=1.0.0", 
        "python-docx>=0.8.11",
        "click>=8.1.7",
        "rich>=13.7.0"
    ],
    entry_points={
        'console_scripts': [
            'myvision=myvision_guides.cli:main',
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", 
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
```

## ✅ Validation and Testing

### Test 1: Install CLI Dependencies

**Verify the new libraries are installed:**
```bash
# Test Click framework
python3 -c "import click; print('✅ Click framework installed')"

# Test Rich console
python3 -c "from rich.console import Console; Console().print('✅ Rich console working', style='green')"
```

**Expected output:**
```
✅ Click framework installed
✅ Rich console working
```

### Test 2: Test UI Helpers

**Verify beautiful terminal output works:**
```bash
PYTHONPATH=src python3 -c "
from myvision_guides.ui_helpers import ui

# Test banner
ui.show_banner()

# Test success message
ui.show_success('UI helpers working!', {'Test': 'Passed'})

# Test info message
ui.show_info('UI components ready')
"
```

### Test 3: Test CLI Import

**Verify CLI module loads correctly:**
```bash
PYTHONPATH=src python3 -c "
from myvision_guides.cli import cli_manager
print('✅ CLI manager imported successfully')

# Test CLI components
print('✅ AI service accessible:', hasattr(cli_manager, 'ai_service'))
print('✅ File manager accessible:', hasattr(cli_manager, 'file_manager'))
print('✅ UI helpers accessible:', hasattr(cli_manager, 'ui'))
"
```

### Test 4: CLI Help System

**Test the help documentation:**
```bash
# Test main help
PYTHONPATH=src python3 -m myvision_guides.cli --help

# Test command-specific help
PYTHONPATH=src python3 -m myvision_guides.cli generate --help
PYTHONPATH=src python3 -m myvision_guides.cli list --help
```

### Test 5: Full CLI Workflow

**Test the complete command workflow:**
```bash
# Test the system check command
PYTHONPATH=src python3 -m myvision_guides.cli test
```

**Expected output:**
```
ℹ️  Testing MyVision Guide Generator components...

✅ AI Service connection working
✅ File manager working
   📁 Output directory: /Users/jamie/Desktop/MyVision_Guides
   📁 Learning guides: 0
   📁 Session guides: 0

✅ 🎉 All components working perfectly!
ℹ️  Ready to generate guides. Try: myvision generate 'VoiceOver basics'
```

### Test 6: Generate Your First CLI Guide

**Create your first guide using the CLI:**
```bash
# Generate a sample guide with beautiful CLI output
PYTHONPATH=src python3 -m myvision_guides.cli generate "CLI testing guide"
```

**Expected workflow:**
```
ℹ️  Generating learning guide for: CLI testing guide

🤖 AI generating content...     ████████████████████ 30%
📄 Creating document...         ████████████████████ 70%
✅ Guide complete!             ████████████████████ 100%

╭─────────── 🎉 Success ───────────╮
│ Guide Successfully Created!       │
│                                   │
│ 📄 File: /Users/.../cli_testing_  │
│ guide_learning_guide_20241215_... │
│ 📝 Title: Cli Testing Guide -     │
│ Learning Guide                    │
│ 🎯 Topic: CLI testing guide       │
╰───────────────────────────────────╯

✅ Guide generation complete!
```

## 🔧 Troubleshooting Common Issues

### Issue: "ModuleNotFoundError: No module named 'click'"

**Cause:** CLI dependencies not installed

**Solutions:**
```bash
# 1. Verify virtual environment is active
echo $VIRTUAL_ENV  # Should show path to venv

# 2. Install dependencies
pip3 install -r requirements.txt

# 3. Verify installation
python3 -c "import click, rich; print('✅ CLI dependencies installed')"
```

### Issue: CLI commands not working

**Cause:** PYTHONPATH not set or incorrect module imports

**Solutions:**
```bash
# 1. Test with explicit PYTHONPATH
PYTHONPATH=src python3 -m myvision_guides.cli --help

# 2. If that works, create an alias
echo 'alias myvision="PYTHONPATH=src python3 -m myvision_guides.cli"' >> ~/.zshrc
source ~/.zshrc

# 3. Test the alias
myvision --help
```

### Issue: "ImportError: attempted relative import with no known parent package"

**Cause:** Running Python files directly instead of as modules

**Solutions:**
```bash
# ❌ Don't do this:
python3 src/myvision_guides/cli.py

# ✅ Do this instead:
PYTHONPATH=src python3 -m myvision_guides.cli

# Or install the package properly:
pip3 install -e .
myvision --help
```

### Issue: Rich formatting not displaying properly

**Cause:** Terminal compatibility issues

**Solutions:**
```bash
# 1. Check terminal support
python3 -c "
from rich.console import Console
console = Console()
console.print('This should be [bold red]RED[/bold red] and [bold blue]BLUE[/bold blue]')
"

# 2. If colors don't appear, try force mode
PYTHONPATH=src python3 -c "
from rich.console import Console
console = Console(force_terminal=True)
console.print('Forced colors [bold green]should work[/bold green]')
"
```

### Issue: Permission denied creating files

**Cause:** Desktop access restrictions

**Solutions:**
```bash
# 1. Check Desktop permissions
ls -la ~/Desktop/ | head -5

# 2. Test file creation
touch ~/Desktop/test_file.txt && rm ~/Desktop/test_file.txt && echo "✅ Write access working"

# 3. Use alternative directory if needed
mkdir -p ~/Documents/MyVision_Guides
echo 'MYVISION_OUTPUT_DIR=~/Documents/MyVision_Guides' >> .env
```

### Issue: Progress bars not appearing

**Cause:** Terminal doesn't support progress display

**Solutions:**
```bash
# 1. Test Rich progress
python3 -c "
from rich.progress import Progress
import time

with Progress() as progress:
    task = progress.add_task('Testing...', total=100)
    for i in range(100):
        progress.update(task, advance=1)
        time.sleep(0.01)
"

# 2. If progress doesn't work, disable in ui_helpers.py
# Change Progress() to use simpler output
```

### Issue: Commands hang or freeze

**Cause:** API timeout or network issues

**Solutions:**
```bash
# 1. Test API connection separately
PYTHONPATH=src python3 -c "
import asyncio
from myvision_guides.ai_service import ai_service

async def test():
    try:
        result = await ai_service.test_connection()
        print('✅ API working:', result['success'])
    except Exception as e:
        print('❌ API failed:', e)

asyncio.run(test())
"

# 2. Check internet connection
curl -s https://api.anthropic.com > /dev/null && echo "✅ Anthropic API reachable"

# 3. Verify API key
echo "API Key length:" ${#ANTHROPIC_API_KEY}  # Should be > 50 characters
```

## 🚀 Next Steps Preview

With your CLI complete, you're ready for **Step 7: Packaging and Distribution**:

**What's Coming Next:**
- 📦 Creating a proper Python package with setup.py
- 🔧 Making your tool installable with `pip install`
- 🌐 Setting up development and production modes
- 📋 Creating requirements files for different environments
- 🎯 Building scripts for easy deployment and updates

**Files You'll Create in Step 7:**
- `setup.py` - Package configuration for pip installation
- `pyproject.toml` - Modern Python packaging configuration
- `MANIFEST.in` - Specify which files to include in package
- `scripts/install.sh` - Easy installation script for users
- `README.md` - Complete user documentation

**Installation Methods You'll Enable:**
```bash
# Development mode (for coding)
pip install -e .

# User mode (for trainers)
pip install myvision-guides

# Direct from GitHub
pip install git+https://github.com/yourusername/myvision-guides.git
```

**Why Packaging Matters:**
Your CLI tool transforms MyVision trainers from requiring coding skills to using professional, installable software. Proper packaging ensures easy distribution, updates, and professional deployment.

You now have a **complete, professional command-line interface** that makes AI-powered guide generation accessible to everyone!

---

**🎯 Learning Objective Achieved:** You can now provide users with simple, intuitive commands that transform accessibility topics into professional documents through beautiful terminal interactions.

**⭐ Professional Skill Unlocked:** Command-line interface design and user experience - essential for any professional development tool.

**Ready for Step 7?** Let's make your powerful CLI tool easily installable and distributable!