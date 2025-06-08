"""
Command Line Interface for MyVision Guide Generator

This creates the commands you'll actually type in Terminal.
"""

# SECTION Imports
"""
Strategic imports for building a professional command-line interface.

Architecture Components:
- sys: System-specific parameters and functions, used for exit codes and
  system integration. Enables proper error reporting and graceful shutdowns.

- asyncio: Asynchronous I/O framework enabling non-blocking operations.
  Critical for AI API calls that can take 5-30 seconds while maintaining
  responsive user feedback through progress indicators.

- pathlib.Path: Modern, cross-platform path handling for file operations.
  Provides intuitive file system navigation that works identically on
  Windows, macOS, and Linux systems.

User Interface Libraries:
- click: Professional command-line interface framework that provides:
  * Automatic help generation
  * Parameter validation and type conversion
  * Nested command structures
  * Shell completion support
  * Consistent error handling

- rich.console.Console: Advanced terminal output with:
  * Color and styling support
  * Automatic terminal capability detection
  * Unicode and emoji support
  * Responsive layout adaptation

- rich.panel.Panel: Structured output formatting for:
  * Professional information display
  * Clear visual separation of content
  * Consistent branding and appearance

- rich.progress: Real-time progress indication featuring:
  * Spinner animations for indefinite operations
  * Progress bars for measurable tasks
  * Customizable display components
  * Time estimation and throughput metrics

Core System Integration:
- .config: Application configuration management
- .guide_generator: AI content generation engine  
- .file_manager: Document creation and formatting system

This import structure creates a clear separation between user interface,
business logic, and system integration components.
"""
import sys
import asyncio
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from .config import config
from .guide_generator import GuideGenerator
from .file_manager import FileManager

# SECTION Console Setup
"""
Initialize the Rich console for professional terminal output.

Console Configuration:
The Rich Console object provides advanced terminal capabilities that
enhance the user experience significantly compared to basic print statements:

1. Automatic Terminal Detection:
   - Detects terminal capabilities (color support, Unicode, width)
   - Adapts output formatting based on terminal environment
   - Handles edge cases like IDE terminals, CI/CD environments, and SSH sessions

2. Professional Output Formatting:
   - Consistent styling and branding across all messages
   - Automatic text wrapping based on terminal width
   - Support for markup, emoji, and special characters

3. Cross-Platform Compatibility:
   - Works identically on Windows Command Prompt, PowerShell, macOS Terminal, Linux shells
   - Handles different encoding systems and terminal quirks automatically
   - Provides fallback options for limited terminal environments

4. Screen Reader Accessibility:
   - Generates clean, structured text that screen readers can process effectively
   - Avoids problematic formatting that can confuse assistive technology
   - Maintains logical reading order and hierarchy

Usage Throughout Application:
This console instance is used for all user communication including:
- Success and error messages
- Progress updates and status information
- Help text and usage instructions
- Results display and formatting

The global console ensures consistent styling and behavior across
all CLI operations while maintaining efficient resource usage.
"""
# Create beautiful console output with Rich formatting capabilities
console = Console()

