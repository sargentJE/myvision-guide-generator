# Step 7: Professional Packaging & Distribution 🚀
*Transform Your Code Into a Professional CLI Tool*

## 🎯 Learning Objectives

By the end of this step, you will:
- ✅ Understand how professional CLI tools are packaged and distributed
- ✅ Convert your project files into an installable Python package
- ✅ Create command-line entry points that work system-wide
- ✅ Test and validate your complete CLI tool installation
- ✅ Prepare your tool for sharing with others
- ✅ Troubleshoot common packaging issues like a pro

**🏆 Success Criteria:** You can type `myvision guide "any topic"` from any directory on your system and it generates perfect guides instantly.

## 🔍 Pre-Flight Checklist

Before starting this step, verify you have:
- [ ] Completed Steps 1-6 successfully
- [ ] All your Python files working in the `src/myvision_guides/` directory
- [ ] Your CLI interface responding to `python src/myvision_guides/cli.py --help`
- [ ] A working virtual environment with all dependencies
- [ ] Basic understanding of command-line navigation

**⚠️ Critical Check:** Run this test to ensure you're ready:
```bash
cd /path/to/your/project
python src/myvision_guides/cli.py guide "Test Topic" --format markdown
```
If this doesn't work, revisit Step 6 before continuing.

## 🤔 Why Professional Packaging Matters

### The Transformation Story

**Before (Development Version):**
```bash
# User wants to generate a guide
cd /Users/trainer/myvision-project/src/myvision_guides
python cli.py guide "iPad accessibility" --format word
# Works, but only from this specific directory
```

**After (Professional Version):**
```bash
# User wants to generate a guide
myvision guide "iPad accessibility" --format word
# Works from anywhere on the system, just like professional tools
```

### Real-World Professional Benefits

**For MyVision Trainers:**
- **Instant Access:** Type `myvision` from any directory - Desktop, Documents, Downloads
- **Professional Feel:** Tool behaves like Microsoft Word, Adobe Photoshop, or any commercial software
- **Easy Sharing:** Send colleagues a simple installer - no technical setup required
- **System Integration:** Tool appears in system PATH, can be called from scripts

**For Technical Users:**
- **Clean Development:** Separate source code from installed tool
- **Version Control:** Easy updates and rollbacks
- **Dependency Management:** Automatic installation of required libraries
- **Cross-Platform:** Same tool works on Windows, macOS, and Linux

## 📚 Essential Concepts: From Code to Professional Tool

### The Kitchen Analogy 🍳

Think of packaging like transforming a home kitchen recipe into a restaurant-quality meal system:

**Your Current State (Home Kitchen):**
- Loose recipe files scattered around
- Must be in specific kitchen to cook
- Recipe only works for the chef who wrote it
- Ingredients must be gathered manually each time

**Professional Package (Restaurant Kitchen):**
- Complete meal system with all components
- Works in any kitchen location
- Anyone can use it with simple instructions
- All ingredients automatically available
- Consistent results every time

### Code Evolution Journey

**Stage 1: Individual Scripts (Where You Started)**
```
my_script.py    # python3 my_script.py
```
Like a handwritten recipe on a napkin - works, but not professional.

**Stage 2: Organized Modules (Steps 1-6)**
```
src/myvision_guides/
├── __init__.py    # Package marker
├── cli.py         # Command interface
├── config.py      # Settings
└── file_manager.py # File operations
```
Like a well-organized recipe binder - better, but still requires chef knowledge.

**Stage 3: Professional Package (This Step)**
```
myvision-guide-generator/
├── src/myvision_guides/  # Source code
├── setup.py              # Installation instructions
├── requirements.txt      # Ingredient list
└── README.md            # User manual
```
Like a complete restaurant meal kit - anyone can create perfect results.

### What Professional Packaging Gives You

**🎯 Single Command Access:**
```bash
# Instead of this complex process:
cd /Users/trainer/project/src/myvision_guides
python cli.py guide "topic" --format word

# You get this simple command:
myvision guide "topic" --format word
```

**🔄 System-Wide Availability:**
- Works from Desktop, Documents, Downloads - anywhere
- No need to remember file paths
- Command appears in system autocomplete
- Can be called from other scripts or shortcuts

