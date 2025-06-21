# MyVision Guide Generator - Complete User Guide
*Your AI-Powered Assistant for Creating Professional Learning Guides*

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Usage](#basic-usage)
3. [Command Reference](#command-reference)
4. [Common Workflows](#common-workflows)
5. [Output Organization](#output-organization)
6. [Tips and Best Practices](#tips-and-best-practices)
7. [Troubleshooting](#troubleshooting)
8. [Integration with MyVision Workflows](#integration-with-myvision-workflows)

## Getting Started

### What is MyVision Guide Generator?

MyVision Guide Generator is your personal AI assistant that creates professional learning guides for assistive technology topics in seconds. Instead of spending 30-60 minutes writing each guide manually, you simply type a command and get a comprehensive, professionally formatted guide ready for client delivery.

### Your First Guide in 3 Steps

**Step 1: Open Terminal**
- Press `Cmd + Space`, type "Terminal", press Enter
- You'll see a black window with text - this is where you'll type commands

**Step 2: Activate Your Environment**
```bash
cd myvision-guide-generator
source venv/bin/activate
```
*You'll see `(venv)` appear at the start of your command line*

**Step 3: Generate Your First Guide**
```bash
myvision guide "VoiceOver basics for beginners"
```
*Watch as the AI streams its thinking process in real-time, then generates your professional guide!*

### What Just Happened?

1. ✅ **Real-Time AI Streaming:** Watch as Claude AI thinks through your topic step-by-step
2. ✅ **Chain-of-Thought Processing:** See the AI's reasoning process as it plans your guide
3. ✅ **Expert Content:** Generated comprehensive learning guide with proper educational structure
4. ✅ **Professional Formatting:** Created Word document with MyVision branding and logo
5. ✅ **Organized Storage:** Saved to `Desktop/MyVision_Guides/Learning_Guides/` with timestamp

### The Real-Time Experience

When you run a guide generation command, you'll see:

```
🤖 AI is analyzing your topic...

💭 Chain of Thought Streaming:
Let me think about creating a comprehensive VoiceOver guide for beginners...

First, I need to consider the user's current knowledge level...
The key concepts they need to understand are...
I should structure this with clear learning objectives...

✨ Now generating your professional guide...

📝 Creating: voiceover_basics_for_beginners_learning_guide_20241215_143022.docx
✅ Guide successfully created and saved to Desktop/MyVision_Guides/Learning_Guides/
```

## Real-Time AI Streaming Features

### Understanding Chain-of-Thought Processing

MyVision Guide Generator uses advanced chain-of-thought streaming, which means you can watch the AI think through your request step-by-step in real-time. This creates a more engaging experience and helps you understand how the AI approaches guide creation.

### What You'll See During Generation

**1. Initial Analysis Phase:**
```
🤖 AI is analyzing your topic...

💭 Chain of Thought Streaming:
Let me think about creating a guide for "VoiceOver basics for beginners"...

I need to consider:
- The user's current knowledge level (complete beginner)
- Essential concepts they must understand first
- Logical progression from simple to complex
- Practical exercises to reinforce learning
```

**2. Planning Phase:**
```
For this guide, I should structure it as:
1. What is VoiceOver and why it matters
2. Basic gestures and navigation
3. Essential settings and customization
4. Practice activities
5. Troubleshooting common issues

Now let me create comprehensive content for each section...
```

**3. Generation Phase:**
```
✨ Now generating your professional guide...

📝 Creating: voiceover_basics_for_beginners_learning_guide_20241215_143022.docx
✅ Guide successfully created and saved to Desktop/MyVision_Guides/Learning_Guides/
```

### Streaming Configuration

By default, chain-of-thought streaming is enabled for the best user experience. You can customize this behavior:

**Environment Configuration (.env file):**
```bash
# Enable/disable streaming
STREAMING_ENABLED=true

# Enable/disable chain-of-thought
CHAIN_OF_THOUGHT_ENABLED=true

# Detail level: minimal, moderate, detailed
CHAIN_OF_THOUGHT_DETAIL_LEVEL=detailed
```

**Benefits of Streaming:**
- ✅ **Transparency:** See exactly how the AI approaches your topic
- ✅ **Engagement:** Stay engaged during the 30-60 second generation process
- ✅ **Learning:** Understand the AI's reasoning for better prompt creation
- ✅ **Trust:** Build confidence in the AI's systematic approach

**When Streaming Helps Most:**
- **Complex Topics:** See how the AI breaks down complicated subjects
- **New Users:** Understand what the AI considers when creating guides
- **Quality Assurance:** Verify the AI is thinking about your specific requirements

## Basic Usage

### Understanding the Command Structure

All commands follow this pattern:
```bash
myvision [COMMAND] [WHAT YOU WANT] [OPTIONS]
```

**Examples:**
```bash
myvision guide "topic here"              # Create a learning guide
myvision guide "topic here" --format md  # Create as markdown instead
myvision list                            # See recent guides
myvision --help                          # Get help
```

### Your Most Common Command

**Creating Topic Guides:**
```bash
myvision guide "TOPIC DESCRIPTION"
```

**Real Examples:**
```bash
myvision guide "VoiceOver rotor navigation"
myvision guide "Setting up JAWS on Windows 11"
myvision guide "iPhone accessibility settings overview"
myvision guide "TalkBack gestures for Android"
myvision guide "ZoomText magnification basics"
```

### Choosing Output Format

**Word Documents (Default - Best for Clients):**
```bash
myvision guide "topic here"
myvision guide "topic here" --format docx
```
*Creates professional Word document with MyVision branding and logo*

**Markdown Files (Best for Technical Users):**
```bash
myvision guide "topic here" --format markdown
```
*Creates lightweight text file, good for version control*

## Command Reference

### Main Commands

#### `myvision guide` - Create Learning Guides

**Purpose:** Generate comprehensive learning guides for assistive technology topics

**Basic Usage:**
```bash
myvision guide "TOPIC DESCRIPTION"
```

**With Options:**
```bash
myvision guide "TOPIC" --format [docx|markdown]
```

**Examples:**
```bash
# Basic guide (creates Word document)
myvision guide "VoiceOver basics"

# Specific format
myvision guide "JAWS keyboard shortcuts" --format markdown

# Complex topics work great
myvision guide "Setting up voice control for motor impairments"

# Mobile accessibility
myvision guide "Android TalkBack navigation for beginners"

# Platform-specific
myvision guide "macOS accessibility features overview"
```

**What You Get:**
- **Learning Objectives:** Clear goals for the user
- **Prerequisites:** What they need to know first
- **Step-by-Step Instructions:** Detailed, numbered steps
- **Practice Activities:** Hands-on exercises
- **Troubleshooting:** Common issues and solutions
- **Next Steps:** What to learn next

#### `myvision list` - View Recent Guides

**Purpose:** See what guides you've created recently

**Basic Usage:**
```bash
myvision list
```

**With Options:**
```bash
myvision list --limit NUMBER
```

**Examples:**
```bash
myvision list                # Show 10 most recent guides
myvision list --limit 5      # Show 5 most recent
myvision list --limit 25     # Show 25 most recent
```

**What You See:**
```
📚 Recent Learning Guides (showing 3):

 1. voiceover_rotor_basics_learning_guide_20241215_143022.docx
     📅 2024-12-15 14:30 | 📄 45,233 bytes

 2. jaws_setup_learning_guide_20241215_142015.md
     📅 2024-12-15 14:20 | 📄 12,456 bytes

 3. iphone_accessibility_learning_guide_20241215_141203.docx
     📅 2024-12-15 14:12 | 📄 52,109 bytes
```

#### Quick Shortcuts

**Pre-defined guides for common topics:**

```bash
myvision voiceover-basics     # VoiceOver fundamentals
myvision jaws-setup          # JAWS installation and setup
```

**With format options:**
```bash
myvision voiceover-basics --format markdown
myvision jaws-setup --format docx
```

#### Accessibility Testing

**Validate accessibility features:**
```bash
myvision accessibility-test                    # Test with Word format
myvision accessibility-test --format markdown  # Test with Markdown format
```

*This generates a comprehensive test document with all accessibility features enabled, perfect for verifying that large print formatting, logo placement, and professional styling are working correctly.*

### Help and Information

```bash
myvision --help              # Main help
myvision guide --help        # Help for guide command
myvision list --help         # Help for list command
myvision --version           # Show version
```

## Common Workflows

### Workflow 1: Pre-Session Preparation

**Scenario:** You have a training session tomorrow about VoiceOver rotor navigation

```bash
# Generate comprehensive guide
myvision guide "VoiceOver rotor navigation for beginners"

# Check it was created
myvision list

# Open it to review (macOS)
open ~/Desktop/MyVision_Guides/Learning_Guides/
```

**Result:** Professional guide ready to:
- Reference during training
- Give to client as takeaway
- Use as session structure

### Workflow 2: Quick Reference Creation

**Scenario:** Client asks about specific JAWS keyboard shortcuts

```bash
# Create quick reference
myvision guide "JAWS essential keyboard shortcuts"

# For faster access, create markdown version too
myvision guide "JAWS essential keyboard shortcuts" --format markdown
```

**Result:** 
- Word doc for client
- Markdown for your quick reference

### Workflow 3: Building Training Series

**Scenario:** Creating multi-session iPhone accessibility training

```bash
# Session 1: Basics
myvision guide "iPhone accessibility settings introduction"

# Session 2: VoiceOver
myvision guide "iPhone VoiceOver navigation basics"

# Session 3: Advanced
myvision guide "iPhone VoiceOver rotor and advanced gestures"

# See your series
myvision list --limit 10
```

**Result:** Complete training series with consistent structure

### Workflow 4: Platform Comparison

**Scenario:** Client switching from Android to iPhone

```bash
# Create transition guide
myvision guide "Switching from Android TalkBack to iPhone VoiceOver"

# Or create separate guides for comparison
myvision guide "Android TalkBack essential gestures"
myvision guide "iPhone VoiceOver essential gestures"
```

### Workflow 5: Troubleshooting Support

**Scenario:** Client having specific issues

```bash
# Targeted troubleshooting guides
myvision guide "VoiceOver not reading webpage content troubleshooting"
myvision guide "JAWS cursor not moving in Microsoft Word solutions"
myvision guide "iPhone VoiceOver gestures not working fixes"
```

## Output Organization

### Where Your Guides Are Saved

**Default Location:**
```
Desktop/MyVision_Guides/
├── Learning_Guides/          # All your topic guides
│   ├── voiceover_basics_learning_guide_20241215_143022.docx
│   ├── jaws_setup_learning_guide_20241215_144033.md
│   └── iphone_accessibility_learning_guide_20241215_145011.docx
└── Session_Guides/           # Future: Personalized session guides
    └── (coming soon)
```

### File Naming System

**Pattern:** `{topic}_{type}_guide_{timestamp}.{format}`

**Examples:**
- `voiceover_rotor_basics_learning_guide_20241215_143022.docx`
- `jaws_keyboard_shortcuts_learning_guide_20241215_144033.md`

**Why This System:**
- **Descriptive:** Easy to find what you need
- **Unique:** Timestamps prevent overwrites
- **Sortable:** Files sort chronologically
- **Professional:** Clean, consistent naming

### Quick Access

**Open guides folder:**
```bash
# macOS
open ~/Desktop/MyVision_Guides/Learning_Guides/

# View in Terminal
ls ~/Desktop/MyVision_Guides/Learning_Guides/
```

**Open recent guide directly:**
```bash
# Find the filename
myvision list

# Open specific file (replace with actual filename)
open ~/Desktop/MyVision_Guides/Learning_Guides/voiceover_basics_learning_guide_20241215_143022.docx
```

## Tips and Best Practices

### Writing Effective Topic Descriptions

**✅ Good Topic Descriptions:**
```bash
myvision guide "VoiceOver rotor navigation for beginners"
myvision guide "Setting up JAWS with Microsoft Word 365"
myvision guide "iPhone VoiceOver gestures for text editing"
myvision guide "Android TalkBack reading controls and navigation"
```

**❌ Avoid These:**
```bash
myvision guide "VoiceOver"           # Too vague
myvision guide "help"                # Not specific
myvision guide "everything about accessibility"  # Too broad
```

**Best Practices:**
- **Be specific:** Include the exact feature or skill
- **Include platform:** "on iPhone", "with JAWS", "in Windows"
- **Specify audience:** "for beginners", "advanced techniques"
- **Use natural language:** Write how you'd explain to a colleague

### Getting the Best Results

**Include Context:**
```bash
# Good - provides context
myvision guide "VoiceOver rotor navigation for reading web pages"

# Better - more specific context
myvision guide "Using VoiceOver rotor to navigate headings and links on websites"
```

**Specify Experience Level:**
```bash
myvision guide "JAWS basics for complete beginners"
myvision guide "Advanced JAWS scripting techniques"
myvision guide "Intermediate VoiceOver shortcuts for power users"
```

**Platform-Specific Topics:**
```bash
myvision guide "Windows 11 Narrator setup and configuration"
myvision guide "macOS Voice Control for motor impairments"
myvision guide "iOS VoiceOver typing and text editing"
```

### Format Selection Strategy

**Use Word Documents (.docx) When:**
- ✅ Giving guides to clients
- ✅ Printing for training sessions
- ✅ Emailing to families
- ✅ Professional presentation needed
- ✅ Includes MyVision branding

**Use Markdown (.md) When:**
- ✅ Quick personal reference
- ✅ Sharing with technical colleagues
- ✅ Version control with git
- ✅ Converting to other formats later
- ✅ Faster file creation

### Organizing Your Guide Library

**Create Topic Collections:**
```bash
# VoiceOver series
myvision guide "VoiceOver basics for beginners"
myvision guide "VoiceOver rotor navigation"
myvision guide "VoiceOver text editing and typing"
myvision guide "VoiceOver web browsing essentials"

# JAWS series
myvision guide "JAWS installation and setup"
myvision guide "JAWS virtual cursor basics"
myvision guide "JAWS with Microsoft Office"
```

**Use Consistent Naming:**
```bash
# Good pattern
myvision guide "iPhone VoiceOver setup"
myvision guide "iPhone VoiceOver navigation"
myvision guide "iPhone VoiceOver text editing"

# Consistent structure helps organization
```

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Command Not Found

**Problem:**
```bash
myvision guide "topic"
# bash: myvision: command not found
```

**Solution:**
```bash
# Activate virtual environment
cd myvision-guide-generator
source venv/bin/activate

# You should see (venv) at start of command line
# Now try again
myvision guide "topic"
```

#### Issue 2: API Key Error

**Problem:**
```bash
myvision guide "topic"
# ❌ ANTHROPIC_API_KEY not found in environment variables
```

**Solution:**
```bash
# Set your API key (replace with your actual key)
export ANTHROPIC_API_KEY="your_actual_api_key_here"

# Or check if .env file exists and has your key
cat .env | grep ANTHROPIC_API_KEY
```

#### Issue 3: No Guides Generated

**Problem:**
```bash
myvision guide "topic"
# Command runs but no file appears
```

**Troubleshooting:**
```bash
# Check if guide was created
myvision list

# Check output directory
ls ~/Desktop/MyVision_Guides/Learning_Guides/

# Look for error messages in the command output
```

#### Issue 4: Generation Takes Too Long

**Problem:** Command runs for several minutes without completing

**Solutions:**
- ✅ **Wait patiently:** Complex topics can take 30-60 seconds
- ✅ **Check internet:** API requires good connection
- ✅ **Try simpler topic:** Break complex topics into smaller parts
- ✅ **Cancel and retry:** Press `Ctrl+C` to cancel, try again

#### Issue 5: Poor Quality Output

**Problem:** Generated guide doesn't meet expectations

**Solutions:**
- ✅ **Be more specific:** Add detail to your topic description
- ✅ **Include context:** Specify platform, audience, experience level
- ✅ **Try different wording:** Rephrase your topic description
- ✅ **Break it down:** Create separate guides for different aspects

### Getting Help

**Built-in Help:**
```bash
myvision --help              # General help
myvision guide --help        # Command-specific help
```

**Check Status:**
```bash
myvision --version           # Confirm installation
myvision list               # See if any guides exist
```

**Environment Check:**
```bash
# Confirm you're in the right directory
pwd
# Should show: /Users/yourname/myvision-guide-generator

# Confirm virtual environment is active
echo $VIRTUAL_ENV
# Should show path to your venv
```

## Integration with MyVision Workflows

### Before Client Sessions

**Preparation Workflow:**
1. **Review client needs:** What assistive technology will you cover?
2. **Generate guides:** Create comprehensive guides for main topics
3. **Print if needed:** Word documents print beautifully
4. **Email preparation:** Have guides ready to email after session

**Example:**
```bash
# Tomorrow's session: VoiceOver basics for new iPhone user
myvision guide "VoiceOver basics for first-time iPhone users"
myvision guide "Essential VoiceOver gestures for daily iPhone use"

# Quick check
myvision list --limit 5
```

### During Training Sessions

**Quick Reference Creation:**
```bash
# Client asks unexpected question
myvision guide "VoiceOver speaking rate adjustment" --format markdown

# Use markdown for quick reference during session
# Create Word version later for client takeaway
```

### After Training Sessions

**Follow-up Materials:**
```bash
# Create personalized follow-up guide
myvision guide "VoiceOver practice exercises for [client name]"

# Or create specific troubleshooting guides based on session
myvision guide "VoiceOver common issues and solutions for new users"
```

### Building Training Libraries

**Systematic Guide Creation:**
```bash
# Create complete training series
myvision guide "Week 1: iPhone VoiceOver introduction"
myvision guide "Week 2: iPhone VoiceOver navigation basics"
myvision guide "Week 3: iPhone VoiceOver text and typing"
myvision guide "Week 4: iPhone VoiceOver apps and email"
```

### Quality Assurance

**Review Process:**
1. **Generate guide:** Use descriptive topic
2. **Review content:** Open Word document, check accuracy
3. **Customize if needed:** Add client-specific notes
4. **Test with client:** Use in actual training
5. **Iterate:** Improve topic descriptions based on results

### Team Collaboration

**Sharing with Colleagues:**
```bash
# Create guides for team use
myvision guide "MyVision training methodology for VoiceOver"
myvision guide "Common VoiceOver troubleshooting for trainers"

# Use consistent naming for team library
myvision guide "Trainer reference: JAWS keyboard shortcuts"
```

### Documentation Standards

**Consistent Topic Formatting:**
```bash
# Use this pattern for organization-wide guides
myvision guide "[Category]: [Specific Topic] for [Audience]"

# Examples:
myvision guide "VoiceOver: Basic navigation for beginners"
myvision guide "JAWS: Setup and configuration for new users"
myvision guide "Magnification: ZoomText basics for low vision"
```

## Advanced Usage

### Batch Guide Creation

**Create Multiple Related Guides:**
```bash
# Complete iPhone accessibility series
myvision guide "iPhone accessibility settings overview"
myvision guide "iPhone VoiceOver basic navigation"
myvision guide "iPhone VoiceOver text editing"
myvision guide "iPhone VoiceOver web browsing"
myvision guide "iPhone magnification and zoom features"
myvision guide "iPhone voice control setup and use"

# Check your work
myvision list --limit 10
```

### Topic Brainstorming

**Common Assistive Technology Topics:**

**Screen Readers:**
- "VoiceOver basic navigation on iPhone"
- "JAWS virtual cursor fundamentals"
- "NVDA browse mode vs focus mode"
- "TalkBack gesture shortcuts for Android"
- "Narrator setup and basic use in Windows 11"

**Magnification:**
- "ZoomText magnification and color enhancement"
- "Windows Magnifier keyboard shortcuts"
- "macOS Zoom features for low vision"
- "iPhone magnification gestures and settings"

**Voice Control:**
- "Dragon NaturallySpeaking basic commands"
- "macOS Voice Control setup and training"
- "Windows Speech Recognition for document editing"

**Mobile Accessibility:**
- "iPhone accessibility settings walkthrough"
- "Android accessibility features overview"
- "Voice assistant setup for blind users"

### Creating Training Curricula

**Structured Learning Paths:**
```bash
# Beginner VoiceOver Course
myvision guide "Course 1: VoiceOver introduction and basic concepts"
myvision guide "Course 2: VoiceOver essential gestures and navigation"
myvision guide "Course 3: VoiceOver text reading and editing"
myvision guide "Course 4: VoiceOver web browsing and internet"
myvision guide "Course 5: VoiceOver apps and email management"
```

## Summary

### What You've Learned

✅ **Basic Commands:** Generate guides with `myvision guide "topic"`  
✅ **Format Options:** Choose between Word docs and markdown  
✅ **File Organization:** Find guides in organized desktop folders  
✅ **Best Practices:** Write effective topic descriptions  
✅ **Troubleshooting:** Solve common issues independently  
✅ **Workflow Integration:** Use tool effectively in MyVision work  

### Your Daily Workflow

**Morning Preparation:**
```bash
cd myvision-guide-generator
source venv/bin/activate
```

**Throughout the Day:**
```bash
myvision guide "specific topic for today's session"
myvision list  # Check recent work
```

**Quick Quality Check:**
- Open generated guide in Word
- Verify content accuracy and completeness
- Customize with any client-specific notes

### Getting Maximum Value

1. **Be Specific:** Detailed topics create better guides
2. **Use Consistently:** Make it part of your daily routine
3. **Review and Iterate:** Improve topic descriptions based on results
4. **Share Knowledge:** Help colleagues learn the tool
5. **Stay Updated:** Check for new features and improvements

---

*This tool transforms your guide creation process from hours to seconds, giving you more time for direct client interaction while maintaining professional quality documentation. Happy guide generating!* 🎉