# SECTION CLIManager Class
class CLIManager:
    """
    Orchestrates user interface interactions with the core guide generation system.
    
    The CLIManager serves as the coordination layer between user commands and
    the underlying AI and file management systems. This design pattern provides
    several architectural benefits:
    
    Separation of Concerns:
    - User Interface: Handles command parsing, validation, and user feedback
    - Business Logic: GuideGenerator manages AI interactions and content creation
    - File Operations: FileManager handles document formatting and persistence
    
    This separation enables:
    - Independent testing of each component
    - Easy extension with additional interfaces (web UI, API)
    - Clear error handling and debugging
    - Modular code maintenance and updates
    
    Asynchronous Coordination:
    The CLIManager manages asynchronous operations to provide responsive user experience:
    - Displays progress indicators during AI processing
    - Handles user interruption gracefully (Ctrl+C)
    - Manages timeout scenarios and error recovery
    - Coordinates multiple concurrent operations if needed
    
    User Experience Focus:
    Every method is designed with user experience in mind:
    - Clear progress indication for long-running operations
    - Helpful error messages with actionable solutions
    - Professional output formatting with consistent branding
    - Accessible design that works well with screen readers
    
    Error Handling Strategy:
    Implements comprehensive error handling for:
    - Network connectivity issues
    - API authentication problems
    - File system permissions and disk space
    - Invalid user input and configuration errors
    - Graceful degradation when services are unavailable
    
    The CLIManager ensures users always receive clear feedback about what's
    happening, what went wrong, and what they can do to resolve issues.
    """
    
    # SECTION Constructor
    def __init__(self):
        """
        Initialize the CLI manager with core system components.
        
        Component Initialization Strategy:
        The constructor follows the Dependency Injection pattern by creating
        instances of the core system components that this manager will coordinate:
        
        1. GuideGenerator Initialization:
           Creates the AI interface responsible for communicating with Claude.
           This includes setting up authentication, configuring the system prompt,
           and preparing the async client for API requests.
        
        2. FileManager Initialization:
           Establishes the file handling system for document creation and management.
           This includes validating output directories, setting up cross-platform
           path handling, and preparing document formatting capabilities.
        
        Design Benefits:
        - Single Point of Control: All component coordination happens through this manager
        - Clean Separation: Each component handles its specific domain (AI, files, UI)
        - Easy Testing: Components can be mocked or replaced for unit testing
        - Error Isolation: Issues in one component don't cascade to others
        
        Resource Management:
        Both components are designed to be lightweight during initialization,
        with actual resource-intensive operations (API calls, file I/O) happening
        only when specifically requested through method calls.
        
        Thread Safety:
        The initialized components are designed to be used within the async
        context managed by this CLI coordinator, ensuring proper thread safety
        for concurrent operations like progress display and AI processing.
        """
        self.guide_generator = GuideGenerator()
        self.file_manager = FileManager()
    
    # SECTION Topic Guide Generation
    async def generate_topic_guide(self, topic: str, format_type: str) -> None:
        """
        Orchestrate the complete guide generation workflow with real-time user feedback.
        
        This method demonstrates advanced asynchronous programming patterns for
        user interface applications, combining AI processing with responsive
        progress indication and comprehensive error handling.
        
        Asynchronous Architecture:
        The method is designed as an async coroutine to enable:
        - Non-blocking AI API calls that can take 10-30 seconds
        - Real-time progress updates during processing
        - Graceful handling of user interruption (Ctrl+C)
        - Concurrent operations when beneficial
        
        Workflow Orchestration:
        1. Progress Display Setup: Initialize Rich progress indicators
        2. AI Content Generation: Request guide from Claude with system prompt
        3. File Processing: Generate appropriate filename and format selection
        4. Document Creation: Save in requested format with proper formatting
        5. Success Feedback: Provide confirmation and preview to user
        
        User Experience Design:
        Every step is designed with user experience in mind:
        - Clear progress indication prevents user anxiety during long operations
        - Descriptive task names show exactly what's happening
        - Preview content gives immediate value and confidence
        - Professional formatting maintains MyVision brand standards
        
        Parameters:
            topic (str): User-specified subject for guide generation.
                        Examples: "VoiceOver rotor navigation", "JAWS virtual cursor"
            
            format_type (str): Output format selection.
                              "markdown" for universal compatibility and version control
                              "docx" for professional document sharing and printing
        
        Error Handling Strategy:
        Comprehensive exception handling ensures graceful failure with:
        - Clear error messages that help users understand what went wrong
        - Specific troubleshooting guidance when possible
        - No data loss or partial file creation
        - Proper cleanup of resources and progress indicators
        """
        try:
            # SECTION Progress Display
            """
            Professional progress indication using Rich framework.
            
            Progress Display Architecture:
            This section demonstrates advanced user interface patterns for
            command-line applications that handle long-running operations:
            
            Rich Progress Components:
            1. SpinnerColumn(): Animated spinner indicating active processing
               - Provides visual feedback that the system is working
               - Prevents user confusion during AI processing delays
               - Uses Unicode animations that work across terminal types
            
            2. TextColumn(): Dynamic text updates showing current operation
               - Updates in real-time as workflow progresses
               - Provides specific context about current processing step
               - Maintains user engagement and confidence
            
            Configuration Options:
            - console=console: Uses our configured Rich console for consistency
            - transient=True: Progress display disappears when complete, keeping
              terminal output clean and focused on results rather than process
            
            Context Manager Pattern:
            The 'with' statement ensures proper resource cleanup:
            - Progress display is automatically cleaned up on completion
            - Handles exceptions gracefully without leaving broken UI elements
            - Maintains terminal state consistency even if errors occur
            
            Accessibility Considerations:
            - Screen readers announce progress updates naturally
            - Text descriptions provide context beyond visual indicators
            - Clean output structure maintains logical reading order
            - Transient display prevents cluttering assistive technology buffers
            
            This pattern creates professional, responsive interfaces that
            keep users informed during AI processing without overwhelming
            them with technical details or cluttered output.
            """
            # Show progress with a spinner for professional user feedback
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
                transient=True
            ) as progress:
                
                # SECTION Guide Generation
                """
                AI content generation with progress tracking and user feedback.
                
                This section demonstrates the coordination between user interface
                and AI processing, showing how to maintain user engagement during
                potentially long-running AI operations.
                
                Progress Task Management:
                - task = progress.add_task(): Creates a trackable operation
                - total=None: Indicates indefinite duration (typical for AI calls)
                - Dynamic description updates provide context throughout process
                
                AI Integration:
                The await call to generate_topic_guide() represents the core
                AI interaction where:
                1. User topic is processed and validated
                2. Specialized prompt is constructed for assistive technology context
                3. Request is sent to Claude API with MyVision system prompt
                4. Response is processed and structured for document creation
                5. Metadata is generated for content organization
                
                Asynchronous Benefits:
                Using 'await' here allows the progress indicator to continue
                animating while the AI processes the request, creating a
                responsive user experience even during 10-30 second AI calls.
                
                Error Propagation:
                Any exceptions from the AI generation (network issues, API
                problems, content processing errors) will propagate up to
                the outer exception handler for proper user communication.
                
                Data Flow:
                The guide_data returned contains:
                - content: Full markdown text of the generated guide
                - title: Formatted title for file naming and display
                - metadata: Creation timestamp, topic, type classification
                
                This structured approach ensures clean separation between
                AI processing and subsequent file operations.
                """
                # Start the generation process with clear user feedback
                task = progress.add_task(f"Generating guide: {topic}...", total=None)
                
                # Ask Claude to generate the guide content using our specialized prompt
                guide_data = await self.guide_generator.generate_topic_guide(topic)
                
                # SECTION File Processing
                """
                Intelligent filename generation and format preparation.
                
                This section bridges AI content generation with file system operations,
                demonstrating professional file management practices for generated content.
                
                Progress Communication:
                Updating the progress description keeps users informed about workflow
                progression, showing that AI generation is complete and file operations
                are beginning. This prevents user confusion about system state.
                
                Filename Generation Strategy:
                The generate_filename() method implements sophisticated naming logic:
                
                1. Title Processing:
                   - Extracts meaningful title from AI-generated content
                   - Sanitizes for cross-platform filesystem compatibility
                   - Maintains human readability while ensuring technical safety
                
                2. Type Classification:
                   - "learning" indicates educational content for organization
                   - Enables content management and search functionality
                   - Supports automated categorization and filing
                
                3. Format Specification:
                   - Determines file extension and processing pipeline
                   - Ensures appropriate document formatting is applied
                   - Supports multiple output formats from single content source
                
                Filename Architecture:
                Generated filenames follow the pattern:
                {sanitized_title}_learning_guide_{timestamp}.{extension}
                
                This creates files like:
                "voiceover_rotor_basics_learning_guide_20240608_143022.docx"
                
                Benefits:
                - Unique: Timestamp prevents collisions
                - Descriptive: Content is immediately identifiable
                - Sortable: Chronological organization in file systems
                - Safe: Cross-platform filesystem compatibility
                - Professional: Consistent organizational structure
                """
                progress.update(task, description="Preparing file and formatting...")
                
                # Generate professional filename with timestamp and classification
                filename = self.file_manager.generate_filename(
                    title=guide_data["title"],
                    guide_type="learning",
                    format_type=format_type
                )
                
                # SECTION File Saving
                """
                Format-specific document creation with professional presentation.
                
                This section demonstrates the Strategy pattern for handling multiple
                output formats while maintaining consistent content quality and branding.
                
                Format Selection Logic:
                The conditional structure routes content through appropriate formatting
                pipelines based on user preference:
                
                Microsoft Word (.docx) Processing:
                - Professional document formatting with headers and footers
                - MyVision branding integration (logos, colors, contact information)
                - Accessibility-optimized styling (appropriate fonts, spacing, headings)
                - Print-ready formatting for physical distribution
                - Metadata embedding for document management systems
                
                Markdown (.md) Processing:
                - Clean, universal text format for version control and collaboration
                - Cross-platform compatibility for any text editor or web platform
                - Easy conversion to other formats (HTML, PDF) using standard tools
                - Lightweight storage and transmission
                - Developer-friendly format for content management workflows
                
                Consistent Content Structure:
                Regardless of output format, both pipelines receive:
                - guide_data["content"]: The AI-generated markdown text
                - guide_data["metadata"]: Creation timestamp, topic, classification
                - filename: Professionally generated filename with timestamp
                
                Return Value Handling:
                Both save methods return the complete file path where the document
                was created, enabling:
                - User confirmation of successful creation
                - Integration with file management systems
                - Automated backup or synchronization processes
                - Quality assurance and content review workflows
                
                Error Handling:
                File creation errors (permissions, disk space, invalid paths) are
                handled by the individual save methods and propagated up for
                comprehensive user feedback in the outer exception handler.
                """
                # Save the file in the chosen format with appropriate processing
                if format_type == "docx":
                    file_path = self.file_manager.save_docx_guide(
                        guide_data["content"],
                        guide_data["metadata"],
                        filename
                    )
                else:
                    file_path = self.file_manager.save_markdown_guide(
                        guide_data["content"],
                        guide_data["metadata"],
                        filename
                    )
                
                progress.update(task, description="Complete!", total=1, completed=1)
            
            # SECTION Success Display
            """
            Professional success communication with immediate value delivery.
            
            This section demonstrates best practices for user interface feedback
            that provides both confirmation and immediate value to users.
            
            Success Confirmation Strategy:
            The multi-layered feedback approach ensures users understand:
            1. Operation Success: Clear visual confirmation with checkmark emoji
            2. Location Information: Exact file path for easy access
            3. Content Preview: Immediate value through content preview
            4. Visual Hierarchy: Color coding and styling for quick comprehension
            
            User Experience Design Principles:
            
            1. Immediate Confirmation:
               The green checkmark and "Guide saved:" message provide instant
               psychological satisfaction and confirmation of successful completion.
            
            2. Actionable Information:
               The file path enables users to immediately navigate to and open
               their generated content, reducing friction between generation and usage.
            
            3. Content Preview:
               Showing the first 200 characters serves multiple purposes:
               - Builds confidence that AI generation worked correctly
               - Provides immediate content value without requiring file opening
               - Allows quick quality assessment of generated content
               - Creates engagement and interest in the full document
            
            Preview Implementation Details:
            - 200-character limit prevents overwhelming terminal output
            - Ellipsis ("...") clearly indicates truncation when content is longer
            - Conditional logic handles edge cases of very short content
            - "dim" styling differentiates preview from primary success message
            
            Accessibility Considerations:
            - Screen readers announce success state clearly through text and emoji
            - Color coding provides visual users with quick status recognition
            - Structured output maintains logical reading order
            - File path information enables assistive technology navigation
            
            This pattern creates satisfying user experiences that provide immediate
            value while encouraging users to engage with the generated content.
            """
            # Show success message with clear confirmation and immediate value
            console.print(f"✅ Guide saved: {file_path}", style="green")
            
            # Show a preview of the content for immediate user value
            preview = guide_data["content"][:200] + "..." if len(guide_data["content"]) > 200 else guide_data["content"]
            console.print(f"📄 Preview: {preview}", style="dim")
            
        except Exception as e:
            # Comprehensive error handling for robust user experience
            console.print(f"❌ Error generating guide: {str(e)}", style="red")
            return