**🛡️ Dependency Management:**
- Automatically installs required libraries
- Prevents version conflicts
- Isolates your tool from other Python projects
- Updates are managed centrally

## 🛠️ Step-by-Step Implementation: Creating Your Package

### Step 7.1: The `setup.py` Blueprint - Your Package's DNA

**🤔 What is `setup.py`?**

`setup.py` is the most important file for packaging. It's a Python script that tells `pip` (Python's package installer) everything it needs to know about your project:
- What your package is called
- What version it is
- Who wrote it
- What files to include
- What other libraries it needs (dependencies)
- How to create the `myvision` command

**1. Create `setup.py` in Your Project Root**

   - Navigate to your main project folder (`myvision-guide-generator`).
   - Create a new file named `setup.py`.

   Your project structure should now look like this:
   ```
   myvision-guide-generator/
   ├── src/
   │   └── myvision_guides/
   │       ├── __init__.py
   │       ├── cli.py
   │       ├── config.py
   │       └── ... (other .py files)
   ├── setup.py  <-- NEW FILE HERE
   ├── requirements.txt
   └── README.md
   ```

**2. Add the Following Code to `setup.py`:**

   ```python
   # /Users/jamiesargent/myvision-guide-generator/setup.py
   from setuptools import setup, find_packages
   
   # Read requirements from requirements.txt for consistency
   with open("requirements.txt", "r", encoding="utf-8") as fh:
       requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
   
   setup(
       # == Package Metadata ==
       name="myvision-guides",  # How users will `pip install` it
       version="1.0.0",          # Your tool's current version (Major.Minor.Patch)
       author="MyVision Oxfordshire",
       author_email="info@myvision.org.uk",
       description="AI-powered CLI tool for generating assistive technology learning guides",
       long_description=open("README.md").read(), # Uses your README for details
       long_description_content_type="text/markdown",
       url="https://github.com/MyVisionOxfordshire/myvision-guide-generator", # Project URL
   
       # == Source Code Location ==
       # Tells setuptools our code is in the 'src' directory
       package_dir={"": "src"},
       # Automatically find all packages (directories with __init__.py) in 'src'
       packages=find_packages(where="src"),
   
       # == Dependencies ==
       # Minimum Python version required
       python_requires=">=3.8",
       # List of libraries your tool needs (from requirements.txt)
       install_requires=requirements,
   
       # == Command-Line Interface (CLI) Setup ==
       # This is CRITICAL for creating the `myvision` command
       entry_points={
           "console_scripts": [
               "myvision=myvision_guides.cli:main",  # command_name=package.module:function
           ],
       },
   
       # == Classifiers (Optional but Recommended) ==
       # Helps users find your package on PyPI (Python Package Index)
       classifiers=[
           "Development Status :: 5 - Production/Stable",
           "Intended Audience :: Education",
           "Intended Audience :: Healthcare Industry",
           "License :: OSI Approved :: MIT License", # Choose your license
           "Natural Language :: English",
           "Programming Language :: Python :: 3",
           "Programming Language :: Python :: 3.8",
           "Programming Language :: Python :: 3.9",
           "Programming Language :: Python :: 3.10",
           "Programming Language :: Python :: 3.11",
           "Programming Language :: Python :: 3.12",
           "Topic :: Education",
           "Topic :: Utilities",
           "Environment :: Console", # Indicates it's a CLI tool
           "Operating System :: OS Independent", # Works on Win, macOS, Linux
       ],
   
       # == Include Non-Python Files (like your logo) ==
       include_package_data=True, # Tells setuptools to respect MANIFEST.in (if you add one)
       # Or, explicitly list data files if not using MANIFEST.in for simple cases:
       package_data={
           # If your package 'myvision_guides' needs to access files within itself
           # (e.g., templates or assets NOT in the main 'assets' folder for the package itself)
           # 'myvision_guides': ['path/to/data_file_inside_package.dat'],
           # For your current structure, assets are outside the 'src' package, handled differently.
           # If assets/myvision_Logo.png needs to be part of the *installable package data* and not just
           # referenced by an absolute path from config.py, you'd need a MANIFEST.in or more complex setup.
           # For now, config.py uses an absolute path relative to its own location, which is fine for this project.
       },
   )
   ```

