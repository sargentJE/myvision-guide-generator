# Step 5: Creating Professional Documents - Complete Beginner Guide
*Transforming AI Intelligence into Beautiful, Branded Word Documents - Zero Experience Required*

## 🎯 What You'll Accomplish in Step 5

By the end of this guide, you will have:
- ✅ Created a complete file management system for organizing guides
- ✅ Built a Word document generator with MyVision branding
- ✅ Implemented smart file naming and directory organization
- ✅ Tested the complete AI → Document pipeline
- ✅ Generated your first professional MyVision learning guide

**Time Investment:** 20-25 minutes of document magic
**Next Step Preview:** Building the command-line interface for user interaction

## 🔍 Pre-flight Check

Before starting, verify you have:
- ✅ Completed Step 4 (AI Integration)
- ✅ AI service working: Guide generation tested successfully
- ✅ Virtual environment activated (you see `(venv)` in your Terminal prompt)
- ✅ All dependencies installed from requirements.txt

**To verify you're ready:**
```bash
# Test AI service is working
PYTHONPATH=src python3 -c "
import asyncio
from myvision_guides.ai_service import ai_service

async def test():
    result = await ai_service.test_connection()
    print('✅ AI Service:', 'Working' if result['success'] else 'Failed')

asyncio.run(test())
"
```

**If AI test fails:** Go back to Step 4 and complete the AI integration first.

## 🤔 Why File Management Matters

### The Document Creation Pipeline

Think of file management like **a professional publishing house:**

**Without File Management (Chaos):**
```
AI generates text → You copy/paste → Manual formatting → Save somewhere
Problems: No organization, inconsistent formatting, lost files
```

**With File Management (Professional):**
```
AI generates text → Automatic formatting → Branded documents → Organized storage
Result: Professional guides ready for trainers and learners
```

**The Complete Transformation:**
```
"VoiceOver basics" (your input)
         ↓
AI Service: Generates comprehensive guide
         ↓
File Manager: Creates professional Word document
         ↓
Output: ~/Desktop/MyVision_Guides/Learning_Guides/
        voiceover_basics_learning_guide_20241215_143022.docx
```

## 📚 Understanding File Management Architecture

### Directory Organization System

**Professional Structure We'll Create:**
```
~/Desktop/MyVision_Guides/
├── Learning_Guides/                    ← Topic-based guides
│   ├── voiceover_basics_20241215.docx  ← Auto-generated files
│   ├── jaws_setup_guide_20241215.docx
│   └── ...
└── Session_Guides/                     ← Training session guides
    ├── sarah_session_20241215.docx     ← Personalized guides
    └── ...
```

**Benefits of This Organization:**
- ✅ **Easy to find:** Logical categorization by guide type
- ✅ **No overwrites:** Timestamp-based unique filenames
- ✅ **Professional:** Ready for trainers to access and use
- ✅ **Scalable:** Handles hundreds of guides without confusion

### File Naming Intelligence

**Smart Filename Generation:**
```
Input: "VoiceOver Rotor Navigation!" 
Process: Clean → Organize → Timestamp → Extension
Output: voiceover_rotor_navigation_learning_guide_20241215_143022.docx
```

**Why This Naming System Works:**
- **Descriptive:** Tells you exactly what the guide covers
- **Safe:** No special characters that cause problems
- **Unique:** Timestamp prevents duplicate filenames
- **Sortable:** Files automatically sort by creation date

## 🛠️ Step-by-Step File Manager Creation

### Step 1: Create file_manager.py (Document Creation Engine)

**What this file does:**
- Takes AI-generated text and creates professional Word documents
- Handles file naming, directory organization, and formatting
- Adds MyVision branding and professional styling

**Create the file:**
```bash
touch src/myvision_guides/file_manager.py
code src/myvision_guides/file_manager.py
```

