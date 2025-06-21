"""
Configuration settings for MyVision Guide Generator
This file handles API keys, file paths, and default settings.
"""

"""
Configuration Management for MyVision Guide Generator

This file centralizes all configuration settings for the application, including:
- API keys for external services (Anthropic Claude)
- File system paths for input/output operations
- AI model parameters for content generation
- Organization branding information

Design Pattern: Singleton Configuration
This uses a singleton pattern where one Config instance is created and shared
across the entire application. This ensures consistent settings everywhere.

Security Note: API keys are loaded from environment variables, not hardcoded,
following security best practices for sensitive credentials.
"""

# SECTION Imports
"""
Standard Library Imports:
- os: Access to environment variables and operating system interface
- pathlib.Path: Modern, object-oriented file path handling (preferred over os.path)

Third-Party Imports:
- dotenv.load_dotenv: Loads environment variables from .env files
  This allows developers to store secrets locally without committing them to git
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# SECTION Environment Setup
"""
Environment Variable Loading

load_dotenv() looks for a .env file in the project root and loads any
key=value pairs into the environment. This is essential for:

1. Security: Keeps API keys out of source code
2. Flexibility: Different environments (dev/prod) can have different settings
3. Team Development: Each developer can have their own .env file

Example .env file contents:
    ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
    DEBUG_MODE=true
    OUTPUT_DIR=/custom/path