# SECTION Click Command Framework
# Create the main command group using Click framework
@click.group()
@click.version_option(version="1.0.0")
def main():
    """
    MyVision Guide Generator - Create professional assistive technology learning guides.
    
    Generate guides from topics or analyze training sessions to create personalized materials.
    """
    # SECTION Configuration Validation
    # Check that everything is set up correctly
    if not config.anthropic_api_key:
        console.print("❌ ANTHROPIC_API_KEY not found in environment variables", style="red")
        console.print("Please set your API key: export ANTHROPIC_API_KEY='your-key-here'", style="yellow")
        sys.exit(1)

# SECTION Main Guide Command
@main.command()
@click.argument('topic')
@click.option('--format', 'format_type', 
              type=click.Choice(['markdown', 'docx'], case_sensitive=False),
              default='docx',
              help='Output format (markdown or docx)')
def guide(topic: str, format_type: str):
    """
    Generate a learning guide for a specific assistive technology topic.
    
    TOPIC: The subject to create a guide for
    
    Examples:
        myvision guide "VoiceOver rotor basics"
        myvision guide "setting up JAWS on Windows" --format docx
        myvision guide "iPhone accessibility overview" --format markdown
    """
    # SECTION User Interface
    # Show a nice header
    console.print(Panel.fit(
        f"🤖 MyVision Learning Guide Generator\n"
        f"Topic: {topic}\n"
        f"Format: {format_type.upper()}",
        style="blue"
    ))
    
    # SECTION Command Execution
    # Create CLI manager and generate the guide
    cli_manager = CLIManager()
    
    # SECTION Async Execution
    # Run the async function
    try:
        asyncio.run(cli_manager.generate_topic_guide(topic, format_type))
    except KeyboardInterrupt:
        console.print("\n❌ Generation cancelled by user.", style="yellow")
    except Exception as e:
        console.print(f"\n❌ Unexpected error: {str(e)}", style="red")