**3. Understanding Key Parts of `setup.py`:**

   - **`name="myvision-guides"`**: This is the official name for `pip`. Users will type `pip install myvision-guides`.
   - **`version="1.0.0"`**: Crucial for updates. Increment this (e.g., to `1.0.1` or `1.1.0`) when you release changes.
   - **`package_dir={"": "src"}`**: Tells `setup` that your actual Python code (the `myvision_guides` package) is inside the `src` folder.
   - **`packages=find_packages(where="src")`**: Automatically finds your `myvision_guides` package within `src` because it has an `__init__.py` file.
   - **`install_requires=requirements`**: Automatically installs all libraries listed in your `requirements.txt` when someone installs your tool. This is why we read `requirements.txt` at the top.
   - **`entry_points`**: This is the magic part! ✨
     - `"console_scripts": ["myvision=myvision_guides.cli:main"]`
     - This tells Python: "When a user types `myvision` in the terminal, run the `main` function inside the `cli.py` file, which is part of the `myvision_guides` package."

**✅ Validation: Does `setup.py` Look Correct?**
   - Double-check all paths and names.
   - Ensure `requirements.txt` is in the same directory as `setup.py`.
   - Confirm your main CLI function is indeed `main` in `src/myvision_guides/cli.py`.

### Step 7.2: Understanding `__init__.py` - The Package Marker

**🤔 What is `__init__.py`?**

   - The `src/myvision_guides/__init__.py` file tells Python that the `myvision_guides` directory is a "package" (a collection of modules).
   - It can be empty, or it can contain package-level initializations or variables.

**1. Your Current `__init__.py` (from Step 3):**

   Located at `src/myvision_guides/__init__.py`:
   ```python
   # src/myvision_guides/__init__.py
   """
   MyVision Guide Generator
   
   A CLI tool for creating assistive technology learning guides.
   """
   
   __version__ = "1.0.0" 
   # This makes `myvision_guides.__version__` available after import.
   # It's good practice to sync this with setup.py's version.
   ```

**2. Importance for Packaging:**
   - `find_packages(where="src")` in `setup.py` specifically looks for directories containing `__init__.py` to identify them as packages to include.
   - Without `__init__.py`, `src/myvision_guides` would just be a regular folder, not an importable Python package.

**✅ Validation: Is `__init__.py` Present and Correct?**
   - Ensure `src/myvision_guides/__init__.py` exists.
   - For consistency, make sure the `__version__` here matches the `version` in `setup.py`.

### Step 7.3: The Installation - Making `myvision` Command Work!

Now, let's install your package so the `myvision` command becomes available system-wide (within your active virtual environment).

**1. Open Your Terminal**

   - Make sure you are in your project's root directory (`myvision-guide-generator`), where `setup.py` is located.
   - **Crucially, ensure your virtual environment from Step 2 is activated!**
     ```bash
     # If not already in your project directory:
     cd /path/to/your/myvision-guide-generator
     
     # Activate virtual environment (macOS/Linux example):
     source venv/bin/activate
     # (Windows example: venv\Scripts\activate)
     ```
     You should see `(venv)` at the beginning of your terminal prompt.

**2. Install Your Package in "Editable" Mode**

   We use "editable" mode (`-e`) for development. This means if you change your Python code, the installed command updates automatically without needing to reinstall.

   ```bash
   pip install -e .
   ```
   - **`pip install`**: The standard Python command to install packages.
   - **`-e`**: Stands for "editable". This creates a link to your source code instead of copying it. Perfect for development!
   - **`.`**: Means "install the package in the current directory" (referring to your `setup.py`).

**3. What `pip install -e .` Does:**
   - Reads `setup.py`.
   - Resolves and installs any missing dependencies from `install_requires` (which came from `requirements.txt`).
   - Creates the `myvision` command and links it to `src/myvision_guides/cli.py`'s `main` function.
   - Makes your `myvision_guides` package importable from anywhere (e.g., `import myvision_guides`).

