"""
Setup configuration for MyVision Guide Generator

This file tells Python how to install your CLI tool.
"""

# SECTION Imports
from setuptools import setup, find_packages

# SECTION Requirements Loading
# Read requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# SECTION Package Setup
setup(
    # SECTION Basic Package Information
    # Basic package information
    name="myvision-guides",
    version="1.0.0",
    author="MyVision Oxfordshire",
    description="CLI tool for generating assistive technology learning guides",
    
    # SECTION Source Code Location
    # Where to find the source code
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    
    # SECTION Python Requirements
    # Python version requirement
    python_requires=">=3.8",
    
    # SECTION Dependencies
    # Dependencies (reads from requirements.txt)
    install_requires=requirements,
    
    # SECTION CLI Entry Point
    # This is the magic part - creates the 'myvision' command
    entry_points={
        "console_scripts": [
            "myvision=myvision_guides.cli:main",
        ],
    },
    
    # SECTION Project Metadata
    # Project metadata
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)