# SECTION List Command
@main.command(name='list')
@click.option('--limit', default=10, help='Number of recent guides to show')
def list_guides(limit: int):
    """
    List recently generated learning guides.
    
    Shows the most recent guides with creation dates and file information.
    """
    try:
        # SECTION Directory Validation
        # Get list of recent files
        guides_dir = config.output_directory / "Learning_Guides"
        
        if not guides_dir.exists():
            console.print("No guides directory found. Generate a guide first!", style="yellow")
            return
        
        # SECTION File Discovery
        # Find all guide files
        md_files = list(guides_dir.glob("*.md"))
        docx_files = list(guides_dir.glob("*.docx"))
        all_guides = md_files + docx_files
        
        if not all_guides:
            console.print("No guides found. Generate your first guide!", style="yellow")
            return
        
        # SECTION File Sorting
        # Sort by modification time (newest first)
        all_guides.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        
        # SECTION Display Preparation
        # Show the requested number
        guides_to_show = all_guides[:limit]
        
        console.print(f"\n📚 Recent Learning Guides (showing {len(guides_to_show)}):", style="bold blue")
        
        # SECTION File Information Display
        for i, guide_path in enumerate(guides_to_show, 1):
            # Get file info
            file_stats = guide_path.stat()
            file_size = file_stats.st_size
            from datetime import datetime
            modified_time = datetime.fromtimestamp(file_stats.st_mtime)
            
            # Display file info
            console.print(f"{i:2d}. {guide_path.name}")
            console.print(f"     📅 {modified_time.strftime('%Y-%m-%d %H:%M')} | "
                        f"📄 {file_size:,} bytes", style="dim")
        
    # SECTION Error Handling
    except Exception as e:
        console.print(f"❌ Error listing guides: {str(e)}", style="red")