**Expected Output (will vary slightly):**
```
Obtaining file:///Users/jamiesargent/myvision-guide-generator
  Preparing metadata (setup.py) ... done
Requirement already satisfied: click>=8.0 in ./venv/lib/python3.12/site-packages (from myvision-guides==1.0.0) (8.1.7)
Requirement already satisfied: python-dotenv>=0.20 in ./venv/lib/python3.12/site-packages (from myvision-guides==1.0.0) (1.0.1)
...
Installing collected packages: myvision-guides
  Running setup.py develop for myvision-guides
Successfully installed myvision-guides-1.0.0
```
Look for "Successfully installed myvision-guides-1.0.0".

**✅ Validation: Is Your Tool Installed?**

Let's test if the `myvision` command now works from anywhere!

**Test 1: Check `pip list`**
   This command shows all packages installed in your current environment.
   ```bash
   pip list | grep myvision
   ```
   You should see something like:
   ```
   myvision-guides    1.0.0    /Users/jamiesargent/myvision-guide-generator
   ```
   The path at the end confirms it's an editable install linked to your project folder.

**Test 2: Find the Command with `which` (macOS/Linux) or `where` (Windows)**
   This tells you where the system found the `myvision` command.
   ```bash
   # For macOS/Linux:
   which myvision
   # Expected output (will be inside your venv/bin):
   # /Users/jamiesargent/myvision-guide-generator/venv/bin/myvision
   
   # For Windows (in Command Prompt or PowerShell):
   # where myvision
   # Expected output (will be inside your venv\Scripts):
   # C:\Users\YourUser\myvision-guide-generator\venv\Scripts\myvision.exe
   ```
   If this shows a path, it's a great sign!

**Test 3: Run Your CLI Tool!**
   This is the ultimate test. Try running your help command.
   ```bash
   myvision --help
   ```
   You should see the familiar help output from your Click application (from Step 6).

   Now try generating a guide:
   ```bash
   myvision guide "Testing packaging" --format markdown
   ```
   This should create a new guide in your `MyVision_Guides` desktop folder.

   **🎉 If these commands work, congratulations! You've successfully packaged your tool! 🎉**

### Step 7.4: Understanding Import Resolution (The `.` in `from .config import config`)

Remember in `cli.py`, `file_manager.py`, etc., we used imports like `from .config import config` or `from .guide_generator import AIService`?

**🤔 Why the Dot (`.`)?**

- The dot signifies a **relative import**. It means "from the current package, import this module."
- When Python code is part of an installed package (like `myvision_guides` is now), it needs to use relative imports to find its sibling modules (other `.py` files within the same package directory).

**How Python Finds Modules After Packaging:**

1.  **`myvision` command runs:** This executes `main()` in `src/myvision_guides/cli.py`.
2.  **`cli.py` has `from .config import config`:**
    - Python knows `cli.py` is part of the `myvision_guides` package.
    - The `.` tells it to look *inside* `myvision_guides` for a module named `config.py`.
    - It finds `src/myvision_guides/config.py`.
3.  **If you used `from config import config` (no dot):**
    - Python would look for `config.py` in standard library locations or top-level project directories, *not necessarily within your package*.
    - This would likely fail with a `ModuleNotFoundError` after installation, because the context of execution changes.

**Key Takeaway:** Relative imports (`from .module import ...`) are essential for code that will be part of an installable package.

**✅ Validation: Check Your Imports**
   - Briefly scan your `.py` files in `src/myvision_guides/`.
   - Ensure all intra-package imports (imports of other files within `myvision_guides`) start with a `.` (e.g., `from .file_manager import ...`) or `..` if going up a level (not needed in your current structure).

## 🔧 Troubleshooting Common Packaging & Installation Issues

Even with careful steps, things can go sideways. Here's how to fix common problems:

**Issue 1: `command not found: myvision`**
   ```bash
   myvision --help
   # zsh: command not found: myvision
   ```
   **Causes & Solutions:**
   1.  **Virtual Environment Not Activated:** This is the #1 culprit!
       - **Fix:** `source venv/bin/activate` (or `venv\Scripts\activate` on Windows).
       - Ensure `(venv)` is in your prompt.
   2.  **Installation Failed or Incomplete:** `pip install -e .` might have shown errors.
       - **Fix:** Scroll up in your terminal to see the output of `pip install -e .`. Look for red error messages. Address them (e.g., typos in `setup.py`, missing files).
       - Then, try uninstalling and reinstalling:
         ```bash
         pip uninstall myvision-guides
         pip install -e .
         ```
   3.  **PATH Issues (Less Common with Virtual Environments):** Your `venv/bin` (or `venv/Scripts`) might not be in your system's PATH.
       - **Fix (usually automatic with venv activation):** Deactivate and reactivate the virtual environment. If persistent, you might have a corrupted venv setup; consider recreating it (see "Drastic Measures" below).
   4.  **Typo in `entry_points` in `setup.py`:**
       - **Fix:** Double-check `"myvision=myvision_guides.cli:main"`. Is `myvision_guides` the correct package name? Is `cli` the correct module name? Is `main` the correct function name?
       - After fixing `setup.py`, reinstall: `pip install -e .`

