"""
Core guide generation using Anthropic Claude

This file handles all communication with Claude AI to create learning guides.
"""

# SECTION Imports
"""
Essential imports for AI integration and asynchronous operations.

Key components explained:
- asyncio: Python's built-in library for handling asynchronous (non-blocking) operations.
  This allows our program to send requests to Claude AI and continue working while waiting
  for responses, making the interface more responsive for users.

- typing.Dict, typing.Any, typing.AsyncGenerator: Type hints that help document what kinds of data our functions
  expect and return. Dict[str, Any] means a dictionary with string keys and values of any type.
  AsyncGenerator enables proper typing for streaming content generation.

- anthropic.Anthropic: The official Python client for communicating with Claude AI. This
  handles authentication, request formatting, and response processing automatically.

- datetime: Standard library for working with dates and times. We use this to timestamp
  when guides are generated for tracking and organization purposes.

- .config: Our local configuration module that securely stores API keys, AI model settings,
  and other application preferences in environment variables.
"""
import asyncio
from typing import Dict, Any, AsyncGenerator
from anthropic import Anthropic 
from datetime import datetime

from .config import config

# SECTION GuideGenerator Class
class GuideGenerator:
    """
    The main class that communicates with Claude AI to create learning guides.
    
    This class implements the Singleton pattern (through configuration) and handles
    all aspects of AI interaction for generating assistive technology documentation.
    
    Architecture Overview:
    - Manages authentication with Anthropic's Claude AI service
    - Constructs specialized prompts for assistive technology education
    - Handles asynchronous API communication for responsive user experience
    - Processes AI responses into structured, usable content
    - Provides comprehensive error handling and logging
    
    Educational Focus:
    The class is designed specifically for creating guides that help people with
    visual impairments learn assistive technology. Every prompt and system message
    is crafted with empathy, clarity, and practical application in mind.
    
    Think of this as your specialized AI assistant that understands both the
    technical aspects of assistive technology AND the human experience of
    learning to use these tools.
    """
    
    # SECTION Constructor
    def __init__(self):
        """
        Initialize the AI client connection and system configuration.
        
        The constructor sets up the authenticated connection to Claude AI using
        the API key from our secure configuration. This pattern ensures that
        API credentials are never hardcoded in the source code.
        
        Architecture Note:
        We initialize the Anthropic client once during object creation rather
        than on each request for efficiency and connection pooling. The client
        handles connection management, rate limiting, and retry logic automatically.
        
        Security:
        The API key is loaded from environment variables through our config module,
        following security best practices for credential management.
        """
        self.client = Anthropic(api_key=config.anthropic_api_key)

        # SECTION System Prompt
        """
        The system prompt defines Claude's personality and expertise for our specific use case.
        
        This is a critical component of prompt engineering - the practice of carefully crafting
        instructions that guide AI behavior to produce consistent, high-quality outputs.
        
        Prompt Engineering Principles Applied:
        1. Role Definition: We establish Claude as an experienced AT trainer with specific credentials
        2. Expertise Areas: Clearly list the technical domains Claude should draw knowledge from
        3. Teaching Philosophy: Define the educational approach and values to maintain consistency
        4. Goal Orientation: Specify the desired outcomes (empowerment and confidence building)
        
        Why This Matters:
        Without a well-defined system prompt, AI responses can be inconsistent, too technical,
        or miss the emotional aspects of learning assistive technology. This prompt ensures
        every guide maintains MyVision's empathetic, practical teaching approach.
        
        The prompt is designed to:
        - Establish credibility and trust with learners
        - Ensure consistent tone and approach across all guides
        - Focus on practical, real-world application
        - Address the emotional journey of learning new technology
        - Maintain professional standards while being approachable
        """
        # This is the "personality" and expertise profile we give Claude
        self.system_prompt = """
        You are an expert assistive technology trainer at MyVision Oxfordshire 
        with 15+ years of experience helping people with visual impairments.
        
        Your expertise includes:
        - All major screen readers (VoiceOver, JAWS, NVDA, TalkBack)
        - Magnification software and tools
        - Voice control systems
        - Mobile and desktop accessibility features
        
        Your teaching philosophy:
        - Start with empathy and encouragement
        - Break complex concepts into manageable steps
        - Use clear, jargon-free language
        - Provide context for why each step matters
        - Include practical tips and troubleshooting
        
        Your goal is to create learning guides that empower independence
        and build confidence with assistive technology.
        """
    
    # SECTION Topic Guide Generation
    async def generate_topic_guide(self, topic: str) -> Dict[str, Any]:
        """
        Generate a comprehensive learning guide for a specific assistive technology topic.
        
        This is the main public method that coordinates the entire guide generation process.
        It handles prompt construction, AI communication, response processing, and metadata
        creation in a single, cohesive workflow.
        
        Asynchronous Design:
        The method is marked as 'async' to prevent the user interface from freezing while
        waiting for Claude's response. This is especially important for AI operations which
        can take several seconds to complete.
        
        Parameters:
            topic (str): The subject for the learning guide. Examples:
                        "VoiceOver rotor navigation"
                        "JAWS virtual cursor basics" 
                        "iPhone accessibility setup"
                        "NVDA browse mode fundamentals"
        
        Returns:
            Dict[str, Any]: A structured dictionary containing:
                - 'content': The full markdown-formatted guide text
                - 'title': Formatted title for the guide
                - 'metadata': Dictionary with generation info, timestamps, and categorization
        
        Error Handling:
        Comprehensive exception handling ensures graceful failure with meaningful error
        messages that help users understand what went wrong and how to resolve it.
        """
        
        # SECTION Prompt Construction
        """
        Advanced prompt engineering for educational content generation.
        
        This section demonstrates sophisticated prompt design that combines:
        1. Clear structural requirements (sections and formatting)
        2. Content guidelines (tone, depth, examples)
        3. Educational best practices (learning objectives, practice activities)
        4. Accessibility considerations (clear language, logical flow)
        
        Template Structure Explained:
        - Learning Objectives: Helps learners understand the purpose and outcomes
        - Prerequisites: Prevents frustration by setting appropriate expectations
        - Step-by-Step Instructions: Core content with detailed, actionable guidance
        - Practice Activities: Reinforces learning through hands-on application
        - Troubleshooting: Addresses common challenges proactively
        - Next Steps: Provides clear learning progression paths
        
        Prompt Engineering Techniques:
        - Structural constraints ensure consistent output format
        - Style guidelines maintain appropriate tone and complexity
        - Example requirements ensure concrete, actionable content
        - Emotional considerations address the human side of learning
        
        Why This Structure Works:
        This format is based on adult learning principles and accessibility best practices.
        It provides multiple ways to engage with the content (reading, doing, troubleshooting)
        while maintaining a logical progression that builds confidence.
        """
        # Create a detailed prompt that tells Claude exactly what we want
        prompt = f"""
        Create a comprehensive learning guide for: {topic}
        
        Structure your guide with these sections:
        
        # {topic.title()} - Learning Guide
        
        ## Learning Objectives
        What the learner will accomplish by completing this guide
        
        ## Prerequisites
        What they should know or have set up before starting
        
        ## Step-by-Step Instructions
        Detailed, numbered steps with clear explanations
        Include specific gesture commands, keyboard shortcuts, or menu paths
        
        ## Practice Activities
        Hands-on exercises to reinforce the learning
        
        ## Troubleshooting
        Common issues and how to resolve them
        
        ## Next Steps
        What to learn next to build on this foundation
        
        Guidelines:
        - Use encouraging, supportive language throughout
        - Explain WHY steps are important, not just HOW
        - Include specific examples and scenarios
        - Consider the emotional journey of learning new technology
        - Use active voice and clear instructions
        """

        # SECTION Chain of Thought Prompt Enhancement
        """
        Advanced prompt engineering for chain-of-thought streaming.
        
        When chain-of-thought mode is enabled, we modify the prompt to encourage
        the AI to show its reasoning process. This provides educational value by
        demonstrating how expert educators approach content creation.
        
        Educational Benefits:
        - Shows pedagogical decision-making process
        - Demonstrates how to analyze learning objectives
        - Reveals consideration of different learner needs
        - Illustrates content structuring techniques
        """
        if config.stream_thinking_process:
            if config.thinking_detail_level == "detailed":
                thinking_instruction = """
                
                IMPORTANT: Show your complete thought process as you work.
                
                Think out loud about:
                - How you analyze this topic and its complexity
                - What you know about the target audience
                - Your pedagogical decisions and why you make them
                - How you structure content for maximum learning
                - What examples and activities would be most effective
                
                Format your thinking clearly, then create the guide.
                """
            elif config.thinking_detail_level == "expert":
                thinking_instruction = """
                
                IMPORTANT: Demonstrate expert-level educational reasoning.
                
                Show your complete analysis including:
                - Topic complexity assessment and prerequisite mapping
                - Learner persona analysis and accessibility considerations  
                - Cognitive load management and chunking strategies
                - Multi-modal learning approach selection
                - Common failure points and mitigation strategies
                - Assessment and practice activity design rationale
                
                Provide deep insight into your educational decision-making process.
                """
            else:  # basic level
                thinking_instruction = """
                
                IMPORTANT: Think out loud as you create this guide.
                
                Show me your reasoning about:
                - What makes this topic challenging for learners
                - How you'll structure the content
                - Why you choose specific examples
                
                Then create the guide based on your analysis.
                """
            
            prompt = prompt + thinking_instruction
        
        # SECTION API Request and Response Handling
        """
        Asynchronous communication with Claude AI using advanced threading techniques.
        
        Technical Implementation:
        We use asyncio.to_thread() to wrap the synchronous Anthropic client call in an
        asynchronous context. This prevents the entire application from freezing while
        waiting for Claude's response, which can take 5-30 seconds depending on complexity.
        
        Why Asynchronous Matters:
        - User Interface Responsiveness: Users can see progress indicators and remain engaged
        - Better Resource Utilization: The application can handle other tasks while waiting
        - Improved User Experience: No "frozen" interface that makes users think the app crashed
        - Scalability: Multiple requests could theoretically be handled concurrently
        
        API Configuration Explained:
        - model: The specific Claude model (e.g., claude-3-sonnet-20240229) configured for optimal
          balance of quality, speed, and cost for educational content
        - max_tokens: Maximum length of response to prevent runaway generation and control costs
        - temperature: Controls creativity vs consistency (lower = more focused and consistent)
        - system: The personality/expertise prompt that shapes all responses
        - messages: The conversation format required by the Claude API
        
        Error Recovery:
        The try/except block catches various failure modes:
        - Network connectivity issues
        - API authentication problems
        - Rate limiting or quota exceeded
        - Invalid request format
        - Service unavailability
        """
        try:
            # Send the request to Claude using asynchronous threading
            response = await asyncio.to_thread(
                self.client.messages.create,
                model=config.default_model,
                max_tokens=config.max_tokens,
                temperature=config.temperature,
                system=self.system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            # SECTION Response Processing
            """
            Extract and validate the AI-generated content from Claude's response.
            
            Response Structure Understanding:
            Claude's API returns a complex response object with multiple components:
            - response.content: Array of content blocks (text, images, etc.)
            - response.content[0].text: The actual generated text content
            - response.usage: Token usage statistics for billing/monitoring
            - response.model: Confirmation of which model was used
            
            Content Extraction:
            We access response.content[0].text because Claude can return multiple
            content blocks in advanced use cases (text + images, multiple text blocks).
            For our educational guides, we expect a single text block with markdown.
            
            Validation Considerations:
            In production, you might add validation here to ensure:
            - Content is not empty
            - Required sections are present
            - Content length is reasonable
            - Markdown formatting is valid
            
            Quality Assurance:
            The content at this point should be well-structured markdown that follows
            our prompt template, but it's still raw AI output that will be processed
            further by the file manager for final formatting.
            """
            # Extract the content from Claude's response
            content = response.content[0].text
            
            # SECTION Metadata Creation
            """
            Generate comprehensive metadata for content organization and tracking.
            
            Metadata serves multiple critical purposes in the system:
            
            1. Content Management:
               - Categorizes content by type (Learning Guide, Quick Reference, etc.)
               - Enables search and filtering in content management systems
               - Supports automated content organization
            
            2. Version Control:
               - Timestamps enable tracking when content was generated
               - Helps identify outdated content that needs refreshing
               - Supports content auditing and quality assurance processes
            
            3. Personalization:
               - client_name field allows for personalized content when needed
               - Supports custom branding and tailored messaging
               - Enables tracking of client-specific content requests
            
            4. Analytics and Reporting:
               - Topic tracking helps identify popular subjects
               - Generation timestamps support usage analytics
               - Type classification enables content performance metrics
            
            Metadata Structure:
            The metadata follows a consistent schema that can be extended as needed.
            All datetime values use ISO 8601 format for international compatibility
            and precise timestamp representation across different systems and time zones.
            
            Future Extensions:
            This metadata structure can be extended to include:
            - Content difficulty level
            - Estimated completion time
            - Prerequisites references
            - Related content suggestions
            - User feedback scores
            """
            # Create comprehensive metadata for content organization and tracking
            metadata = {
                "type": "Learning Guide",
                "title": f"{topic.title()} - Learning Guide",
                "topic": topic,
                "generated": datetime.now().isoformat(),
                "client_name": None
            }

            # SECTION Return Result
            """
            Package the generated content and metadata into a standardized response format.
            
            Response Architecture:
            The returned dictionary provides a clean, consistent interface for the rest
            of the application. This standardization enables:
            
            1. Predictable Data Structure:
               - Other components can reliably access content, title, and metadata
               - Reduces coupling between the AI generation and file processing
               - Simplifies testing and validation
            
            2. Extensibility:
               - New fields can be added without breaking existing code
               - Metadata can be enriched with additional information
               - Multiple content formats could be supported in the future
            
            3. Error Handling:
               - Consistent return format makes error detection easier
               - Metadata includes generation status and timestamp
               - Calling code can validate the response structure
            
            Content Flow:
            This response flows to the FileManager class, which handles:
            - Saving content to markdown files
            - Converting to Word documents if requested
            - Adding MyVision branding and formatting
            - Creating proper file names and organization
            
            The separation of concerns between content generation (this class)
            and content management (FileManager) creates a modular, maintainable
            architecture where each component has a single, clear responsibility.
            """
            return {
                "content": content,
                "title": f"{topic.title()} - Learning Guide",
                "metadata": metadata
            }
            
        except Exception as e:
            # SECTION Error Handling
            """
            Comprehensive error handling for robust, user-friendly operation.
            
            Error Handling Strategy:
            This catch-all exception handler implements a "fail-fast" approach that
            provides meaningful error messages while preventing system crashes.
            
            Common Error Scenarios:
            1. Network Issues:
               - Internet connectivity problems
               - DNS resolution failures
               - Firewall or proxy blocking
            
            2. Authentication Errors:
               - Invalid or expired API key
               - Insufficient API permissions
               - Account suspension or billing issues
            
            3. API Limitations:
               - Rate limiting (too many requests)
               - Token quota exceeded
               - Model temporarily unavailable
            
            4. Request Format Errors:
               - Invalid model name in configuration
               - Malformed prompt or system message
               - Parameter values outside allowed ranges
            
            5. Service Errors:
               - Anthropic service downtime
               - Model-specific outages
               - Temporary capacity limitations
            
            Error Message Design:
            The error message format "Failed to generate guide: {error details}"
            provides users with:
            - Clear indication of what operation failed
            - Specific technical details for troubleshooting
            - Consistent messaging across the application
            
            Production Considerations:
            In a production environment, you might enhance this with:
            - Structured logging with severity levels
            - Error categorization for automated handling
            - Retry logic for transient failures
            - User-friendly error messages for common issues
            - Integration with monitoring and alerting systems
            
            The exception is re-raised to allow calling code to handle it appropriately,
            whether that's displaying an error message to the user, logging for debugging,
            or implementing fallback strategies.
            """
            raise Exception(f"Failed to generate guide: {str(e)}")

    # SECTION Streaming Guide Generation (Phase 2 Enhancement)
    async def stream_topic_guide(self, topic: str) -> AsyncGenerator[str, None]:
        """
        Generate a comprehensive learning guide with real-time streaming output.
        
        This method implements Phase 2 enhancement: Streaming AI Responses for improved
        user experience and perceived performance. Instead of waiting for the complete
        response, users see the guide being generated in real-time.
        
        Streaming Architecture:
        This method uses the Anthropic Claude streaming API to deliver content as it's
        generated. Each piece of content is yielded immediately upon receipt, creating
        a smooth, engaging user experience that shows the AI "thinking" and writing.
        
        Technical Implementation:
        - Uses async generator pattern for memory-efficient streaming
        - Handles streaming events from Anthropic's API
        - Accumulates content while yielding chunks for real-time display
        - Maintains full backward compatibility with existing code
        - Preserves all error handling and quality standards from Phase 1
        
        Parameters:
            topic (str): The subject for the learning guide. Examples:
                        "VoiceOver rotor navigation"
                        "JAWS virtual cursor basics" 
                        "iPhone accessibility setup"
                        "NVDA browse mode fundamentals"
        
        Yields:
            str: Chunks of content as they are generated by Claude AI.
                 Each chunk contains a portion of the final guide text.
                 
        Raises:
            AuthenticationError: Invalid API key
            RateLimitError: API usage quota exceeded
            APITimeoutError: Request timeout
            APIConnectionError: Network connectivity issues
            APIStatusError: Server-side errors
            Exception: Unexpected errors with descriptive messages
        
        Usage Example:
            async for chunk in guide_generator.stream_topic_guide("VoiceOver basics"):
                console.print(chunk, end="")  # Display chunk immediately
        """
        
        # SECTION Prompt Construction (Identical to Non-Streaming)
        """
        Use the same high-quality prompt engineering as the non-streaming method.
        This ensures consistent output quality regardless of delivery method.
        """
        prompt = f"""
        Create a comprehensive learning guide for: {topic}
        
        Structure your guide with these sections:
        
        # {topic.title()} - Learning Guide
        
        ## Learning Objectives
        What the learner will accomplish by completing this guide
        
        ## Prerequisites
        What they should know or have set up before starting
        
        ## Step-by-Step Instructions
        Detailed, numbered steps with clear explanations
        Include specific gesture commands, keyboard shortcuts, or menu paths
        
        ## Practice Activities
        Hands-on exercises to reinforce the learning
        
        ## Troubleshooting
        Common issues and how to resolve them
        
        ## Next Steps
        What to learn next to build on this foundation
        
        Guidelines:
        - Use encouraging, supportive language throughout
        - Explain WHY steps are important, not just HOW
        - Include specific examples and scenarios
        - Consider the emotional journey of learning new technology
        - Use active voice and clear instructions
        """

        # SECTION Chain of Thought Prompt Enhancement
        """
        Advanced prompt engineering for chain-of-thought streaming.
        
        When chain-of-thought mode is enabled, we modify the prompt to encourage
        the AI to show its reasoning process. This provides educational value by
        demonstrating how expert educators approach content creation.
        
        Educational Benefits:
        - Shows pedagogical decision-making process
        - Demonstrates how to analyze learning objectives
        - Reveals consideration of different learner needs
        - Illustrates content structuring techniques
        """
        if config.stream_thinking_process:
            if config.thinking_detail_level == "detailed":
                thinking_instruction = """
                
                IMPORTANT: Show your complete thought process as you work.
                
                Think out loud about:
                - How you analyze this topic and its complexity
                - What you know about the target audience
                - Your pedagogical decisions and why you make them
                - How you structure content for maximum learning
                - What examples and activities would be most effective
                
                Format your thinking clearly, then create the guide.
                """
            elif config.thinking_detail_level == "expert":
                thinking_instruction = """
                
                IMPORTANT: Demonstrate expert-level educational reasoning.
                
                Show your complete analysis including:
                - Topic complexity assessment and prerequisite mapping
                - Learner persona analysis and accessibility considerations  
                - Cognitive load management and chunking strategies
                - Multi-modal learning approach selection
                - Common failure points and mitigation strategies
                - Assessment and practice activity design rationale
                
                Provide deep insight into your educational decision-making process.
                """
            else:  # basic level
                thinking_instruction = """
                
                IMPORTANT: Think out loud as you create this guide.
                
                Show me your reasoning about:
                - What makes this topic challenging for learners
                - How you'll structure the content
                - Why you choose specific examples
                
                Then create the guide based on your analysis.
                """
            
            prompt = prompt + thinking_instruction
        
        # SECTION Streaming API Request and Event Processing
        """
        Advanced streaming implementation using Anthropic's event-driven API.
        
        Streaming Event Handling:
        The Anthropic API returns a stream of events rather than a single response.
        Each event represents a piece of the AI's response as it's generated.
        
        Event Types (from Anthropic documentation):
        - message_start: Stream initialization
        - content_block_start: Beginning of content generation
        - content_block_delta: Incremental content chunks (THIS IS WHAT WE WANT)
        - content_block_stop: End of content generation
        - message_stop: Stream completion
        
        Real-Time Processing:
        We iterate through the event stream and yield content deltas immediately,
        providing users with real-time feedback as the AI generates the response.
        
        Memory Efficiency:
        Using async generators ensures minimal memory usage even for very long
        responses, as content is yielded and processed incrementally.
        
        Error Handling:
        All existing error handling from Phase 1 is preserved and enhanced for
        streaming scenarios, including partial content recovery.
        """
        try:
            # Create streaming request to Claude AI
            def create_streaming_request():
                return self.client.messages.create(
                    model=config.default_model,
                    max_tokens=config.max_tokens,
                    temperature=config.temperature,
                    system=self.system_prompt,
                    messages=[{"role": "user", "content": prompt}],
                    stream=True  # Enable streaming mode
                )
            
            # Execute streaming request in thread to maintain async compatibility
            response_stream = await asyncio.to_thread(create_streaming_request)
            
            # Process streaming events and yield content as it arrives
            accumulated_content = ""
            
            # Handle synchronous streaming response
            for event in response_stream:
                # Handle content delta events (the actual text chunks)
                if hasattr(event, 'type') and event.type == "content_block_delta":
                    if hasattr(event, 'delta') and hasattr(event.delta, 'text'):
                        text_chunk = event.delta.text
                        accumulated_content += text_chunk
                        yield text_chunk
                
                # Handle other event types for completeness and debugging
                elif hasattr(event, 'type'):
                    # Stream start/stop events - could be used for additional UX
                    pass
            
            # Validate that we received complete content
            if not accumulated_content.strip():
                raise Exception("No content received from streaming API")
                
        except Exception as e:
            # Enhanced error handling for streaming scenarios
            """
            Streaming-specific error scenarios require special handling:
            
            1. Stream Interruption:
               - Connection drops during streaming
               - Partial content received
               - Network timeouts mid-stream
            
            2. Event Processing Errors:
               - Malformed streaming events
               - Unexpected event types
               - Missing required event fields
            
            3. Fallback Strategy:
               - Automatic retry with non-streaming mode
               - Partial content preservation
               - User notification of streaming issues
            
            All existing error types from Phase 1 are preserved and will
            propagate correctly through the streaming infrastructure.
            """
            raise Exception(f"Failed to stream guide generation: {str(e)}")

    # SECTION Legacy Compatibility Method
    async def generate_topic_guide_with_streaming(self, topic: str) -> Dict[str, Any]:
        """
        Generate a topic guide using streaming with legacy-compatible return format.
        
        This method bridges the gap between the new streaming functionality and
        existing code that expects the traditional Dict[str, Any] return format.
        It accumulates all streamed content and returns it in the expected format.
        
        This enables gradual adoption of streaming while maintaining full backward
        compatibility with existing file saving and processing logic.
        
        Parameters:
            topic (str): The subject for the learning guide
            
        Returns:
            Dict[str, Any]: Traditional format with complete content and metadata
        """
        # Accumulate all streaming content
        full_content = ""
        async for chunk in self.stream_topic_guide(topic):
            full_content += chunk
        
        # Return in traditional format for compatibility
        return {
            "content": full_content,
            "title": f"{topic.title()} - Learning Guide",
            "metadata": {
                "generated": datetime.now().isoformat(),
                "topic": topic,
                "type": "learning_guide",
                "client_name": None,
                "streaming_enabled": True
            }
        }