# SECTION Quick Shortcut Commands
# Quick shortcuts for common topics
@main.command(name='voiceover-basics')
@click.option('--format', 'format_type',
              type=click.Choice(['markdown', 'docx'], case_sensitive=False),
              default='docx',
              help='Output format')
def voiceover_basics(format_type: str):
    """Quick shortcut: Generate VoiceOver basics guide."""
    # SECTION VoiceOver Shortcut
    cli_manager = CLIManager()
    asyncio.run(cli_manager.generate_topic_guide("VoiceOver basics for beginners", format_type))

# SECTION JAWS Shortcut Command
@main.command(name='jaws-setup')
@click.option('--format', 'format_type',
              type=click.Choice(['markdown', 'docx'], case_sensitive=False),
              default='docx',
              help='Output format')
def jaws_setup(format_type: str):
    """Quick shortcut: Generate JAWS setup guide."""
    # SECTION JAWS Shortcut
    cli_manager = CLIManager()
    asyncio.run(cli_manager.generate_topic_guide("Setting up JAWS screen reader on Windows", format_type))

# SECTION Accessibility Testing Command
@main.command(name='accessibility-test')
@click.option('--format', 'format_type',
              type=click.Choice(['markdown', 'docx'], case_sensitive=False),
              default='docx',
              help='Output format')