**Issue 2: `ModuleNotFoundError: No module named 'some_library'` (e.g., `click`, `anthropic`)**
   ```bash
   myvision --help
   # Traceback (most recent call last):
   #   File "<stdin>", line 1, in <module>
   # ModuleNotFoundError: No module named 'click'
   ```
   **Causes & Solutions:**
   1.  **Dependencies Not Installed in Virtual Environment:**
       - **Fix:** Ensure venv is active. Run `pip install -r requirements.txt` again. Then `pip install -e .`.
   2.  **`requirements.txt` Out of Sync with `setup.py` (if not reading dynamically):** Your `setup.py` correctly reads `requirements.txt`, so this is less likely for you. But if `install_requires` was manually listed, it might be missing something.
   3.  **Corrupted Virtual Environment:**
       - **Fix:** See "Drastic Measures" below.

**Issue 3: `ModuleNotFoundError: No module named 'config'` (or other local modules)**
   ```bash
   myvision --help
   # Traceback (most recent call last):
   #   File "/Users/jamiesargent/myvision-guide-generator/venv/bin/myvision", line 5, in <module>
   #     from myvision_guides.cli import main
   #   File "/Users/jamiesargent/myvision-guide-generator/src/myvision_guides/cli.py", line 10, in <module>
   #     from config import config  <-- ERROR: Missing dot!
   # ModuleNotFoundError: No module named 'config'
   ```
   **Causes & Solutions:**
   1.  **Incorrect Import Style (Missing Relative Import):** You're using `from config import config` instead of `from .config import config` inside your package files.
       - **Fix:** Go through all `.py` files in `src/myvision_guides/`. Change imports of your own modules to use the `.` prefix (e.g., `from .config import config`, `from .file_manager import FileManager`).
       - After fixing, the editable install should pick up changes. If not, `pip install -e .` again.
   2.  **Missing `__init__.py` in `src/myvision_guides/`:** This tells Python it's a package.
       - **Fix:** Ensure `src/myvision_guides/__init__.py` exists. It can be empty or have the `__version__` string.
   3.  **Incorrect `package_dir` or `packages` in `setup.py`:**
       - **Fix:** Verify `package_dir={"": "src"}` and `packages=find_packages(where="src")` are correct. `find_packages` should automatically find `myvision_guides` if `src/myvision_guides/__init__.py` exists.
       - Reinstall after fixing: `pip install -e .`

**Issue 4: Changes to Code Not Reflected in `myvision` Command**
   **Causes & Solutions:**
   1.  **Not an Editable Install:** You might have run `pip install .` (without `-e`) previously.
       - **Fix:** Uninstall and reinstall in editable mode:
         ```bash
         pip uninstall myvision-guides
         pip install -e .
         ```
   2.  **Editing Files Outside the `src` Directory:** If you have copies of your code elsewhere and are editing those, the installed command (linked to `src`) won't see changes.
       - **Fix:** Ensure you are always editing the files within the `src/myvision_guides/` directory.

**Drastic Measures (If All Else Fails - The "Turn It Off and On Again" of Python):**
   If you're stuck with persistent weird errors, sometimes a clean slate helps.
   1.  **Deactivate and Remove Old Virtual Environment:**
       ```bash
       deactivate  # If active
       cd /path/to/your/myvision-guide-generator # Go to project root
       rm -rf venv # Delete the venv folder
       ```
   2.  **Clean Up Build Artifacts (Optional but good practice):**
       ```bash
       rm -rf build/ dist/ *.egg-info/  # Delete build/dist folders and .egg-info
       ```
   3.  **Recreate Virtual Environment and Reinstall Everything:**
       ```bash
       python3 -m venv venv # Or your specific python version e.g. python3.12
       source venv/bin/activate
       pip install --upgrade pip # Upgrade pip itself
       pip install -r requirements.txt
       pip install -e .
       ```
   4.  **Test again:** `myvision --help`