**Add this complete file management system:**
```python
"""
File Management System for MyVision Guide Generator

This module handles:
- Creating organized directory structures
- Generating professional Word documents with branding
- Safe filename creation with timestamps
- Document formatting and styling
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

from .config import config


class FileManagerError(Exception):
    """Raised when file management operations fail"""
    pass


class FileManager:
    """
    Handles creation and organization of guide documents.
    
    This class transforms AI-generated content into professional, 
    branded Word documents with proper organization and formatting.
    """
    
    def __init__(self):
        """Initialize file manager with configuration"""
        self.output_directory = config.output_directory
        self.organization_name = config.organization_name
        self.contact_email = config.contact_email
        
        # Ensure output directories exist
        self.ensure_directories()
    
    def ensure_directories(self):
        """
        Create the complete directory structure if it doesn't exist.
        
        Creates:
        - Main MyVision_Guides directory
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
            raise FileManagerError(
                f"Permission denied creating directories at {self.output_directory}. "
                f"Please check directory permissions."
            )
        except Exception as e:
            raise FileManagerError(f"Failed to create directories: {e}")
    
    def generate_filename(self, title: str, guide_type: str, format_type: str = "docx") -> str:
        """
        Generate a safe, unique filename for a guide.
        
        Args:
            title: The guide title (e.g., "VoiceOver Basics")
            guide_type: "learning" or "session"
            format_type: "docx" or "markdown"
        
        Returns:
            Safe filename with timestamp and extension
            
        Example:
            Input: "VoiceOver Rotor Navigation!", "learning", "docx"
            Output: "voiceover_rotor_navigation_learning_guide_20241215_143022.docx"
        """
        # Clean the title
        clean_title = self._clean_filename_text(title)
        
        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Combine components
        filename_parts = [
            clean_title,
            guide_type,
            "guide",
            timestamp
        ]
        
        filename_base = "_".join(filter(None, filename_parts))
        
        # Add extension
        extension = f".{format_type}"
        
        return filename_base + extension
    
    def _clean_filename_text(self, text: str) -> str:
        """
        Clean text to make it safe for filenames.
        
        Args:
            text: Raw text that might contain unsafe characters
            
        Returns:
            Cleaned text safe for filenames
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters, keep only letters, numbers, spaces, and hyphens
        text = re.sub(r'[^a-z0-9\s\-]', '', text)
        
        # Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text)
        
        # Replace spaces with underscores
        text = text.replace(' ', '_')
        
        # Replace multiple underscores with single underscore
        text = re.sub(r'_+', '_', text)
        
        # Remove leading/trailing underscores
        text = text.strip('_')
        
        # Limit length (keep first 30 characters for readability)
        if len(text) > 30:
            text = text[:30].rstrip('_')
        
        return text
    
    def save_word_document(self, content: str, metadata: Dict[str, Any]) -> Path:
        """
        Create a professional Word document with MyVision branding.
        
        Args:
            content: The guide content (markdown-formatted text from AI)
            metadata: Guide metadata (title, topic, etc.)
            
        Returns:
            Path to the created document
            
        Raises:
            FileManagerError: If document creation fails
        """
        try:
            # Generate filename
            guide_type = "learning" if metadata.get("guide_type") == "topic" else "session"
            filename = self.generate_filename(
                title=metadata.get("topic", metadata.get("title", "guide")),
                guide_type=guide_type,
                format_type="docx"
            )
            
            # Determine subdirectory
            if guide_type == "learning":
                subdirectory = "Learning_Guides"
            else:
                subdirectory = "Session_Guides"
            
            # Full file path
            file_path = self.output_directory / subdirectory / filename
            
            # Create the Word document
            document = Document()
            
            # Add MyVision header
            self._add_document_header(document, metadata)
            
            # Add content
            self._add_document_content(document, content)
            
            # Add footer
            self._add_document_footer(document)
            
            # Save the document
            document.save(str(file_path))
            
            return file_path
            
        except Exception as e:
            raise FileManagerError(f"Failed to create Word document: {e}")
    
    def _add_document_header(self, document: Document, metadata: Dict[str, Any]):
        """Add professional header with MyVision branding"""
        
        # Document title (large, bold, centered)
        title_paragraph = document.add_paragraph()
        title_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        title_run = title_paragraph.add_run(metadata.get("title", "Learning Guide"))
        title_run.font.size = Pt(18)
        title_run.bold = True
        
        # Organization name (medium, centered)
        org_paragraph = document.add_paragraph()
        org_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        org_run = org_paragraph.add_run(self.organization_name)
        org_run.font.size = Pt(12)
        
        # Generation date (small, centered)
        date_paragraph = document.add_paragraph()
        date_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        date_str = datetime.now().strftime("%B %d, %Y")
        date_run = date_paragraph.add_run(f"Generated: {date_str}")
        date_run.font.size = Pt(10)
        
        # Add separator line
        separator = document.add_paragraph()
        separator.add_run("_" * 50)
        separator.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Add spacing
        document.add_paragraph()
    
    def _add_document_content(self, document: Document, content: str):
        """
        Parse markdown content and add to Word document with proper formatting.
        
        Args:
            document: The Word document to add content to
            content: Markdown-formatted content from AI
        """
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            if not line:
                # Empty line - add paragraph break
                document.add_paragraph()
                continue
            
            if line.startswith('# '):
                # Main heading (H1)
                heading_text = line[2:].strip()
                paragraph = document.add_heading(heading_text, level=1)
                
            elif line.startswith('## '):
                # Sub heading (H2)
                heading_text = line[3:].strip()
                document.add_heading(heading_text, level=2)
                
            elif line.startswith('### '):
                # Sub-sub heading (H3)
                heading_text = line[4:].strip()
                document.add_heading(heading_text, level=3)
                
            elif line.startswith('- ') or line.startswith('* '):
                # Bullet point
                bullet_text = line[2:].strip()
                paragraph = document.add_paragraph(bullet_text, style='List Bullet')
                
            elif re.match(r'^\d+\.\s', line):
                # Numbered list
                # Remove the number and period, keep the text
                numbered_text = re.sub(r'^\d+\.\s', '', line)
                paragraph = document.add_paragraph(numbered_text, style='List Number')
                
            else:
                # Regular paragraph
                paragraph = document.add_paragraph(line)
    
    def _add_document_footer(self, document: Document):
        """Add professional footer with contact information"""
        
        # Add spacing before footer
        document.add_paragraph()
        
        # Footer separator
        separator = document.add_paragraph()
        separator.add_run("_" * 50)
        separator.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Contact information
        footer_paragraph = document.add_paragraph()
        footer_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        footer_text = f"{self.organization_name} | Email: {self.contact_email}"
        footer_run = footer_paragraph.add_run(footer_text)
        footer_run.font.size = Pt(8)
    
    def save_markdown_file(self, content: str, metadata: Dict[str, Any]) -> Path:
        """
        Save content as a markdown file with metadata header.
        
        Args:
            content: The guide content
            metadata: Guide metadata
            
        Returns:
            Path to the created markdown file
        """
        try:
            # Generate filename
            guide_type = "learning" if metadata.get("guide_type") == "topic" else "session"
            filename = self.generate_filename(
                title=metadata.get("topic", metadata.get("title", "guide")),
                guide_type=guide_type,
                format_type="md"
            )
            
            # Determine subdirectory
            subdirectory = "Learning_Guides" if guide_type == "learning" else "Session_Guides"
            
            # Full file path
            file_path = self.output_directory / subdirectory / filename
            
            # Create markdown content with metadata
            markdown_content = self._create_markdown_with_metadata(content, metadata)
            
            # Write to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            return file_path
            
        except Exception as e:
            raise FileManagerError(f"Failed to create markdown file: {e}")
    
    def _create_markdown_with_metadata(self, content: str, metadata: Dict[str, Any]) -> str:
        """Create markdown file with metadata header"""
        
        # YAML metadata header
        metadata_header = f"""---
type: {metadata.get('guide_type', 'Guide')}
title: {metadata.get('title', 'Learning Guide')}
topic: {metadata.get('topic', 'Unknown')}
generated: {datetime.now().isoformat()}
organization: {self.organization_name}
---

"""
        
        return metadata_header + content
    
    def get_guide_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about saved guides.
        
        Returns:
            Dictionary with file counts and directory information
        """
        try:
            stats = {
                "output_directory": str(self.output_directory),
                "directory_exists": self.output_directory.exists(),
                "learning_guides_count": 0,
                "session_guides_count": 0,
                "total_guides": 0
            }
            
            if self.output_directory.exists():
                # Count learning guides
                learning_dir = self.output_directory / "Learning_Guides"
                if learning_dir.exists():
                    learning_files = list(learning_dir.glob("*.docx")) + list(learning_dir.glob("*.md"))
                    stats["learning_guides_count"] = len(learning_files)
                
                # Count session guides
                session_dir = self.output_directory / "Session_Guides"
                if session_dir.exists():
                    session_files = list(session_dir.glob("*.docx")) + list(session_dir.glob("*.md"))
                    stats["session_guides_count"] = len(session_files)
                
                stats["total_guides"] = stats["learning_guides_count"] + stats["session_guides_count"]
            
            return stats
            
        except Exception as e:
            raise FileManagerError(f"Failed to get guide statistics: {e}")


# Create global file manager instance
file_manager = FileManager()
```