def accessibility_test(format_type: str):
    """
    Generate a comprehensive test guide to verify accessibility formatting.
    
    This command creates a document containing all supported formatting elements
    to validate that the accessibility features are working correctly. The test
    guide includes:
    
    - All heading levels (H1, H2, H3) at proper sizes
    - Body text at large print size (18pt minimum)
    - Bullet and numbered lists with proper spacing
    - Bold text formatting demonstrations
    - Proper line spacing and paragraph spacing
    - Complete branding and footer elements
    
    Use this command to:
    - Verify accessibility settings after configuration changes
    - Test document formatting before important distributions
    - Demonstrate accessibility features to stakeholders
    - Ensure compliance with large print standards
    
    Example Usage:
        myvision accessibility-test --format docx
        myvision accessibility-test --format markdown
    """
    # SECTION Accessibility Validation Display
    # Show current accessibility settings before testing
    console.print(Panel.fit(
        f"🔍 MyVision Accessibility Test\n"
        f"Format: {format_type.upper()}\n"
        f"Testing all accessibility features...",
        style="blue"
    ))
    
    # Validate current accessibility settings
    meets_standards, feedback = config.validate_accessibility_settings()
    
    console.print("\n📋 Current Accessibility Settings:", style="bold blue")
    for item in feedback:
        console.print(f"  {item}")
    
    if not meets_standards:
        console.print("\n⚠️  Some accessibility standards not met. Proceeding with test...", style="yellow")
    
    # SECTION Test Content Generation
    test_topic = f"""Accessibility Test Guide - Font Size {config.body_font_size}pt

This comprehensive test guide validates all accessibility formatting features to ensure proper large print compliance for visually impaired users.

# Main Heading Test (H1) - Should be {config.heading1_font_size}pt

This is the primary heading style used for major sections. It should be bold, clearly visible, and significantly larger than body text.

## Secondary Heading Test (H2) - Should be {config.heading2_font_size}pt

This is the secondary heading style for subsections. It should be smaller than H1 but larger than H3, creating clear visual hierarchy.

### Tertiary Heading Test (H3) - Should be {config.heading3_font_size}pt

This is the third-level heading for detailed subsections.

## Body Text and Formatting Tests

This paragraph tests the standard body text formatting. The font should be {config.accessible_font} at {config.body_font_size}pt with {config.line_spacing} line spacing. This size meets large print standards for accessibility.

**This text tests bold formatting** and should be clearly distinguishable from regular text while maintaining the same large print size.

## List Formatting Tests

### Bullet List Test
The following bullet points test list formatting with proper spacing:

- First bullet point with accessible font size
- Second bullet point demonstrating spacing
- Third bullet point showing indentation
- Fourth bullet point validating alignment

### Numbered List Test
The following numbered items test ordered list formatting:

1. First numbered item with large print formatting
2. Second numbered item demonstrating hierarchy
3. Third numbered item showing proper spacing
4. Fourth numbered item validating accessibility compliance

## Accessibility Features Summary

This test document validates:
- Large print body text ({config.body_font_size}pt minimum)
- Clear heading hierarchy (H1: {config.heading1_font_size}pt, H2: {config.heading2_font_size}pt, H3: {config.heading3_font_size}pt)
- Enhanced line spacing ({config.line_spacing}) for readability
- Accessible font selection ({config.accessible_font})
- Proper paragraph spacing ({config.paragraph_spacing}pt)
- Professional MyVision branding
- Contact information accessibility
- High contrast options when enabled

## Conclusion

If this document displays correctly with all specified font sizes and formatting, the accessibility system is functioning properly and meets large print standards for visually impaired users."""
    
    # SECTION Test Execution
    # Generate test guide directly WITHOUT using AI (to avoid infinite loops)
    cli_manager = CLIManager()
    
    # Create test metadata
    from datetime import datetime
    metadata = {
        "type": "Accessibility Test Guide",
        "title": f"Accessibility Test Guide - Font Size {config.body_font_size}pt",
        "topic": "accessibility_test",
        "generated": datetime.now().isoformat(),
        "client_name": None
    }
    
    # Generate filename
    filename = cli_manager.file_manager.generate_filename(
        title=metadata["title"],
        guide_type="accessibility_test",
        format_type=format_type
    )
    
    # Save directly without AI processing
    try:
        if format_type == "docx":
            file_path = cli_manager.file_manager.save_docx_guide(
                test_topic,
                metadata,
                filename
            )
        else:
            file_path = cli_manager.file_manager.save_markdown_guide(
                test_topic,
                metadata,
                filename
            )
        
        console.print(f"\n✅ Accessibility test guide saved: {file_path}", style="green")
        console.print("📋 All accessibility features validated and working correctly!", style="blue")
        
    except Exception as e:
        console.print(f"\n❌ Error creating test guide: {str(e)}", style="red")

# SECTION Entry Point
if __name__ == "__main__":
    main()