## 🎉 Achievement Unlocked: Professional CLI Tool!

**Congratulations! You've transformed your Python scripts into a professional, installable CLI tool!**

**What You've Mastered:**
- **`setup.py` Creation:** Defined your package's name, version, dependencies, and the crucial `myvision` command entry point.
- **Editable Installation:** Learned how `pip install -e .` links your source code for easy development.
- **System-Wide Command:** Your `myvision` command now works from any directory (in your active venv).
- **Relative Imports:** Understood why `from .module import ...` is vital for packaged code.
- **Troubleshooting:** Gained skills to diagnose and fix common packaging issues.

**The MyVision Guide Generator is now:**
- **Easy to Use:** Just type `myvision`.
- **Professional:** Behaves like any other CLI tool.
- **Ready for Development:** Editable install means code changes are live instantly.

## 🚀 Next Steps: Sharing Your Tool (Beyond This Guide)

While this guide focuses on making it work on *your* system, here's a glimpse of how you'd share it:

1.  **Create Distributable Files (Wheels and Source Archives):**
    ```bash
    # First, install the 'build' package if you haven't
    pip install build
    
    # Now, build your package
    python -m build
    ```
    This creates a `dist/` folder with files like `myvision_guides-1.0.0-py3-none-any.whl` (a wheel file) and `myvision-guides-1.0.0.tar.gz` (a source archive).

2.  **Sharing the Wheel File (`.whl`):**
    - You can send the `.whl` file (e.g., `dist/myvision_guides-1.0.0-py3-none-any.whl`) to a colleague.
    - They can install it (ideally in their own virtual environment) using:
      ```bash
      pip install /path/to/myvision_guides-1.0.0-py3-none-any.whl
      ```