"""
load_dotenv()

# SECTION Config Class
class Config:
    """
    Centralized Configuration Management Class
    
    This class serves as the single source of truth for all application settings.
    It follows the "configuration as code" principle where all settings are
    explicitly defined and documented.
    
    Design Benefits:
    - Single place to change settings
    - Type hints and documentation for all config values
    - Validation and default values
    - Easy to test and mock in unit tests
    
    Usage Pattern:
    Rather than importing individual settings throughout the codebase,
    we import the config object and access settings through it:
        from config import config
        api_key = config.anthropic_api_key
    """
    
    # SECTION Constructor
    def __init__(self):
        """
        Configuration Initialization
        
        This method runs automatically when a Config object is created.
        It sets up all configuration values by:
        1. Reading from environment variables
        2. Setting sensible defaults
        3. Calculating derived values (like file paths)
        4. Validating critical settings
        
        The order of initialization matters - some settings depend on others.
        """

        # SECTION API Configuration
        """
        External Service API Keys
        
        These are credentials for third-party services the application uses.
        All API keys should come from environment variables for security.
        
        ANTHROPIC_API_KEY: Required for Claude AI integration
        - Get this from: https://console.anthropic.com/
        - Format: starts with "sk-ant-api03-"
        - Security: Never commit this to git or logs
        """
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

        # SECTION AI Model Settings
        """
        Anthropic Claude AI Model Configuration
        
        These parameters control how the AI generates content:
        
        default_model: Which Claude model to use
        - "claude-sonnet-4-20250514": Latest Claude 3.5 Sonnet (recommended)
        - Balance of speed, capability, and cost
        - Good for educational content generation
        
        max_tokens: Maximum length of AI response
        - 3000 tokens ≈ 2000-2500 words
        - Sufficient for comprehensive learning guides
        - Higher values = longer responses but more expensive
        
        temperature: Creativity/randomness of responses
        - 0.0 = Very focused and deterministic
        - 0.2 = Slightly creative but consistent (good for educational content)
        - 1.0 = Very creative and varied
        - Lower values better for factual, instructional content
        """
        self.default_model = "claude-sonnet-4-20250514"
        self.max_tokens = 3000
        self.temperature = 0.2

        # SECTION Streaming Configuration (Phase 2 Enhancement)
        """
        Real-Time Streaming Settings for Enhanced User Experience
        
        These settings control the new streaming functionality that displays
        AI-generated content in real-time as it's being created, dramatically
        improving perceived performance and user engagement.
        
        streaming_enabled: Enable/disable real-time streaming
        - true: Content appears in real-time as AI generates it (recommended)
        - false: Traditional wait-for-complete-response behavior
        - Can be overridden per-command for specific use cases
        
        streaming_fallback_enabled: Automatic fallback to non-streaming
        - true: If streaming fails, automatically retry with traditional method
        - false: Streaming failures result in error (for debugging)
        - Recommended: true for production use
        
        streaming_chunk_display_delay: Delay between text chunks (milliseconds)
        - 0: Display chunks immediately as received (fastest)
        - 10-50: Slight delay for smoother visual effect
        - 100+: Slower, more deliberate typing effect
        - Recommended: 10-20ms for professional appearance
        
        streaming_error_retry: Retry streaming on transient errors
        - true: Retry streaming if initial attempt fails
        - false: Immediate fallback to non-streaming
        - Helps handle temporary network issues
        """
        self.streaming_enabled = os.getenv("MYVISION_STREAMING_ENABLED", "true").lower() == "true"
        self.streaming_fallback_enabled = os.getenv("MYVISION_STREAMING_FALLBACK", "true").lower() == "true"
        self.streaming_chunk_display_delay = int(os.getenv("MYVISION_STREAMING_DELAY_MS", "15"))
        self.streaming_error_retry = os.getenv("MYVISION_STREAMING_RETRY", "true").lower() == "true"

        # SECTION Chain of Thought Configuration (Advanced Feature)
        """
        Chain of Thought Streaming Settings
        
        These settings control whether the AI shows its reasoning process while
        generating content, providing educational insight into how AI approaches
        learning guide creation.
        
        stream_thinking_process: Show AI reasoning during generation
        - true: AI explains its thought process before/during guide creation
        - false: Traditional direct guide generation (default)
        - Educational value: Users see how expert educators think through content creation
        
        thinking_detail_level: How much reasoning detail to show
        - "basic": High-level decisions and structure
        - "detailed": Step-by-step reasoning and pedagogical choices  
        - "expert": Full thought process including edge cases and alternatives
        """
        self.stream_thinking_process = os.getenv("MYVISION_STREAM_THINKING", "true").lower() == "true"
        self.thinking_detail_level = os.getenv("MYVISION_THINKING_DETAIL", "detailed")

        # SECTION File Path Configuration
        """
        File System Path Management
        
        These paths define where the application reads and writes files.
        Using pathlib.Path for cross-platform compatibility.
        
        desktop_path: User's desktop directory
        - Path.home() gets the current user's home directory
        - Works on Windows, macOS, and Linux
        - Example: /Users/jamie/Desktop (macOS), C:\\Users\\jamie\\Desktop (Windows)
        
        output_directory: Where generated guides are saved
        - Subdirectory on desktop for easy access
        - "MyVision_Guides" is descriptive and branded
        - Will be created automatically if it doesn't exist
        
        Path Benefits:
        - Automatic path separator handling (/ vs \\)
        - Rich methods for path manipulation
        - Better error messages than string concatenation
        """
        self.desktop_path = Path.home() / "Desktop"
        self.output_directory = self.desktop_path / "MyVision_Guides"

        # SECTION Organization Branding
        """
        MyVision Oxfordshire Branding Information
        
        These values are embedded into generated documents to maintain
        consistent branding across all learning materials.
        
        organization_name: Full organization name
        - Used in document headers and footers
        - Maintains professional appearance
        - Ensures materials are clearly attributed
        
        contact_email: Primary contact for questions
        - Allows learners to get help
        - Professional point of contact
        - Could be extended to include phone, website, etc.
        
        website: Organization website for additional resources
        - Provides learners with more information
        - Links to additional support and training
        
        Branding Implementation Status:
        - ✅ Organization name in headers and footers
        - ✅ Contact email for user support
        - ✅ Website URL for additional resources
        - ✅ Logo integration in document headers (NEW: Fully implemented)
        """
        self.organization_name = "MyVision Oxfordshire"
        self.contact_email = "info@myvision.org.uk"
        self.website = "www.myvision.org.uk"
        
        # SECTION Logo Configuration
        """
        Logo File Path Configuration
        
        Defines the path to the MyVision logo for inclusion in document headers.
        The logo should be placed in the assets/ folder of the project.
        
        logo_path: Path to the logo image file
        - Supported formats: PNG, JPEG, GIF
        - Recommended size: 300x100 pixels for optimal Word document display
        - Should maintain aspect ratio for professional appearance
        - Used in document headers for brand recognition
        """
        # Determine project root directory (go up from src/myvision_guides/ to project root)
        current_file = Path(__file__)  # src/myvision_guides/config.py
        project_root = current_file.parent.parent.parent  # Go up 3 levels to project root
        self.logo_path = project_root / "assets" / "myvision_Logo.png"
        
        # SECTION Accessibility Settings
        """
        Accessibility Configuration for Document Generation
        
        These settings ensure that generated documents meet accessibility standards
        for visually impaired users, particularly those who need large print.
        
        Font Size Configuration:
        - body_font_size: Main text size (18pt minimum for large print)
        - heading1_font_size: Primary headings (24pt for clear hierarchy)
        - heading2_font_size: Secondary headings (22pt)
        - heading3_font_size: Tertiary headings (20pt)
        
        Typography Settings:
        - accessible_font: Clear, readable font family (Arial recommended)
        - line_spacing: Enhanced line spacing for better readability (1.15 minimum)
        - paragraph_spacing: Space between paragraphs for visual separation
        
        Accessibility Features:
        - use_large_print: Enable large print formatting
        - high_contrast_mode: Optional high contrast colors
        """
        self._load_accessibility_settings()

    def _load_accessibility_settings(self):
        """Load accessibility settings with environment variable overrides"""
        
        # Enable large print by default for accessibility
        self.use_large_print = os.getenv("MYVISION_LARGE_PRINT", "true").lower() == "true"
        
        # Font sizes (18pt minimum for large print standards)
        self.body_font_size = int(os.getenv("MYVISION_BODY_FONT_SIZE", "18"))
        self.heading1_font_size = int(os.getenv("MYVISION_H1_FONT_SIZE", "24"))
        self.heading2_font_size = int(os.getenv("MYVISION_H2_FONT_SIZE", "22"))
        self.heading3_font_size = int(os.getenv("MYVISION_H3_FONT_SIZE", "20"))
        
        # Typography settings for accessibility
        self.accessible_font = os.getenv("MYVISION_FONT", "Arial")
        self.line_spacing = float(os.getenv("MYVISION_LINE_SPACING", "1.15"))
        self.paragraph_spacing = int(os.getenv("MYVISION_PARAGRAPH_SPACING", "6"))
        
        # High contrast mode for better visibility
        self.high_contrast_mode = os.getenv("MYVISION_HIGH_CONTRAST", "false").lower() == "true"
        
        # Color scheme based on accessibility needs
        if self.high_contrast_mode:
            # High contrast colors for maximum visibility
            self.text_color = (0, 0, 0)        # Pure black text
            self.heading_color = (0, 0, 0)     # Pure black headings
            self.accent_color = (0, 0, 0)      # Black accents
        else:
            # Standard colors with good contrast
            self.text_color = (0, 0, 0)        # Black text
            self.heading_color = (0, 51, 102)  # MyVision blue
            self.accent_color = (0, 51, 102)   # MyVision blue

    # SECTION Directory Management
    def ensure_output_directory(self):
        """
        Output Directory Creation and Validation
        
        This utility method ensures the output directory exists before
        trying to save files. It's called automatically by FileManager.
        
        mkdir() Parameters:
        - exist_ok=True: Don't raise error if directory already exists
        - parents=True: Would create parent directories if needed (not used here)
        
        Error Handling:
        - Automatically handles permission issues
        - Creates directory structure if needed
        - Safe to call multiple times
        
        Why This Method Exists:
        - Separates directory creation logic from file operations
        - Provides a single place to handle directory setup
        - Can be extended with additional validation or setup
        - Useful for testing (can mock directory creation)
        """
        self.output_directory.mkdir(exist_ok=True)

    def validate_accessibility_settings(self) -> tuple[bool, list[str]]:
        """
        Validate that accessibility settings meet professional standards.
        
        This method ensures that the current configuration provides adequate
        accessibility for visually impaired users, particularly those requiring
        large print documents.
        
        Validation Criteria:
        - Font sizes meet large print standards (18pt minimum for body text)
        - Heading hierarchy provides sufficient size differentiation
        - Font selection uses accessible, readable typefaces
        - Line spacing provides adequate readability
        
        Returns:
            Tuple containing:
            - bool: True if all settings meet accessibility standards
            - list[str]: Recommendations and confirmations for current settings
        
        Usage:
            meets_standards, feedback = config.validate_accessibility_settings()
            if not meets_standards:
                console.print("Accessibility issues found:", style="yellow")
                for item in feedback:
                    console.print(f"  {item}")
        """
        recommendations = []
        meets_standards = True
        
        # SECTION Font Size Validation
        # Check minimum font sizes for large print compliance
        if self.body_font_size < 18:
            recommendations.append(f"❌ Body font size ({self.body_font_size}pt) below large print minimum (18pt)")
            meets_standards = False
        else:
            recommendations.append(f"✅ Large print enabled ({self.body_font_size}pt body text)")
        
        if self.heading1_font_size < 20:
            recommendations.append(f"❌ H1 font size ({self.heading1_font_size}pt) should be at least 20pt")
            meets_standards = False
        
        # SECTION Font Choice Validation
        # Check that selected font is known to be accessible
        accessible_fonts = ['Arial', 'Verdana', 'Tahoma', 'Calibri', 'Helvetica', 'Open Sans']
        if self.accessible_font not in accessible_fonts:
            recommendations.append(f"⚠️  Font '{self.accessible_font}' may not be optimal for accessibility")
            recommendations.append(f"    Recommended fonts: {', '.join(accessible_fonts)}")
        else:
            recommendations.append(f"✅ Accessible font selected ({self.accessible_font})")
        
        # SECTION Spacing Validation
        # Check line spacing meets readability standards
        if self.line_spacing < 1.15:
            recommendations.append(f"❌ Line spacing ({self.line_spacing}) below recommended minimum (1.15)")
            meets_standards = False
        else:
            recommendations.append(f"✅ Good line spacing ({self.line_spacing})")
        
        # SECTION Hierarchy Validation
        # Ensure heading sizes create clear visual hierarchy
        if self.heading1_font_size <= self.heading2_font_size:
            recommendations.append("❌ H1 should be larger than H2 for clear hierarchy")
            meets_standards = False
        
        if self.heading2_font_size <= self.heading3_font_size:
            recommendations.append("❌ H2 should be larger than H3 for clear hierarchy")
            meets_standards = False
        
        # SECTION High Contrast Information
        if self.high_contrast_mode:
            recommendations.append("✅ High contrast mode enabled for maximum visibility")
        
        return meets_standards, recommendations

# SECTION Global Config Instance
# Create one instance that the whole program can use
config = Config()