### Step 2: Test File Manager Creation

**Test directory creation:**
```bash
PYTHONPATH=src python3 -c "
from myvision_guides.file_manager import file_manager

# Test directory creation
file_manager.ensure_directories()
print('✅ Directories created successfully')

# Check directory structure
import os
output_dir = file_manager.output_directory
print(f'📁 Output directory: {output_dir}')
print(f'📁 Learning guides: {output_dir}/Learning_Guides')
print(f'📁 Session guides: {output_dir}/Session_Guides')

# Verify directories exist
if (output_dir / 'Learning_Guides').exists():
    print('✅ Learning_Guides directory created')
if (output_dir / 'Session_Guides').exists():
    print('✅ Session_Guides directory created')
"
```

**Test filename generation:**
```bash
PYTHONPATH=src python3 -c "
from myvision_guides.file_manager import file_manager

# Test various filename scenarios
test_titles = [
    'VoiceOver Basics',
    'JAWS Setup & Configuration!',
    'iPhone VoiceOver: Advanced Navigation Techniques',
    'Switch Access on iPad - Getting Started'
]

print('🧪 Testing filename generation:')
for title in test_titles:
    filename = file_manager.generate_filename(title, 'learning', 'docx')
    print(f'  {title} → {filename}')
"
```

### Step 3: Create Complete AI to Document Pipeline

