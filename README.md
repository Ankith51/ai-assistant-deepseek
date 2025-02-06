# ai-assistant-deepseek
Build and interact with a powerful AI assistant using the DeepSeek LLM API! This project provides a command-line interface (CLI) for seamless interaction with DeepSeek's advanced language model.
# AI Assistant with DeepSeek LLM API

This is an AI assistant that interacts with users using the DeepSeek LLM API.

## Features
- Interactive command-line interface.
- Integration with DeepSeek's powerful language model.
- Easy-to-extend architecture.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ankith51/ai-assistant-deepseek.git
   cd ai-assistant-deepseek

   pip install -r requirements.txt

   python src/cli.py

   python -m pytest tests/


   setup.py (Optional)
   If you want to package your project:

   from setuptools import setup, find_packages

setup(
    name="ai-assistant-deepseek",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "ai-assistant=cli:main",
        ],
    },
)
