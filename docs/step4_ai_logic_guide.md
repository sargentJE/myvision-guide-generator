# Step 4: Building Your AI Brain - Complete Beginner Guide
*Creating the Intelligence That Powers Your Guide Generator - Zero Experience Required*

## 🎯 What You'll Accomplish in Step 4

By the end of this guide, you will have:
- ✅ Created a complete AI service that connects to Claude
- ✅ Built intelligent prompt engineering for assistive technology guides
- ✅ Implemented your first AI-powered guide generator
- ✅ Tested the AI integration with real examples
- ✅ Set up your Claude API key securely

**Time Investment:** 25-30 minutes of AI magic
**Next Step Preview:** Building the file management system for organized output

## 🔍 Pre-flight Check

Before starting, verify you have:
- ✅ Completed Step 3 (Foundation Files)
- ✅ Package importing correctly: `import myvision_guides` works
- ✅ Configuration loading: `from myvision_guides.config import config` works
- ✅ Virtual environment activated (you see `(venv)` in your Terminal prompt)

**To verify you're ready:**
```bash
# Quick foundation test
PYTHONPATH=src python3 -c "
from myvision_guides.config import config
print('✅ Config working:', config.organization_name)
print('✅ API key configured:', 'Yes' if config.anthropic_api_key != 'your_api_key_here' else 'No (need real key)')
"
```

**If configuration test fails:** Go back to Step 3 and complete the foundation setup first.

## 🤔 Why AI Integration Matters

### The Transformation Process

Think of your AI service like **a brilliant assistant trainer:**

**Before AI (Manual Process):**
```
You: "I need a VoiceOver guide"
Process: Research → Plan → Write → Format → Review
Time: 2-3 hours of focused work
Result: One guide, significant time investment
```

**After AI (Automated Intelligence):**
```
You: "I need a VoiceOver guide"  
AI: Instant expertise → Professional structure → Complete guide
Time: 30 seconds to 2 minutes
Result: Professional guide, ready for learners
```

**The Magic Behind the Scenes:**
```
Your Input: "VoiceOver basics"
         ↓
AI Service: Analyzes topic
         ↓
Expert Prompts: "You are a skilled MyVision trainer with 15+ years experience..."
         ↓
Claude AI: Generates professional learning guide
         ↓
Your Output: Complete Word document ready for printing
```

## 📚 Understanding AI Service Architecture

### Your AI Service Components

**File Structure We'll Create:**
```
src/myvision_guides/
├── __init__.py           ← Already created ✅
├── config.py             ← Already created ✅
├── ai_service.py         ← AI brain (we'll create this)
└── prompts.py            ← Expert knowledge templates (we'll create this)
```

**Component Responsibilities:**
- **ai_service.py:** Connects to Claude, manages API calls, handles errors
- **prompts.py:** Contains expert trainer knowledge and guide templates

### The AI Pipeline Explained

```
Step 1: Topic Analysis
"VoiceOver basics" → Detect: iOS screen reader, beginner level

Step 2: Prompt Engineering  
Base knowledge + Topic specifics + MyVision methodology

Step 3: AI Generation (Real-Time Streaming)
Send expert prompt to Claude → Stream response in real-time → User sees content as it's generated

Step 4: Response Processing
Validate content → Structure for Word document → Return result
```

**Enhanced User Experience with Real-Time Streaming:**

The modern implementation includes advanced streaming capabilities that transform the user experience:

**Traditional AI Generation:**
```
User: "Generate VoiceOver guide"
System: "Processing..." (30 seconds of silence)
System: "Done! Guide created."
```

**Streaming AI Generation:**
```
User: "Generate VoiceOver guide"
System: 🤖 "AI is analyzing your topic..."

💭 Chain of Thought Streaming:
"Let me think about VoiceOver basics for beginners...
I need to consider the user's knowledge level...
The key concepts they need to understand are..."

✨ Now generating your professional guide...

# VoiceOver Basics for Beginners
## Learning Objectives
By completing this guide, you will...
(content appears in real-time as AI writes it)
```

**Streaming Benefits:**
- ✅ **Immediate Engagement:** Users see progress immediately
- ✅ **Perceived Performance:** Feels much faster than waiting in silence
- ✅ **Transparency:** Users understand how AI approaches the topic
- ✅ **Trust Building:** Seeing the reasoning process builds confidence
- ✅ **Educational Value:** Users learn from the AI's systematic approach

## 🛠️ Step-by-Step AI Service Creation

### Step 1: Get Your Claude API Key

**Why you need an API key:**
Your API key is like a membership card that lets your app talk to Claude AI.