**Test the complete workflow:**
```bash
PYTHONPATH=src python3 -c "
import asyncio
from myvision_guides.ai_service import ai_service
from myvision_guides.file_manager import file_manager

async def test_complete_pipeline():
    print('🚀 Testing Complete AI → Document Pipeline')
    print()
    
    # Step 1: Generate AI content
    print('⚡ Step 1: Generating AI content...')
    try:
        guide_data = await ai_service.generate_topic_guide('VoiceOver basics for beginners')
        print('✅ AI content generated successfully')
        print(f'📝 Content length: {len(guide_data[\"content\"])} characters')
    except Exception as e:
        print(f'❌ AI generation failed: {e}')
        return
    
    # Step 2: Create Word document
    print()
    print('📄 Step 2: Creating Word document...')
    try:
        # Prepare metadata for document
        metadata = {
            'title': 'VoiceOver Basics - Learning Guide',
            'topic': guide_data['topic'],
            'guide_type': guide_data['guide_type'],
            'generated': True
        }
        
        doc_path = file_manager.save_word_document(guide_data['content'], metadata)
        print('✅ Word document created successfully')
        print(f'📁 Saved to: {doc_path}')
        
    except Exception as e:
        print(f'❌ Document creation failed: {e}')
        return
    
    # Step 3: Get statistics
    print()
    print('📊 Step 3: File system status...')
    stats = file_manager.get_guide_statistics()
    print(f'📂 Output directory: {stats[\"output_directory\"]}')
    print(f'📚 Learning guides: {stats[\"learning_guides_count\"]}')
    print(f'👥 Session guides: {stats[\"session_guides_count\"]}')
    print(f'📖 Total guides: {stats[\"total_guides\"]}')
    
    print()
    print('🎉 Complete pipeline test successful!')
    print('✅ AI generates content → File manager creates professional document')

asyncio.run(test_complete_pipeline())
"
```

## ✅ Validation and Testing

### Test 1: Directory Structure Verification

**Check your desktop for the new folder structure:**
```bash
# Check if MyVision_Guides folder was created
ls -la ~/Desktop/ | grep MyVision

# Check subdirectories
ls -la ~/Desktop/MyVision_Guides/
```