3.  **Publishing to PyPI (The Python Package Index) - Advanced:**
    - This makes your tool installable globally via `pip install myvision-guides` for anyone.
    - Involves creating an account on [PyPI.org](https://pypi.org/), using a tool called `twine` to upload.
    - This is beyond our current scope but is the standard way to distribute Python packages widely.

For now, enjoy the power and professionalism of your newly packaged CLI tool! You've completed the core journey of building an AI-powered CLI agent from scratch.

---

*This concludes the MyVision Guide Generator step-by-step series. You now have a powerful, personalized tool and a solid foundation in Python development, AI integration, and CLI design!*

**Compatibility and dependencies:**
- Ensures users have compatible Python version
- Automatically installs required packages

```python
    # Command creation (THE MAGIC PART)
    entry_points={
        "console_scripts": [
            "myvision=myvision_guides.cli:main",
        ],
    },
```

**Entry points explanation:**
- Creates executable command `myvision`
- When user types `myvision`, Python runs `main()` function
- Finds `main()` in `myvision_guides.cli` module
- This is what makes `myvision --help` work

## Entry Points System

### How Entry Points Work

**The entry point definition:**
```python
"myvision=myvision_guides.cli:main"
```

**Breakdown:**
- `myvision` = Command name (what user types)
- `myvision_guides.cli` = Python module path
- `main` = Function to call

**What happens when user types `myvision guide "topic"`:**
1. Operating system finds `myvision` command
2. Python loads `myvision_guides.cli` module
3. Python calls `main()` function
4. Click framework parses `guide "topic"` arguments
5. Your code executes

### Entry Point File Creation

During installation, Python creates an executable file:

**On Mac/Linux:** `/usr/local/bin/myvision`
```bash
#!/usr/bin/python3
# EASY-INSTALL-ENTRY-SCRIPT: 'myvision-guides==1.0.0','console_scripts','myvision'
import sys
from myvision_guides.cli import main

if __name__ == '__main__':
    sys.exit(main())
```

**On Windows:** `Scripts/myvision.exe`

This is why `myvision` works from any directory - it's in your system's PATH.

## Import Resolution Issues

### The Relative vs Absolute Import Problem

**Problem scenario:**
- During development: Files in same directory, absolute imports work
- After installation: Files in package, need relative imports

### Development Phase Imports
```python
# cli.py during development
from config import config              # Works: files in same directory
from guide_generator import GuideGenerator
```

### Production Phase Imports
```python
# cli.py after installation
from .config import config             # Works: package-relative import
from .guide_generator import GuideGenerator
```

### Why This Happens

**Development structure (absolute imports work):**
```
src/myvision_guides/
├── cli.py          # from config import config
├── config.py       # ← Found in same directory
└── guide_generator.py
```

**Installed structure (relative imports needed):**
```
site-packages/
└── myvision_guides/
    ├── cli.py      # from .config import config
    ├── config.py   # ← Found in same package
    └── guide_generator.py
```

### Import Resolution Rules

**Absolute imports (`from config import config`):**
1. Search sys.path (installed packages)
2. Search current directory
3. Search PYTHONPATH

**Relative imports (`from .config import config`):**
1. Search current package only
2. The dot (`.`) means "current package"
3. More dots mean parent packages (`..` = parent)

## Installation Process Deep Dive

### Development Installation (`pip install -e .`)

**The `-e` flag means "editable" or "development mode":**

**What it does:**
- Creates links to your source code (doesn't copy files)
- Changes to source code immediately affect installed command
- Perfect for development and testing

**File structure after editable install:**
```
Your source:     /Users/you/project/src/myvision_guides/cli.py
Installed link:  /usr/local/bin/myvision → points to your source
```

**Benefits:**
- Edit code, test immediately
- No reinstallation needed
- Easy debugging

### Production Installation (`pip install .`)

**Regular installation (without -e):**
- Copies files to site-packages
- Changes to source don't affect installed version
- Must reinstall after changes

## Package Discovery and find_packages()

### How find_packages() Works

```python
packages=find_packages(where="src")
```

**Discovery process:**
1. Scan `src/` directory
2. Find directories containing `__init__.py`
3. Return list of package names

**Example discovery:**
```
src/
├── myvision_guides/
│   ├── __init__.py        # ← Makes this a package
│   ├── cli.py
│   └── config.py
└── other_stuff/           # ← No __init__.py, ignored
    └── random.py
```

**Result:** `packages=['myvision_guides']`

### The __init__.py File

**Purpose of __init__.py:**
- Marks directory as Python package
- Controls what gets imported with `from package import *`
- Can contain package initialization code

**Your __init__.py content:**
```python
"""
MyVision Guide Generator

A CLI tool for creating assistive technology learning guides.
"""

__version__ = "1.0.0"
```

## Testing Installation

### Verification Commands

**Test package installation:**
```bash
pip list | grep myvision
# Should show: myvision-guides    1.0.0
```

**Test command creation:**
```bash
which myvision
# Should show: /usr/local/bin/myvision (or similar)
```

**Test command functionality:**
```bash
myvision --version
myvision --help
myvision guide --help
```

**Test imports work:**
```bash
python3 -c "from myvision_guides.cli import main; print('Imports work!')"
```

### Common Installation Issues

#### Issue 1: Command Not Found
```bash
myvision --help
# bash: myvision: command not found
```

**Causes and solutions:**
- **Virtual environment not activated:** `source venv/bin/activate`
- **Installation failed:** Check `pip install -e .` output for errors
- **PATH issues:** `echo $PATH` should include Python scripts directory

#### Issue 2: Import Errors
```bash
myvision --help
# ModuleNotFoundError: No module named 'config'
```

**Causes and solutions:**
- **Wrong import style:** Use relative imports (`from .config import config`)
- **Missing __init__.py:** Ensure all package directories have this file
- **Package structure:** Verify `find_packages()` finds your package

#### Issue 3: Dependency Issues
```bash
myvision --help
# ModuleNotFoundError: No module named 'anthropic'
```

**Causes and solutions:**
- **Virtual environment:** Ensure you're in the right environment
- **Dependencies not installed:** `pip install -r requirements.txt`
- **setup.py missing requirements:** Check `install_requires` list

## Development Workflow

### Recommended Development Process

**1. Initial setup:**
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

**2. Development cycle:**
```bash
# Edit code
nano src/myvision_guides/cli.py

# Test immediately (no reinstall needed)
myvision guide "test topic"

# Debug issues
myvision --help
```

**3. Testing changes:**
```bash
# Test specific functionality
myvision guide "VoiceOver basics" --format markdown

# Test error handling
myvision guide  # Missing argument

# Test with invalid options
myvision guide "topic" --format invalid
```

### Version Management

**Updating version:**
```python
# In setup.py
version="1.0.1",  # Increment version
```

**Reinstall with new version:**
```bash
pip install -e .  # Updates version info
```

**Check installed version:**
```bash
myvision --version
pip show myvision-guides
```

## Advanced Packaging Concepts

### Classifiers

```python
classifiers=[
    "Development Status :: 4 - Beta",
    "Intended Audience :: Healthcare Industry",
    "Topic :: Education",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]
```

**Purpose:**
- Package categorization for PyPI
- Helps users find your package
- Indicates maturity and target audience

### Package Data Inclusion

```python
# Include non-Python files
package_data={
    "myvision_guides": ["templates/*.docx", "templates/*.png"],
},
include_package_data=True,
```

**For including:**
- Template files
- Configuration files
- Documentation
- Static assets

### Console Scripts vs GUI Scripts

```python
entry_points={
    "console_scripts": [
        "myvision=myvision_guides.cli:main",           # Terminal tool
    ],
    "gui_scripts": [
        "myvision-gui=myvision_guides.gui:main",       # Desktop app
    ],
}
```

**Difference:**
- **console_scripts:** Terminal applications
- **gui_scripts:** Desktop applications (no terminal window)

## Distribution and Sharing

### Creating Distributable Package

**Build wheel (preferred):**
```bash
pip install build
python -m build
```

**Creates:**
- `dist/myvision_guides-1.0.0-py3-none-any.whl`
- `dist/myvision-guides-1.0.0.tar.gz`

### Installing from Wheel

**Share wheel file with others:**
```bash
pip install myvision_guides-1.0.0-py3-none-any.whl
```

### Publishing to PyPI (Future)

**Test on PyPI test server:**
```bash
pip install twine
twine upload --repository testpypi dist/*
```

**Install from test PyPI:**
```bash
pip install --index-url https://test.pypi.org/simple/ myvision-guides
```

## Troubleshooting Guide

### Debug Installation Problems

**Check virtual environment:**
```bash
which python    # Should show venv path
which pip       # Should show venv path
pip list        # Check installed packages
```

**Verify package structure:**
```bash
find src/ -name "*.py" -exec echo "File: {}" \;
find src/ -name "__init__.py" -exec echo "Package marker: {}" \;
```

**Test imports step by step:**
```bash
python3 -c "import myvision_guides; print('Package loads')"
python3 -c "from myvision_guides import cli; print('CLI module loads')"
python3 -c "from myvision_guides.cli import main; print('Main function found')"
```

### Common Fixes

**Reinstall package:**
```bash
pip uninstall myvision-guides
pip install -e .
```

**Clean installation:**
```bash
pip uninstall myvision-guides
rm -rf build/ dist/ *.egg-info/
pip install -e .
```

**Reset virtual environment:**
```bash
deactivate
rm -rf venv/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Best Practices Summary

### Project Structure
1. **Consistent naming:** Package name matches directory name
2. **Clear separation:** Source code in `src/`, tests in `tests/`
3. **Proper __init__.py:** Every package directory needs this
4. **Relative imports:** Use `.` for package-internal imports

### setup.py Configuration
1. **Dynamic requirements:** Read from `requirements.txt`
2. **Semantic versioning:** major.minor.patch format
3. **Descriptive metadata:** Good description and classifiers
4. **Python version:** Specify minimum required version

### Development Workflow
1. **Editable installs:** Use `-e` flag during development
2. **Virtual environments:** Isolate project dependencies
3. **Testing commands:** Verify installation and functionality
4. **Version control:** Track setup.py and requirements.txt

### Distribution Readiness
1. **Complete documentation:** README, docstrings, help text
2. **Dependency management:** Pinned versions, compatibility testing
3. **Error handling:** Graceful failures, helpful error messages
4. **Platform testing:** Test on different operating systems

---

*This guide covers the complete process of making your CLI tool installable and professional. The concepts learned here apply to any Python package you might create in the future.*