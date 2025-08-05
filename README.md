# GPT CLI Tool

A command-line tool that uses OpenAI's GPT to help you generate Linux commands from natural language descriptions.

## Description

This tool allows you to describe what you want to do in plain English, and it will suggest the appropriate Linux command. Perfect for when you know what you want to accomplish but can't remember the exact command syntax.

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. **Get an OpenAI API key** from [OpenAI Platform](https://platform.openai.com/account/api-keys)

2. **Set up your API key**:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```
   
   Add this to your shell configuration to make it permanent:
   ```bash
   echo 'export OPENAI_API_KEY=your_api_key_here' >> ~/.zshrc
   ```

3. **Install required dependencies**:
   ```bash
   pip install openai
   ```

4. **Create the bin directory** (if it doesn't exist):
   ```bash
   mkdir -p ~/bin
   ```

5. **Add ~/bin to your PATH** (if not already done):
   ```bash
   echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
   ```

6. **Make the script executable**:
   ```bash
   chmod +x ask.py
   ```

7. **Create a symbolic link** for easy access:
   ```bash
   ln -s ~/projects/gpt-cli-tool/ask.py ~/bin/ask
   ```

8. **Reload your shell configuration**:
   ```bash
   source ~/.zshrc
   ```

## Usage

After installation, you can use the `ask` command from anywhere:

```bash
ask "list all hidden directories"
ask "find files larger than 100MB"
ask "compress a directory into a tar.gz file"
ask "show disk usage sorted by size"
```

The tool will output the appropriate Linux command based on your description.

## Examples

```bash
$ ask "list all files in current directory"
ls -la

$ ask "find all Python files"
find . -name "*.py"

$ ask "show running processes"
ps aux
```

## Notes

- The tool only outputs the command itself, no explanations or markdown formatting
- Always review the generated commands before executing them
- The tool uses GPT-4o-mini model for cost efficiency while maintaining good performance