**Expected output:**
```
drwxr-xr-x  4 jamie  staff  128 Dec 15 14:30 Learning_Guides
drwxr-xr-x  4 jamie  staff  128 Dec 15 14:30 Session_Guides
```

### Test 2: Word Document Creation

**Generate and open your first professional guide:**
```bash
PYTHONPATH=src python3 -c "
import asyncio
from myvision_guides.ai_service import ai_service
from myvision_guides.file_manager import file_manager

async def create_sample_guide():
    # Generate guide
    guide_data = await ai_service.generate_topic_guide('iPhone accessibility basics')
    
    # Create document
    metadata = {
        'title': 'iPhone Accessibility Basics - Learning Guide',
        'topic': guide_data['topic'],
        'guide_type': guide_data['guide_type']
    }
    
    doc_path = file_manager.save_word_document(guide_data['content'], metadata)
    print(f'📄 Guide created: {doc_path}')
    
    # Open the document (macOS)
    import subprocess
    subprocess.run(['open', str(doc_path)])

asyncio.run(create_sample_guide())
"
```

### Test 3: Markdown Export

**Test markdown file creation:**
```bash
PYTHONPATH=src python3 -c "
import asyncio
from myvision_guides.ai_service import ai_service
from myvision_guides.file_manager import file_manager

async def create_markdown_guide():
    guide_data = await ai_service.generate_topic_guide('TalkBack basics')
    
    metadata = {
        'title': 'TalkBack Basics - Learning Guide',
        'topic': guide_data['topic'],
        'guide_type': guide_data['guide_type']
    }
    
    md_path = file_manager.save_markdown_file(guide_data['content'], metadata)
    print(f'📝 Markdown guide created: {md_path}')
    
    # Show first few lines
    with open(md_path, 'r') as f:
        lines = f.readlines()[:10]
        print('📄 File preview:')
        for line in lines:
            print(f'  {line.rstrip()}')

asyncio.run(create_markdown_guide())
"
```

## 🎉 Achievement Summary

### What You've Accomplished

🏆 **File Management System Complete:**
- ✅ Professional directory organization on Desktop
- ✅ Smart filename generation with timestamps
- ✅ Word document creation with MyVision branding
- ✅ Markdown export with metadata headers
- ✅ Complete AI → Document pipeline working

🏆 **Professional Document Features:**
- ✅ **MyVision branding:** Organization name, contact info, professional formatting
- ✅ **Intelligent formatting:** Markdown converted to proper Word styles
- ✅ **Safe file naming:** No overwrites, descriptive names, timestamp uniqueness
- ✅ **Organized storage:** Learning vs Session guides properly categorized

🏆 **Capabilities Gained:**
- ✅ **One-command document creation:** AI content → Professional Word doc
- ✅ **Multiple format support:** Both .docx and .md files
- ✅ **Automatic organization:** Files saved in logical directory structure
- ✅ **Professional presentation:** Ready for trainers and learners

### File System Impact

**What's on your Desktop now:**
```
~/Desktop/MyVision_Guides/
├── Learning_Guides/
│   ├── voiceover_basics_for_beginners_learning_guide_[timestamp].docx
│   ├── iphone_accessibility_basics_learning_guide_[timestamp].docx
│   └── talkback_basics_learning_guide_[timestamp].md
└── Session_Guides/
    └── (ready for future session guides)
```

**Professional Standards Achieved:**
- **Consistent branding:** Every document represents MyVision professionally
- **Trainer-ready:** Documents can be immediately used in training sessions
- **Learner-friendly:** Clear formatting and structure for accessibility
- **Scalable:** System handles unlimited guide creation without conflicts

## 🔧 Troubleshooting Common Issues

### Issue: "Permission denied" when creating files

**Cause:** Insufficient permissions for Desktop access

**Solutions:**
```bash
# 1. Check Desktop permissions
ls -la ~/Desktop/

# 2. Create test file to verify write access
touch ~/Desktop/test_file.txt && rm ~/Desktop/test_file.txt && echo "✅ Write access working"

# 3. Use alternative directory if needed
echo 'MYVISION_OUTPUT_DIR=/Users/$(whoami)/Documents/MyVision_Guides' >> .env
```

### Issue: Word documents won't open

**Cause:** Missing python-docx dependency or corrupted file