**Get your API key:**
1. **Visit:** [console.anthropic.com](https://console.anthropic.com/)
2. **Sign up/Log in** with your email
3. **Go to API Keys** (in the left sidebar)
4. **Create Key** → Give it a name like "MyVision Guide Generator"
5. **Copy the key** (starts with `sk-ant-...`)

**Add to your .env file:**
```bash
# Open your .env file
code .env
```

**Replace the placeholder with your real key:**
```bash
# Replace this line:
ANTHROPIC_API_KEY=your_api_key_here

# With your actual key:
ANTHROPIC_API_KEY=sk-ant-api03-your-actual-key-here
```

**Save the file** (`Cmd+S`)

**Test your API key:**
```bash
PYTHONPATH=src python3 -c "
from myvision_guides.config import config
print('API key length:', len(config.anthropic_api_key))
print('API key starts correctly:', config.anthropic_api_key.startswith('sk-ant-'))
"
```

### Step 2: Create prompts.py (Expert Knowledge Templates)

**What this file does:**
Contains all the expert trainer knowledge that makes Claude generate professional, empathetic assistive technology guides.

**Create the file:**
```bash
touch src/myvision_guides/prompts.py
code src/myvision_guides/prompts.py
```

**Add this expert knowledge system:**
```python
"""
Expert prompt engineering for assistive technology learning guides

This module contains the specialized knowledge and teaching methodology
that transforms Claude into a skilled MyVision trainer.
"""

# Core system prompt that defines Claude's expertise and personality
SYSTEM_PROMPT = """
You are an expert assistive technology trainer at MyVision Oxfordshire 
with 15+ years of experience helping people with visual impairments and other disabilities.

Your expertise includes:
- Screen readers: VoiceOver (iOS/macOS), JAWS (Windows), NVDA (Windows), TalkBack (Android)
- Magnification tools: ZoomText, built-in OS magnification, hardware magnifiers  
- Voice control: Dragon NaturallySpeaking, built-in voice commands
- Switch navigation and alternative input methods
- Mobile accessibility: iPhone, iPad, Android accessibility features
- Desktop accessibility: Windows, macOS, Linux accessibility settings

Your teaching philosophy:
- Start with empathy and encouragement
- Break complex concepts into manageable, sequential steps  
- Use clear, jargon-free language with explanations of technical terms
- Provide context for why each step matters to the user's independence
- Include practical tips from real-world experience
- Address common concerns and emotional aspects of learning new technology
- End with confidence-building next steps and resources

Your communication style:
- Warm, supportive, and patient tone
- Person-first language (person with visual impairment, not "blind person")
- Acknowledge the learning curve and celebrate small wins
- Include practical wisdom about when to ask for help
- Reference the broader assistive technology ecosystem

Your goal is to create learning guides that empower independence, 
build confidence, and provide practical skills for daily life with assistive technology.
"""

def create_topic_prompt(topic: str) -> str:
    """
    Create a specialized prompt for generating a topic-based learning guide.
    
    Args:
        topic: The assistive technology topic to create a guide for
        
    Returns:
        Complete prompt ready for Claude API
    """
    return f"""
Create a comprehensive learning guide for: "{topic}"

Please structure your response as a complete learning guide with these sections:

# [Topic Title] - Learning Guide

## Learning Objectives
- Clear, specific goals the learner will achieve
- Written in "By the end of this guide, you will be able to..." format

## Prerequisites
- What the learner should know or have ready before starting
- Any required equipment, settings, or setup

## Why This Matters
- Real-world benefits and independence this skill provides
- Personal empowerment aspects
- Connection to daily life activities

## Step-by-Step Instructions
- Numbered steps with clear, specific actions
- Include what the user will hear, see, or feel at each step
- Provide alternative approaches when helpful
- Add encouragement throughout the process

## Practice Activities
- Hands-on exercises to reinforce learning
- Progressive difficulty to build confidence
- Real-world scenarios to practice

## Troubleshooting
- Common challenges learners face
- Clear solutions and workarounds
- When and how to get additional help

## Next Steps
- Natural progression to related skills
- Additional resources and learning opportunities
- Confidence-building achievements to celebrate

Remember to:
- Use encouraging, supportive language throughout
- Explain technical terms when first introduced
- Include realistic time estimates for activities
- Address common emotional aspects of learning assistive technology
- Provide practical tips from your years of training experience

The guide should be comprehensive enough to support independent learning 
while maintaining an encouraging tone that builds confidence.
"""

def create_session_prompt(transcript: str) -> str:
    """
    Create a specialized prompt for generating a guide from training session transcript.
    
    Args:
        transcript: Text of the training session conversation
        
    Returns:
        Complete prompt ready for Claude API
    """
    return f"""
Analyze this training session transcript and create a personalized learning guide 
based on what was covered and the learner's specific needs:

TRAINING SESSION TRANSCRIPT:
{transcript}

Please create a personalized learning guide with these sections:

# Personalized Learning Guide - [Date]

## Session Overview
- Brief summary of what was covered
- Key skills or concepts that were the focus
- Learner's starting point and progress made

## Key Learning Points
- Main concepts or skills covered in the session
- Important discoveries or "aha moments" from the learner
- Specific techniques or approaches that worked well

## Step-by-Step Review
- Recreate the successful steps from the session
- Include specific details about what worked
- Note any modifications or personal adaptations discovered

## Reinforcement Activities
- Practice exercises based on what was covered
- Ways to build on the session's successes
- Activities to strengthen the skills practiced

## Addressing Challenges
- Any difficulties encountered during the session
- Strategies that helped overcome challenges
- Alternative approaches to try if problems persist

## Personal Notes
- Specific preferences or adaptations noted for this learner
- Equipment or settings that work particularly well
- Individual learning style considerations

## Next Session Goals
- Natural next steps based on current progress
- Skills to build on from this foundation
- Specific goals for continued learning

Remember to:
- Maintain the encouraging tone from the session
- Preserve any personal insights or breakthroughs
- Include specific details that make this guide unique to this learner
- Focus on building confidence and celebrating progress
- Provide clear next steps for continued growth

Create a guide that captures the personalized nature of the training 
while providing a clear reference for continued practice and learning.
"""

# Technology-specific knowledge for enhanced prompts
TECHNOLOGY_KNOWLEDGE = {
    "voiceover": {
        "platform": "iOS/macOS",
        "key_gestures": "Single finger swipe, double tap, rotor, magic tap",
        "common_challenges": "Gesture timing, rotor navigation, web browsing",
        "beginner_focus": "Basic navigation, reading text, making calls"
    },
    "jaws": {
        "platform": "Windows",
        "key_commands": "Insert key combinations, virtual cursor, forms mode",
        "common_challenges": "Virtual vs. PC cursor, browser compatibility",
        "beginner_focus": "Basic navigation, reading documents, email"
    },
    "nvda": {
        "platform": "Windows", 
        "key_commands": "NVDA key combinations, browse mode, focus mode",
        "common_challenges": "Mode switching, add-on configuration",
        "beginner_focus": "Basic navigation, web browsing, text editing"
    },
    "talkback": {
        "platform": "Android",
        "key_gestures": "Explore by touch, swipe navigation, global gestures",
        "common_challenges": "Gesture conflicts with apps, settings navigation",
        "beginner_focus": "Basic navigation, making calls, texting"
    },
    "magnification": {
        "platform": "Cross-platform",
        "key_features": "Zoom levels, color contrast, cursor tracking",
        "common_challenges": "Optimal zoom levels, tracking moving content",
        "beginner_focus": "Basic zoom, contrast adjustment, reading text"
    }
}

def enhance_prompt_for_technology(base_prompt: str, topic: str) -> str:
    """
    Enhance a base prompt with technology-specific knowledge.
    
    Args:
        base_prompt: The base prompt to enhance
        topic: The topic to analyze for technology keywords
        
    Returns:
        Enhanced prompt with specific technology insights
    """
    topic_lower = topic.lower()
    
    # Find matching technology
    for tech_key, tech_info in TECHNOLOGY_KNOWLEDGE.items():
        if tech_key in topic_lower:
            enhancement = f"""

Additional context for {tech_info['platform']} {tech_key.upper()}:
- Key features: {tech_info.get('key_gestures', tech_info.get('key_commands', tech_info.get('key_features', 'N/A')))}
- Common challenges: {tech_info['common_challenges']}
- Beginner focus areas: {tech_info['beginner_focus']}

Please incorporate this specific knowledge into your guide creation.
"""
            return base_prompt + enhancement
    
    return base_prompt
```

### Step 3: Create ai_service.py (The AI Brain)

**What this file does:**
- Connects securely to Claude API
- Sends expert prompts and receives professional guides
- Handles errors gracefully (network issues, API problems)
- Processes AI responses into structured content

**Create the file:**
```bash
touch src/myvision_guides/ai_service.py
code src/myvision_guides/ai_service.py
```

**Add this complete AI service:**
```python
"""
AI Service for MyVision Guide Generator

This module handles all AI integration, including:
- Secure connection to Anthropic Claude API
- Expert prompt engineering for assistive technology
- Response processing and validation
- Error handling and retry logic
"""

import asyncio
from typing import Dict, Any, Optional
from anthropic import Anthropic
from anthropic.types import Message

from .config import config
from .prompts import (
    SYSTEM_PROMPT,
    create_topic_prompt,
    create_session_prompt,
    enhance_prompt_for_technology
)


class AIServiceError(Exception):
    """Raised when AI service encounters an error"""
    pass


class GuideGenerator:
    """
    Handles AI-powered generation of assistive technology learning guides.
    
    This class manages the connection to Claude AI and transforms user input
    into professional, empathetic learning guides following MyVision's
    teaching methodology.
    """
    
    def __init__(self):
        """Initialize the AI service with Claude client"""
        try:
            self.client = Anthropic(api_key=config.anthropic_api_key)
            self.system_prompt = SYSTEM_PROMPT
            
            # API configuration from config
            self.model = config.default_model
            self.max_tokens = config.max_tokens
            self.temperature = getattr(config, 'temperature', 0.2)
            
        except Exception as e:
            raise AIServiceError(f"Failed to initialize AI service: {e}")
    
    async def generate_topic_guide(self, topic: str) -> Dict[str, Any]:
        """
        Generate a comprehensive learning guide for a specific topic.
        
        Args:
            topic: The assistive technology topic to create a guide for
                  (e.g., "VoiceOver basics", "JAWS web browsing")
        
        Returns:
            Dictionary containing:
            - content: The generated guide text
            - topic: The original topic
            - guide_type: "topic"
            - metadata: Additional information about the generation
        
        Raises:
            AIServiceError: If guide generation fails
        """
        try:
            # Create and enhance the prompt
            base_prompt = create_topic_prompt(topic)
            enhanced_prompt = enhance_prompt_for_technology(base_prompt, topic)
            
            # Generate the guide
            response = await self._make_api_call(enhanced_prompt)
            
            # Process the response
            guide_content = self._extract_content(response)
            
            return {
                "content": guide_content,
                "topic": topic,
                "guide_type": "topic",
                "metadata": {
                    "model": self.model,
                    "tokens_used": getattr(response.usage, 'input_tokens', 0) + getattr(response.usage, 'output_tokens', 0),
                    "generation_successful": True
                }
            }
        
        except Exception as e:
            raise AIServiceError(f"Failed to generate topic guide for '{topic}': {e}")
    
    async def generate_session_guide(self, transcript: str, session_date: str = None) -> Dict[str, Any]:
        """
        Generate a personalized learning guide from a training session transcript.
        
        Args:
            transcript: Text of the training session conversation
            session_date: Optional date of the session for metadata
        
        Returns:
            Dictionary containing:
            - content: The generated personalized guide
            - transcript: The original transcript (truncated for privacy)
            - guide_type: "session" 
            - metadata: Additional information about the generation
        
        Raises:
            AIServiceError: If guide generation fails
        """
        try:
            # Create the session prompt
            session_prompt = create_session_prompt(transcript)
            
            # Generate the guide
            response = await self._make_api_call(session_prompt)
            
            # Process the response
            guide_content = self._extract_content(response)
            
            return {
                "content": guide_content,
                "transcript": transcript[:200] + "..." if len(transcript) > 200 else transcript,
                "guide_type": "session",
                "session_date": session_date,
                "metadata": {
                    "model": self.model,
                    "tokens_used": getattr(response.usage, 'input_tokens', 0) + getattr(response.usage, 'output_tokens', 0),
                    "generation_successful": True
                }
            }
        
        except Exception as e:
            raise AIServiceError(f"Failed to generate session guide: {e}")
    
    async def _make_api_call(self, prompt: str, max_retries: int = 3) -> Message:
        """
        Make a robust API call to Claude with error handling and retries.
        
        Args:
            prompt: The user prompt to send to Claude
            max_retries: Maximum number of retry attempts
        
        Returns:
            Claude API response message
        
        Raises:
            AIServiceError: If all retries fail
        """
        last_error = None
        
        for attempt in range(max_retries):
            try:
                # Use asyncio.to_thread to make the synchronous API call non-blocking
                response = await asyncio.to_thread(
                    self.client.messages.create,
                    model=self.model,
                    max_tokens=self.max_tokens,
                    temperature=self.temperature,
                    system=self.system_prompt,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
                
                return response
                
            except Exception as e:
                last_error = e
                
                # Check if this is a retryable error
                if attempt < max_retries - 1 and self._is_retryable_error(e):
                    # Wait before retrying (exponential backoff)
                    wait_time = min(2 ** attempt, 30)  # Max 30 seconds
                    await asyncio.sleep(wait_time)
                    continue
                else:
                    # Don't retry for certain error types
                    break
        
        # If we get here, all retries failed
        raise AIServiceError(f"API call failed after {max_retries} attempts: {last_error}")
    
    def _is_retryable_error(self, error: Exception) -> bool:
        """
        Determine if an error is worth retrying.
        
        Args:
            error: The exception that occurred
        
        Returns:
            True if the error is retryable, False otherwise
        """
        error_str = str(error).lower()
        
        # Retryable errors (network, rate limiting, temporary issues)
        retryable_indicators = [
            "rate limit",
            "timeout", 
            "connection",
            "network",
            "temporary",
            "503",  # Service unavailable
            "502",  # Bad gateway
            "500"   # Internal server error
        ]
        
        return any(indicator in error_str for indicator in retryable_indicators)
    
    def _extract_content(self, response: Message) -> str:
        """
        Extract the text content from Claude's response.
        
        Args:
            response: Claude API response message
        
        Returns:
            The generated guide content as a string
        
        Raises:
            AIServiceError: If content extraction fails
        """
        try:
            if hasattr(response, 'content') and len(response.content) > 0:
                # Claude returns content as a list of content blocks
                content_block = response.content[0]
                if hasattr(content_block, 'text'):
                    return content_block.text
                else:
                    return str(content_block)
            else:
                raise AIServiceError("No content in API response")
                
        except Exception as e:
            raise AIServiceError(f"Failed to extract content from response: {e}")
    
    async def test_connection(self) -> Dict[str, Any]:
        """
        Test the connection to Claude API with a simple request.
        
        Returns:
            Dictionary with test results
        """
        try:
            test_prompt = "Please respond with: 'AI connection successful for MyVision Guide Generator'"
            response = await self._make_api_call(test_prompt)
            content = self._extract_content(response)
            
            return {
                "success": True,
                "response": content,
                "model": self.model,
                "message": "AI service is working correctly"
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "AI service connection failed"
            }


# Create a global instance for easy importing
ai_service = GuideGenerator()
```

## ✅ Testing Your AI Integration

### Test 1: API Connection

**Test your Claude connection:**
```bash
PYTHONPATH=src python3 -c "
import asyncio
from myvision_guides.ai_service import ai_service

async def test_connection():
    result = await ai_service.test_connection()
    if result['success']:
        print('✅ AI Connection successful!')
        print('Response:', result['response'][:100], '...')
    else:
        print('❌ AI Connection failed:', result['error'])

asyncio.run(test_connection())
"
```

### Test 2: Generate Your First Guide

**Create a VoiceOver basics guide:**
```bash
PYTHONPATH=src python3 -c "
import asyncio
from myvision_guides.ai_service import ai_service

async def test_guide_generation():
    print('🔄 Generating VoiceOver basics guide...')
    try:
        result = await ai_service.generate_topic_guide('VoiceOver basics')
        print('✅ Guide generated successfully!')
        print('Topic:', result['topic'])
        print('Type:', result['guide_type'])
        print('Content preview:', result['content'][:200], '...')
        print('Tokens used:', result['metadata']['tokens_used'])
    except Exception as e:
        print('❌ Guide generation failed:', e)

asyncio.run(test_guide_generation())
"
```

### Test 3: Session Guide Generation

**Test with sample transcript:**
```bash
PYTHONPATH=src python3 -c "
import asyncio
from myvision_guides.ai_service import ai_service

async def test_session_guide():
    sample_transcript = '''
    Trainer: Today we'll work on VoiceOver gestures on your iPhone.
    Sarah: I'm excited but nervous about learning the swipe gestures.
    Trainer: Let's start with the basic single finger swipe right to move to the next item.
    Sarah: Oh wow, I can hear it reading each app name as I swipe!
    Trainer: Exactly! And double tap to open the app you want.
    Sarah: This is amazing - I had no idea it could be this straightforward.
    '''
    
    print('🔄 Generating personalized session guide...')
    try:
        result = await ai_service.generate_session_guide(sample_transcript)
        print('✅ Session guide generated successfully!')
        print('Type:', result['guide_type'])
        print('Content preview:', result['content'][:200], '...')
    except Exception as e:
        print('❌ Session guide generation failed:', e)

asyncio.run(test_session_guide())
"
```

## 🎉 Achievement Summary

### What You've Accomplished

🏆 **AI Integration Complete:**
- ✅ Claude API connected and tested
- ✅ Expert prompt engineering system created
- ✅ Professional guide generation working
- ✅ Error handling and retry logic implemented
- ✅ Both topic and session guide types supported

🏆 **Files Created:**
- ✅ `prompts.py` - Expert knowledge and teaching methodology
- ✅ `ai_service.py` - Complete AI integration with Claude

🏆 **Capabilities Gained:**
- ✅ **Generate topic guides:** "VoiceOver basics" → Professional learning guide
- ✅ **Create session guides:** Training transcript → Personalized guide
- ✅ **Handle errors gracefully:** Network issues, API problems managed
- ✅ **Async operations:** Non-blocking AI generation for responsive UI

### Professional Standards Achieved

🎯 **AI Engineering Best Practices:**
- **Security:** API keys managed through environment variables
- **Reliability:** Robust error handling with retry logic  
- **Performance:** Asynchronous operations prevent UI blocking
- **Maintainability:** Modular design with separated concerns
- **Quality:** Expert prompt engineering for consistent output

🎯 **Educational Excellence:**
- **Empathetic AI:** Claude trained with MyVision's supportive methodology
- **Adaptive Intelligence:** Technology-specific knowledge enhancement
- **Personalization:** Session transcripts become individualized guides
- **Professional Output:** Structured content ready for document creation

## 🔧 Troubleshooting Common Issues

### Issue: "Invalid API key" or Authentication Errors

**Cause:** API key not properly configured

**Solutions:**
```bash
# 1. Check API key in .env file
cat .env | grep ANTHROPIC_API_KEY

# 2. Verify key format (should start with sk-ant-)
PYTHONPATH=src python3 -c "
from myvision_guides.config import config
print('Key starts correctly:', config.anthropic_api_key.startswith('sk-ant-'))
print('Key length:', len(config.anthropic_api_key))
"

# 3. Test key directly
curl -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     https://api.anthropic.com/v1/messages
```

### Issue: "Module not found" Errors

**Cause:** Python can't find your modules

**Solutions:**
```bash
# 1. Ensure you're in project root
pwd  # Should show: .../myvision-guide-generator

# 2. Check PYTHONPATH
echo $PYTHONPATH

# 3. Add src to path and test
export PYTHONPATH="${PYTHONPATH}:${PWD}/src"
python3 -c "from myvision_guides.ai_service import ai_service; print('✅ Import works')"
```

### Issue: Network or Connection Errors

**Cause:** Internet connectivity or API service issues

**Diagnostic steps:**
```bash
# 1. Test internet connectivity
ping -c 3 api.anthropic.com

# 2. Check if API is accessible
curl -s -I https://api.anthropic.com/v1/messages | head -1

# 3. Test with simple request
PYTHONPATH=src python3 -c "
import asyncio
from myvision_guides.ai_service import ai_service

async def test():
    result = await ai_service.test_connection()
    print('Connection test:', 'Success' if result['success'] else 'Failed')
    if not result['success']:
        print('Error:', result['error'])

asyncio.run(test())
"
```

### Issue: Slow Response Times

**Cause:** Large prompts or API rate limiting

**Solutions:**
```bash
# 1. Check token usage in responses
# (The test scripts above show token usage)

# 2. Reduce max_tokens if needed
echo 'MYVISION_MAX_TOKENS=2000' >> .env

# 3. Use faster model for testing
echo 'MYVISION_MODEL=claude-3-haiku-20240307' >> .env
```

## 🚀 Next Steps Preview

With your AI brain working, you're ready for **Step 5: File Management System**:

**What's Coming Next:**
- 📁 Creating organized file management
- 📄 Converting AI text to professional Word documents  
- 🎨 Adding MyVision branding and formatting
- 📅 Implementing smart file naming and organization
- 🔍 Building a guide library system

**Files You'll Create in Step 5:**
- `src/myvision_guides/file_manager.py` - Document creation and organization
- `src/myvision_guides/document_formatter.py` - Word document styling

**Why This AI Foundation Matters:**
Your AI service provides the intelligence, but the file manager transforms that intelligence into professional, branded documents that trainers can immediately use with learners.

You now have a **working AI brain** that can generate professional assistive technology guides! 

---

**🎯 Learning Objective Achieved:** You can now generate professional, empathetic learning guides using AI, with robust error handling and expert prompt engineering.

**⭐ Professional Skill Unlocked:** AI integration and prompt engineering - the future of content creation automation.

**Ready for Step 5?** Let's turn your AI intelligence into beautiful, professional documents!

### API Client Setup and Configuration

**Basic Client Initialization:**
```python
from anthropic import Anthropic

class GuideGenerator:
    def __init__(self):
        """Initialize Claude client with configuration"""
        self.client = Anthropic(api_key=config.anthropic_api_key)
        
        # Configure default parameters
        self.default_model = config.default_model
        self.max_tokens = config.max_tokens
        self.temperature = config.temperature
```

**Advanced Client Configuration:**
```python
from anthropic import Anthropic
import httpx

class GuideGenerator:
    def __init__(self):
        """Initialize with custom HTTP client and settings"""
        
        # Custom HTTP client with timeout and retries
        http_client = httpx.Client(
            timeout=config.api_timeout,
            limits=httpx.Limits(max_connections=5, max_keepalive_connections=2)
        )
        
        self.client = Anthropic(
            api_key=config.anthropic_api_key,
            http_client=http_client,
            max_retries=config.max_retries
        )
```

### API Request Structure

**Claude Messages API Format:**
```python
response = await asyncio.to_thread(
    self.client.messages.create,
    model="claude-3-sonnet-20241022",
    max_tokens=3000,
    temperature=0.2,
    system="You are an expert assistive technology trainer...",
    messages=[
        {
            "role": "user",
            "content": "Create a guide for VoiceOver basics"
        }
    ]
)
```

**Parameter Explanations:**
- **model:** Which Claude model to use (sonnet for quality, haiku for speed)
- **max_tokens:** Maximum response length (3000 = ~2000 words)
- **temperature:** Creativity vs consistency (0.2 = very consistent)
- **system:** AI's role and expertise definition
- **messages:** Conversation history (user input, AI responses)

### Rate Limiting and Error Handling

**API Error Types:**
```python
from anthropic import (
    APIError,
    APIConnectionError,
    RateLimitError,
    AuthenticationError,
    BadRequestError
)

async def robust_api_call(self, prompt: str):
    """API call with comprehensive error handling"""
    
    for attempt in range(config.max_retries):
        try:
            response = await asyncio.to_thread(
                self.client.messages.create,
                model=self.default_model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=self.system_prompt,
                messages=[{"role": "user", "content": prompt}]
            )
            return response
            
        except RateLimitError as e:
            # Wait and retry for rate limits
            wait_time = min(2 ** attempt, 60)  # Exponential backoff
            await asyncio.sleep(wait_time)
            continue
            
        except AuthenticationError:
            # API key issues - don't retry
            raise APIError("Invalid API key. Please check your ANTHROPIC_API_KEY.")
            
        except APIConnectionError:
            # Network issues - retry with backoff
            if attempt < config.max_retries - 1:
                await asyncio.sleep(2 ** attempt)
                continue
            raise APIError("Network connection failed after retries.")
            
        except BadRequestError as e:
            # Request format issues - don't retry
            raise APIError(f"Invalid request: {e}")
            
        except Exception as e:
            # Unexpected errors
            raise APIError(f"Unexpected API error: {e}")
    
    raise APIError("API request failed after all retries.")
```

## Prompt Engineering for Educational Content

### System Prompt Design

**The Foundation System Prompt:**
```python
self.system_prompt = """
You are an expert assistive technology trainer at MyVision Oxfordshire 
with 15+ years of experience helping people with visual impairments and other disabilities.

Your expertise includes:
- Screen readers: VoiceOver (iOS/macOS), JAWS (Windows), NVDA (Windows), TalkBack (Android)
- Magnification tools: ZoomText, built-in OS magnification, hardware magnifiers
- Voice control: Dragon NaturallySpeaking, built-in voice commands
- Switch navigation and alternative input methods
- Mobile accessibility: iPhone, iPad, Android accessibility features
- Desktop accessibility: Windows, macOS, Linux accessibility settings

Your teaching philosophy:
- Start with empathy and encouragement
- Break complex concepts into manageable, sequential steps
- Use clear, jargon-free language with explanations of technical terms
- Provide context for why each step matters to the user's independence
- Include practical tips from real-world experience
- Address common concerns and emotional aspects of learning new technology
- End with confidence-building next steps and resources

Your communication style:
- Warm, supportive, and patient tone
- Person-first language (person with visual impairment, not "blind person")
- Acknowledge the learning curve and celebrate small wins
- Include practical wisdom about when to ask for help
- Reference the broader assistive technology ecosystem

Your goal is to create learning guides that empower independence, 
build confidence, and provide practical skills for daily life with assistive technology.
"""
```

**Why This System Prompt Works:**
- **Establishes expertise:** Claude adopts the knowledge of an experienced trainer
- **Defines methodology:** Incorporates MyVision's teaching philosophy
- **Sets tone:** Ensures empathetic, supportive language
- **Specifies scope:** Covers relevant assistive technologies
- **Guides structure:** Implies the educational format to follow

### Dynamic Prompt Engineering

**Topic Analysis and Prompt Customization:**
```python
def _analyze_topic(self, topic: str) -> Dict[str, str]:
    """
    Analyze topic to extract key components for prompt customization.
    
    Args:
        topic: User-provided topic string
        
    Returns:
        Dictionary with analyzed components
    """
    topic_lower = topic.lower()
    
    # Detect assistive technology
    technology = "assistive technology"
    if "voiceover" in topic_lower:
        technology = "VoiceOver"
    elif "jaws" in topic_lower:
        technology = "JAWS"
    elif "nvda" in topic_lower:
        technology = "NVDA"
    elif "talkback" in topic_lower:
        technology = "TalkBack"
    elif "dragon" in topic_lower:
        technology = "Dragon NaturallySpeaking"
    elif "magnif" in topic_lower or "zoom" in topic_lower:
        technology = "Screen Magnification"
    elif "voice control" in topic_lower:
        technology = "Voice Control"
    
    # Detect platform/device
    device = "device"
    if "mac" in topic_lower or "macos" in topic_lower:
        device = "Mac"
    elif "iphone" in topic_lower or "ios" in topic_lower:
        device = "iPhone"
    elif "ipad" in topic_lower:
        device = "iPad"
    elif "windows" in topic_lower or "pc" in topic_lower:
        device = "Windows"
    elif "android" in topic_lower:
        device = "Android"
    elif "linux" in topic_lower:
        device = "Linux"
    
    # Determine experience level
    experience_level = "beginner to intermediate"
    if "basic" in topic_lower or "beginner" in topic_lower or "introduction" in topic_lower:
        experience_level = "beginner"
    elif "advanced" in topic_lower or "expert" in topic_lower:
        experience_level = "advanced"
    elif "intermediate" in topic_lower:
        experience_level = "intermediate"
    
    # Detect guide type
    guide_type = "general learning guide"
    if "setup" in topic_lower or "install" in topic_lower:
        guide_type = "setup and installation guide"
    elif "troubleshoot" in topic_lower or "problem" in topic_lower:
        guide_type = "troubleshooting guide"
    elif "shortcut" in topic_lower or "command" in topic_lower:
        guide_type = "command reference guide"
    
    # Create proper title
    title = topic.title()
    if not title.endswith(("Guide", "Tutorial", "Instructions")):
        title += " - Learning Guide"
    
    return {
        "title": title,
        "technology": technology,
        "device": device,
        "experience_level": experience_level,
        "guide_type": guide_type,
        "original_topic": topic
    }
```

**Customized Prompt Generation:**
```python
def _create_topic_prompt(self, topic: str) -> str:
    """
    Create a customized prompt based on topic analysis.
    
    Args:
        topic: User-provided topic
        
    Returns:
        Customized prompt string
    """
    analysis = self._analyze_topic(topic)
    
    prompt = f"""
Create a comprehensive learning guide for: {topic}

Topic Analysis:
- Technology: {analysis['technology']}
- Platform: {analysis['device']}
- Experience Level: {analysis['experience_level']}
- Guide Type: {analysis['guide_type']}

Structure your guide with these sections:

# {analysis['title']}

## Learning Objectives
Clear, specific outcomes the learner will achieve
- Focus on practical skills and independence
- Include both technical and confidence-building objectives

## Prerequisites
What the learner should know or have set up before starting
- Previous experience assumptions
- Required software, hardware, or settings
- Environmental considerations (quiet space, assistance available)

## Step-by-Step Instructions
Detailed, numbered steps with clear explanations
- Include specific gesture commands, keyboard shortcuts, or menu paths
- Explain the purpose of each step
- Provide alternative methods when available
- Include checkpoints to verify progress

## Practice Activities
Hands-on exercises to reinforce the learning
- Start with guided practice, move to independent practice
- Include real-world scenarios relevant to daily life
- Progressive difficulty to build confidence

## Troubleshooting
Common issues and how to resolve them
- What to do when things don't work as expected
- How to recognize and recover from mistakes
- When to seek additional help or support

## Next Steps
Building on this foundation for continued learning
- Related skills to develop
- Resources for further learning
- Connection to broader assistive technology ecosystem

Special Considerations for {analysis['technology']} on {analysis['device']}:
- Include platform-specific details and terminology
- Reference official documentation and support resources
- Consider integration with other accessibility features
- Address common misconceptions or challenges specific to this combination

Writing Guidelines:
- Use encouraging, patient language throughout
- Explain technical terms in plain language
- Include practical tips from real-world experience
- Address emotional aspects of learning new technology
- Celebrate progress and build confidence
- Use person-first language consistently
- Provide context for why skills matter to independence
"""
    
    return prompt
```

### Session-Based Prompt Engineering

**Transcription Analysis Prompt:**
```python
def _create_analysis_prompt(self, transcription: str) -> str:
    """
    Create prompt for analyzing training session transcription.
    
    Args:
        transcription: Training session transcript
        
    Returns:
        Analysis prompt
    """
    return f"""
Analyze this training session transcription to extract key information 
for creating a personalized follow-up learning guide.

Transcription:
{transcription}

Please analyze and identify:

1. **Client Information:**
   - Name (if mentioned)
   - Learning style preferences that emerged
   - Technology comfort level demonstrated
   - Specific goals or motivations mentioned

2. **Technical Content:**
   - Assistive technology topics covered
   - Specific features or functions taught
   - Successful techniques that worked well
   - Areas where the client struggled

3. **Teaching Methods That Worked:**
   - Analogies or metaphors that resonated
   - Explanations that led to understanding
   - Pacing that was effective
   - Encouragement or support that helped

4. **Client Response Patterns:**
   - Moments of success and confidence
   - Points of confusion or frustration
   - Questions that indicated understanding
   - Language or terms the client used naturally

5. **Emotional Context:**
   - Confidence level throughout session
   - Concerns or anxieties expressed
   - Enthusiasm or resistance to certain features
   - Personal context that motivated learning

6. **Personalization Opportunities:**
   - Specific use cases or scenarios mentioned
   - Family or social connections referenced
   - Daily routines or activities discussed
   - Individual preferences expressed

Provide a structured analysis that will help create a follow-up guide 
that uses the same successful language, analogies, and methods from the session.
Focus on what will help this specific person continue learning effectively.
"""
```

**Personalized Guide Generation Prompt:**
```python
def _create_personalized_prompt(self, analysis: Dict[str, Any]) -> str:
    """
    Create prompt for personalized guide based on session analysis.
    
    Args:
        analysis: Analyzed session data
        
    Returns:
        Personalized guide prompt
    """
    return f"""
Based on this training session analysis, create a personalized learning guide 
that reinforces what was taught and continues the learning journey.

Session Analysis:
- Client: {analysis.get('client_name', 'Client')}
- Topics covered: {', '.join(analysis.get('topics', []))}
- Effective methods: {', '.join(analysis.get('effective_methods', []))}
- Learning style: {analysis.get('learning_style', 'hands-on')}
- Successes: {', '.join(analysis.get('successes', []))}
- Challenges: {', '.join(analysis.get('challenges', []))}

Create a guide that:
1. Uses the SAME language, analogies, and explanations that worked in the session
2. References specific moments of success to build confidence  
3. Addresses the individual challenges with patience and additional support
4. Feels like a natural continuation of your conversation
5. Maintains the personal connection established during training

Structure:
# Your Personal Learning Guide - {analysis.get('client_name', 'Client')}

## What We Accomplished Today
- Celebrate specific successes from the session
- Reference moments when things "clicked"
- Acknowledge the effort and progress made

## Your Key Techniques (What Worked Well)
- Use the exact analogies and explanations that resonated
- Reinforce the methods that led to success
- Build on the foundation of understanding established

## Practice Steps for This Week
- Specific exercises using the successful techniques
- Real-world applications relevant to their goals
- Progressive challenges that build confidence

## When You Get Stuck
- Solutions for the specific challenges that arose
- Reminders of successful strategies from the session
- Encouragement based on demonstrated capabilities

## For Our Next Session
- Building on today's foundation
- New skills that connect to established knowledge
- Questions to explore based on individual interests

Writing Guidelines:
- Write as if you're speaking directly to {analysis.get('client_name', 'this client')}
- Reference specific moments and breakthroughs from the session
- Use the teaching language and style that was effective
- Maintain the supportive, encouraging tone that worked
- Include personal touches that acknowledge their individual journey
"""
```

## Response Processing and Validation

### Content Structure Validation

**Validating Claude's Response:**
```python
def _validate_guide_content(self, content: str) -> tuple[bool, list[str]]:
    """
    Validate that generated content meets quality standards.
    
    Args:
        content: Generated guide content
        
    Returns:
        Tuple of (is_valid, list_of_issues)
    """
    issues = []
    
    # Check length
    if len(content) < 500:
        issues.append("Content too short (less than 500 characters)")
    elif len(content) > 20000:
        issues.append("Content too long (over 20,000 characters)")
    
    # Check for required sections
    required_sections = [
        "Learning Objectives",
        "Prerequisites", 
        "Step-by-Step Instructions",
        "Practice Activities",
        "Troubleshooting",
        "Next Steps"
    ]
    
    content_lower = content.lower()
    missing_sections = []
    for section in required_sections:
        if section.lower() not in content_lower:
            missing_sections.append(section)
    
    if missing_sections:
        issues.append(f"Missing required sections: {', '.join(missing_sections)}")
    
    # Check for markdown formatting
    if not content.startswith('#'):
        issues.append("Content should start with a markdown heading")
    
    # Check for step-by-step instructions
    if not any(pattern in content for pattern in ['1.', '2.', '3.', 'Step 1', 'Step 2']):
        issues.append("No numbered steps found in instructions")
    
    # Check for inappropriate content
    inappropriate_terms = ['impossible', 'can\'t be done', 'too difficult', 'give up']
    for term in inappropriate_terms:
        if term in content_lower:
            issues.append(f"Contains discouraging language: '{term}'")
    
    return len(issues) == 0, issues
```

**Content Enhancement and Cleanup:**
```python
def _enhance_content(self, content: str, metadata: Dict[str, Any]) -> str:
    """
    Enhance and clean up generated content.
    
    Args:
        content: Raw generated content
        metadata: Guide metadata
        
    Returns:
        Enhanced content
    """
    # Ensure proper title format
    lines = content.split('\n')
    if lines and not lines[0].startswith('# '):
        title = metadata.get('title', 'Learning Guide')
        content = f"# {title}\n\n{content}"
    
    # Add MyVision context if missing
    if 'MyVision' not in content and 'myvision' not in content.lower():
        footer = "\n\n---\n\n*This guide was created by MyVision Oxfordshire to support your assistive technology learning journey.*"
        content += footer
    
    # Ensure proper section spacing
    content = content.replace('\n##', '\n\n##')
    content = content.replace('\n#', '\n\n#')
    
    # Clean up multiple blank lines
    import re
    content = re.sub(r'\n\n\n+', '\n\n', content)
    
    return content.strip()
```

### Metadata Generation

**Creating Comprehensive Metadata:**
```python
def _create_metadata(self, topic: str, content: str, guide_type: str = "learning") -> Dict[str, Any]:
    """
    Generate comprehensive metadata for the guide.
    
    Args:
        topic: Original topic input
        content: Generated content
        guide_type: Type of guide ("learning" or "session")
        
    Returns:
        Metadata dictionary
    """
    from datetime import datetime
    
    # Analyze topic for metadata
    analysis = self._analyze_topic(topic)
    
    # Extract title from content or use analyzed title
    title = analysis['title']
    content_lines = content.split('\n')
    if content_lines and content_lines[0].startswith('# '):
        title = content_lines[0][2:].strip()
    
    # Calculate content statistics
    word_count = len(content.split())
    estimated_read_time = max(1, word_count // 200)  # 200 words per minute
    
    # Generate keywords from content
    keywords = self._extract_keywords(content, analysis)
    
    metadata = {
        # Basic information
        "type": f"{guide_type.title()} Guide",
        "title": title,
        "topic": topic,
        "generated": datetime.now().isoformat(),
        
        # Content analysis
        "technology": analysis['technology'],
        "device": analysis['device'],
        "experience_level": analysis['experience_level'],
        "guide_type": analysis['guide_type'],
        
        # Statistics
        "word_count": word_count,
        "estimated_read_time_minutes": estimated_read_time,
        "character_count": len(content),
        
        # Organization
        "client_name": None,  # Set for session guides
        "keywords": keywords,
        "sections": self._extract_sections(content),
        
        # Technical
        "generator_version": "1.0.0",
        "model_used": self.default_model,
        "temperature": self.temperature,
    }
    
    return metadata

def _extract_keywords(self, content: str, analysis: Dict[str, str]) -> list[str]:
    """Extract relevant keywords from content."""
    keywords = []
    
    # Add technology and device
    if analysis['technology'] != "assistive technology":
        keywords.append(analysis['technology'])
    if analysis['device'] != "device":
        keywords.append(analysis['device'])
    
    # Common assistive technology terms
    at_terms = [
        'screen reader', 'voice control', 'magnification', 'accessibility',
        'navigation', 'keyboard shortcuts', 'gestures', 'settings'
    ]
    
    content_lower = content.lower()
    for term in at_terms:
        if term in content_lower:
            keywords.append(term)
    
    # Limit keywords
    return keywords[:10]

def _extract_sections(self, content: str) -> list[str]:
    """Extract section headings from content."""
    import re
    
    # Find markdown headings
    headings = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
    
    # Clean and return
    return [heading.strip() for heading in headings if heading.strip()]
```

## Complete GuideGenerator Implementation

**Full Class Implementation:**
```python
"""
Core guide generation using Anthropic Claude

This module handles all AI interactions and content generation,
creating structured, educational content for assistive technology topics.
"""

import asyncio
from typing import Dict, Any, Optional, Tuple
from datetime import datetime
import re

from anthropic import Anthropic, APIError, RateLimitError, AuthenticationError

from .config import config

class GuideGenerationError(Exception):
    """Raised when guide generation fails"""
    pass

class GuideGenerator:
    """
    Main class for generating learning guides using Claude AI.
    
    This class handles all AI interactions and content generation,
    creating structured, educational content for assistive technology topics.
    """
    
    def __init__(self):
        """Initialize the guide generator with Claude client."""
        try:
            self.client = Anthropic(api_key=config.anthropic_api_key)
        except Exception as e:
            raise GuideGenerationError(f"Failed to initialize Anthropic client: {e}")
        
        # API configuration
        self.default_model = config.default_model
        self.max_tokens = config.max_tokens
        self.temperature = config.temperature
        
        # System prompt for Claude
        self.system_prompt = """
        You are an expert assistive technology trainer at MyVision Oxfordshire 
        with 15+ years of experience helping people with visual impairments and other disabilities.

        Your expertise includes:
        - Screen readers: VoiceOver (iOS/macOS), JAWS (Windows), NVDA (Windows), TalkBack (Android)
        - Magnification tools: ZoomText, built-in OS magnification, hardware magnifiers
        - Voice control: Dragon NaturallySpeaking, built-in voice commands
        - Switch navigation and alternative input methods
        - Mobile accessibility: iPhone, iPad, Android accessibility features
        - Desktop accessibility: Windows, macOS, Linux accessibility settings

        Your teaching philosophy:
        - Start with empathy and encouragement
        - Break complex concepts into manageable, sequential steps
        - Use clear, jargon-free language with explanations of technical terms
        - Provide context for why each step matters to the user's independence
        - Include practical tips from real-world experience
        - Address common concerns and emotional aspects of learning new technology
        - End with confidence-building next steps and resources

        Your communication style:
        - Warm, supportive, and patient tone
        - Person-first language (person with visual impairment, not "blind person")
        - Acknowledge the learning curve and celebrate small wins
        - Include practical wisdom about when to ask for help
        - Reference the broader assistive technology ecosystem

        Your goal is to create learning guides that empower independence, 
        build confidence, and provide practical skills for daily life with assistive technology.
        """
    
    async def generate_topic_guide(self, topic: str) -> Dict[str, Any]:
        """
        Generate a learning guide for a specific assistive technology topic.
        
        Args:
            topic: What to create a guide for (e.g., "VoiceOver rotor basics")
            
        Returns:
            Dictionary containing 'content', 'title', and 'metadata'
            
        Raises:
            GuideGenerationError: If generation fails
        """
        try:
            # Analyze topic for customization
            analysis = self._analyze_topic(topic)
            
            # Create customized prompt
            prompt = self._create_topic_prompt(topic, analysis)
            
            # Call Claude API
            response = await self._robust_api_call(prompt)
            
            # Extract and validate content
            content = response.content[0].text
            is_valid, issues = self._validate_guide_content(content)
            
            if not is_valid:
                raise GuideGenerationError(f"Generated content validation failed: {'; '.join(issues)}")
            
            # Enhance content
            content = self._enhance_content(content, analysis)
            
            # Create metadata
            metadata = self._create_metadata(topic, content, "learning")
            metadata.update(analysis)
            
            return {
                "content": content,
                "title": analysis['title'],
                "metadata": metadata
            }
            
        except Exception as e:
            if isinstance(e, GuideGenerationError):
                raise
            raise GuideGenerationError(f"Failed to generate topic guide: {str(e)}")
    
    async def generate_session_guide(self, transcription: str) -> Dict[str, Any]:
        """
        Generate a personalized learning guide from training session transcription.
        
        Args:
            transcription: Text transcription from training session
            
        Returns:
            Dictionary containing 'content', 'title', and 'metadata'
            
        Raises:
            GuideGenerationError: If generation fails
        """
        try:
            # Analyze transcription
            analysis = await self._analyze_transcription(transcription)
            
            # Create personalized prompt
            prompt = self._create_personalized_prompt(analysis)
            
            # Call Claude API
            response = await self._robust_api_call(prompt)
            
            # Extract and validate content
            content = response.content[0].text
            is_valid, issues = self._validate_guide_content(content)
            
            if not is_valid:
                raise GuideGenerationError(f"Generated content validation failed: {'; '.join(issues)}")
            
            # Enhance content
            metadata_for_enhancement = {"title": f"Learning Guide for {analysis['client_name']}"}
            content = self._enhance_content(content, metadata_for_enhancement)
            
            # Create metadata
            metadata = self._create_session_metadata(transcription, content, analysis)
            
            return {
                "content": content,
                "title": f"Learning Guide for {analysis['client_name']}",
                "metadata": metadata
            }
            
        except Exception as e:
            if isinstance(e, GuideGenerationError):
                raise
            raise GuideGenerationError(f"Failed to generate session guide: {str(e)}")
    
    async def _robust_api_call(self, prompt: str):
        """Make robust API call with error handling and retries."""
        
        for attempt in range(config.max_retries):
            try:
                response = await asyncio.to_thread(
                    self.client.messages.create,
                    model=self.default_model,
                    max_tokens=self.max_tokens,
                    temperature=self.temperature,
                    system=self.system_prompt,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
                return response
                
            except RateLimitError as e:
                if attempt < config.max_retries - 1:
                    wait_time = min(2 ** attempt, 60)
                    await asyncio.sleep(wait_time)
                    continue
                raise GuideGenerationError("Rate limit exceeded. Please try again later.")
                
            except AuthenticationError:
                raise GuideGenerationError("Authentication failed. Please check your API key.")
                
            except APIError as e:
                if attempt < config.max_retries - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                raise GuideGenerationError(f"API error: {str(e)}")
            
            except Exception as e:
                if attempt < config.max_retries - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                raise GuideGenerationError(f"Unexpected error: {str(e)}")
        
        raise GuideGenerationError("API request failed after all retries.")
    
    # [Additional helper methods would be implemented here]
    # _analyze_topic, _create_topic_prompt, _validate_guide_content, etc.
    # (These are shown in detail in previous sections)
```

## Testing and Validation

### Unit Testing the AI Logic

**Create test file:**
```python
# test_guide_generator.py
"""Tests for the GuideGenerator class"""

import pytest
import asyncio
from unittest.mock import Mock, patch

from myvision_guides.guide_generator import GuideGenerator, GuideGenerationError

class TestGuideGenerator:
    
    @pytest.fixture
    def generator(self):
        """Create generator instance for testing"""
        return GuideGenerator()
    
    def test_initialization(self, generator):
        """Test that generator initializes correctly"""
        assert generator.client is not None
        assert generator.default_model is not None
        assert generator.system_prompt is not None
    
    @pytest.mark.asyncio
    async def test_topic_guide_generation(self, generator):
        """Test basic topic guide generation"""
        
        # Mock API response
        mock_response = Mock()
        mock_response.content = [Mock(text="# VoiceOver Basics\n\n## Learning Objectives\n...")]
        
        with patch.object(generator, '_robust_api_call', return_value=mock_response):
            result = await generator.generate_topic_guide("VoiceOver basics")
            
            assert "content" in result
            assert "title" in result
            assert "metadata" in result
            assert len(result["content"]) > 0
    
    def test_topic_analysis(self, generator):
        """Test topic analysis functionality"""
        
        analysis = generator._analyze_topic("VoiceOver rotor navigation on iPhone")
        
        assert analysis["technology"] == "VoiceOver"
        assert analysis["device"] == "iPhone"
        assert "rotor" in analysis["original_topic"].lower()
    
    def test_content_validation(self, generator):
        """Test content validation"""
        
        # Valid content
        valid_content = """
        # Test Guide
        
        ## Learning Objectives
        Learn something
        
        ## Prerequisites
        Know something
        
        ## Step-by-Step Instructions
        1. Do this
        2. Do that
        
        ## Practice Activities
        Practice
        
        ## Troubleshooting
        Fix issues
        
        ## Next Steps
        Continue learning
        """
        
        is_valid, issues = generator._validate_guide_content(valid_content)
        assert is_valid
        assert len(issues) == 0
        
        # Invalid content (too short)
        invalid_content = "Short content"
        is_valid, issues = generator._validate_guide_content(invalid_content)
        assert not is_valid
        assert len(issues) > 0
```

### Integration Testing

**Test with actual API:**
```python
# integration_test.py
"""Integration test with actual Claude API"""

import asyncio
import os
from myvision_guides.guide_generator import GuideGenerator

async def test_real_api():
    """Test with real API (requires valid API key)"""
    
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Skipping integration test - no API key")
        return
    
    generator = GuideGenerator()
    
    try:
        # Test topic guide
        result = await generator.generate_topic_guide("VoiceOver basics for beginners")
        
        print("✅ API call successful")
        print(f"Title: {result['title']}")
        print(f"Content length: {len(result['content'])} characters")
        print(f"Technology: {result['metadata']['technology']}")
        
        # Verify content structure
        content = result['content']
        assert "Learning Objectives" in content
        assert "Step-by-Step Instructions" in content
        assert "Next Steps" in content
        
        print("✅ Content structure valid")
        
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(test_real_api())
```

## Best Practices Summary

### AI Integration
1. **Use async for API calls** - Prevents blocking user interface
2. **Implement robust error handling** - Handle rate limits, network issues
3. **Validate API responses** - Ensure content meets quality standards
4. **Cache expensive operations** - Avoid redundant API calls
5. **Monitor usage and costs** - Track API consumption

### Prompt Engineering
1. **Design system prompts carefully** - Establish expertise and tone
2. **Customize prompts for context** - Analyze input for better results
3. **Include specific examples** - Guide AI toward desired output
4. **Validate prompt effectiveness** - Test prompts with various inputs
5. **Version control prompts** - Track changes and improvements

### Content Quality
1. **Validate generated content** - Check structure and completeness
2. **Enhance content post-generation** - Clean up formatting and add context
3. **Maintain consistent structure** - Ensure all guides follow same format
4. **Include comprehensive metadata** - Support search and organization
5. **Test with real users** - Validate educational effectiveness

### Error Handling
1. **Provide specific error messages** - Help users understand issues
2. **Implement graceful degradation** - Partial success better than failure
3. **Log errors for debugging** - Track patterns and improvements
4. **Retry with backoff** - Handle temporary issues automatically
5. **Validate configuration early** - Catch setup issues immediately

---

*This AI logic guide provides the intelligence that transforms your CLI tool from a simple utility into a sophisticated AI-powered assistant for creating professional educational content.*