**Solutions:**
```bash
# 1. Verify python-docx installation
python3 -c "import docx; print('✅ python-docx working')"

# 2. If not installed
pip3 install python-docx

# 3. Test document creation manually
PYTHONPATH=src python3 -c "
from docx import Document
doc = Document()
doc.add_paragraph('Test')
doc.save('/tmp/test.docx')
print('✅ Word document creation working')
"
```

### Issue: Import errors for file_manager

**Cause:** Module path or import issues

**Solutions:**
```bash
# 1. Verify file exists
ls -la src/myvision_guides/file_manager.py

# 2. Test import
PYTHONPATH=src python3 -c "
from myvision_guides.file_manager import file_manager
print('✅ File manager import working')
"

# 3. Check for syntax errors
python3 -m py_compile src/myvision_guides/file_manager.py
```

### Issue: Filename too long errors

**Cause:** Very long guide titles

**The filename cleaner automatically handles this, but you can test:**
```bash
PYTHONPATH=src python3 -c "
from myvision_guides.file_manager import file_manager

# Test with very long title
long_title = 'This is an extremely long guide title that would normally cause filename problems in most systems'
filename = file_manager.generate_filename(long_title, 'learning', 'docx')
print(f'Long title handled: {filename}')
print(f'Length: {len(filename)} characters')
"
```

## 🚀 Next Steps Preview

With your file management system complete, you're ready for **Step 6: Command-Line Interface**:

**What's Coming Next:**
- 🖥️ Building a user-friendly command-line interface
- 🎨 Adding beautiful terminal output with colors and progress bars
- ⚡ Creating simple commands for guide generation
- 🔧 Implementing error handling and user feedback
- 📋 Adding help system and usage examples

**Files You'll Create in Step 6:**
- `src/myvision_guides/cli.py` - Main command-line interface
- `src/myvision_guides/ui_helpers.py` - Terminal formatting and display

**Commands You'll Build:**
- `myvision-guides generate "VoiceOver basics"` - Quick topic guide
- `myvision-guides session transcript.txt` - Session guide from file
- `myvision-guides list` - Show all created guides
- `myvision-guides --help` - Full help system

**Why This File Foundation Matters:**
Your file management system transforms AI intelligence into professional, trainer-ready documents. The CLI will make this power accessible through simple, intuitive commands.

You now have a **complete AI-to-Document pipeline** that creates professional MyVision learning guides! 

---

**🎯 Learning Objective Achieved:** You can now transform AI-generated content into professional, branded documents with organized file management.

**⭐ Professional Skill Unlocked:** Document automation and file system design - essential for any professional application.

**Ready for Step 6?** Let's build the user interface that makes this powerful system easy to use!

3. **Footer Section:**
   - Organization contact information
   - Professional formatting

## File Safety Features

### Timestamp-Based Uniqueness
Every filename includes a timestamp: `20241215_143022`
- Format: YYYYMMDD_HHMMSS
- Prevents overwriting existing files
- Allows tracking creation order

### Character Sanitization
The `_clean_filename()` method ensures safe filenames:

**Problematic Characters Removed:**
- Special characters: `!@#$%^&*()+=[]{}|;':",.<>?`
- Leading/trailing spaces
- Multiple consecutive spaces

**Safe Transformations:**
- Spaces → underscores
- Multiple underscores → single underscore
- Length limiting (50 characters max)

### Directory Management
```python
def ensure_output_directory(self):
    """Creates directories if they don't exist"""
    self.output_directory.mkdir(exist_ok=True)
    (self.output_directory / "Learning_Guides").mkdir(exist_ok=True)
    (self.output_directory / "Session_Guides").mkdir(exist_ok=True)
```

## Word Document Formatting Details

### Header Creation
```python
def _add_document_header(self, doc, metadata):
    # Title: 18pt, bold, centered
    title_run.font.size = Inches(0.25)
    title_run.bold = True
    
    # Organization: 12pt, centered
    org_run.font.size = Inches(0.17)
    
    # Date: 10pt, centered
    date_run.font.size = Inches(0.13)
```

### Content Parsing
The FileManager includes a simple markdown parser:

**Supported Markdown:**
- `# Heading` → Word Heading 1
- `## Subheading` → Word Heading 2
- `### Sub-subheading` → Word Heading 3
- `- Bullet` → Word Bullet List
- `1. Number` → Word Numbered List
- Regular text → Word Paragraph

### Footer Creation
```python
def _add_document_footer(self, doc):
    footer_text = (f"{config.organization_name} | "
                  f"Email: {config.contact_email}")
    footer_run.font.size = Inches(0.11)  # 8pt
```

## Usage Examples

### Basic Usage
```python
from file_manager import FileManager

# Create file manager
fm = FileManager()

# Generate filename
filename = fm.generate_filename(
    title="iPhone VoiceOver Setup",
    guide_type="learning",
    format_type="docx"
)

# Save as Word document
file_path = fm.save_docx_guide(
    content=guide_content,
    metadata=guide_metadata,
    filename=filename
)

print(f"Guide saved to: {file_path}")
```

### Metadata Structure
```python
metadata = {
    "type": "Learning Guide",
    "title": "VoiceOver Basics - Learning Guide", 
    "topic": "VoiceOver basics",
    "generated": "2024-12-15T14:30:22.123456",
    "client_name": None  # For session guides
}
```

## Error Handling

### Common Issues and Solutions

**1. Permission Errors**
```
PermissionError: [Errno 13] Permission denied
```
**Solution:** Ensure the output directory is writable, close any open files with the same name

**2. Path Too Long**
```
OSError: [Errno 36] File name too long
```
**Solution:** The filename cleaner limits length to 50 characters automatically

**3. Invalid Characters**
```
OSError: [Errno 22] Invalid argument
```
**Solution:** The filename cleaner removes problematic characters automatically

## Configuration Dependencies

The FileManager relies on these config settings:

```python
# From config.py
config.desktop_path = Path.home() / "Desktop"
config.output_directory = config.desktop_path / "MyVision_Guides"
config.organization_name = "MyVision Oxfordshire"
config.contact_email = "info@myvision.org"
```

## File System Impact

### Files Created
- **Guides:** `.md` or `.docx` files in organized folders
- **Directories:** Auto-created folder structure on desktop

### Files Never Modified
- Existing files are never overwritten (timestamp prevents this)
- Original source files remain untouched

### Storage Considerations
- **Markdown files:** ~5-15KB per guide
- **Word documents:** ~25-50KB per guide  
- **Growth rate:** Depends on usage (estimated 10-50 files per month)

## Future Enhancements

### Planned Features
1. **Template System:** Custom Word templates with logos
2. **Client-Specific Folders:** Organize by client name
3. **Export Options:** PDF generation
4. **Bulk Operations:** Process multiple guides at once
5. **Backup System:** Automatic guide backups

### Extensibility Points
- **Custom formatters:** Add new output formats
- **Template engines:** More sophisticated document creation
- **Cloud integration:** Save to Google Drive, OneDrive
- **Version control:** Track guide revisions

## Troubleshooting Guide

### Test FileManager Installation
```bash
python3 -c "from file_manager import FileManager; fm = FileManager(); print('FileManager working!')"
```

### Debug File Creation
```python
# Test filename generation
fm = FileManager()
filename = fm.generate_filename("Test Guide", "learning", "docx")
print(f"Generated filename: {filename}")

# Check output directory
print(f"Output directory: {fm.config.output_directory}")
print(f"Directory exists: {fm.config.output_directory.exists()}")
```

### Verify Dependencies
```bash
python3 -c "import docx; print('python-docx installed')"
python3 -c "from pathlib import Path; print('pathlib available')"
python3 -c "import re; print('regex module available')"
```

## Integration with Other Components

### With GuideGenerator
```python
# Typical workflow
generator = GuideGenerator()
file_manager = FileManager()

# Generate content
guide_data = await generator.generate_topic_guide("VoiceOver basics")

# Create filename
filename = file_manager.generate_filename(
    guide_data["title"], 
    "learning", 
    "docx"
)

# Save file
file_path = file_manager.save_docx_guide(
    guide_data["content"],
    guide_data["metadata"], 
    filename
)
```

### With CLI Interface
The CLI will coordinate between GuideGenerator and FileManager to provide a seamless user experience.

---

*This guide covers the FileManager component of the MyVision Guide Generator CLI tool. For complete system documentation, see the main project README.*