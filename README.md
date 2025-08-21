# 🖥️ LLM-Powered Terminal Assistant (Text → CMD)

## 🌟 Overview

The **LLM-Powered Terminal Assistant** is a **CLI tool** that allows you to interact with your shell using **plain English instructions**.  
It acts as a **smart AI-powered developer assistant** that converts natural language into **safe and executable terminal commands**.

Think of it as:  
👉 *“Hey terminal, show me all `.txt` files”* → `ls *.txt`  



## 🎯 Features

- 🤖 **AI-powered command generation** – translate natural language into shell commands.  
- 📝 **Preview before execution** – review suggested commands before running.  
- ⚡ **Auto-execution option** – run the generated command instantly if approved.  
- 🔒 **Safety-first approach** – avoids blindly running dangerous commands.  
- 🌐 **Powered by OpenAI GPT models** – flexible, accurate, and constantly improving.  
- 🪟 **Cross-platform roadmap** – upcoming support for **Windows/PowerShell**.  



## 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/text-to-cmd-ai.git
cd text-to-cmd-ai
pip install -r requirements.txt
```

Set your **OpenAI API key** (required):

```bash
export OPENAI_API_KEY="your_api_key_here"
```

*(Windows users: use `setx OPENAI_API_KEY "your_api_key_here"`)  



## ▶️ Usage

Run the tool by passing your natural language query:

```bash
python ask.py "list all .txt files"
```

Output:

```
🤖 Suggested command: ls *.txt
⚡ Do you want to run this command? (y/n): y
```

Another example:

```bash
python ask.py "check disk usage"
```

```
🤖 Suggested command: du -h
⚡ Do you want to run this command? (y/n): n
```



## 📂 Project Structure

```
text-to-cmd-ai/
│── ask.py           # Main CLI entry point
│── requirements.txt # Python dependencies
│── README.md        # Project documentation
```



## 🚀 Roadmap

✅ Current features:  
- Linux/macOS terminal support  
- AI-powered text-to-command translation  

🛠 Planned improvements:  
- [ ] Windows/PowerShell support 🪟  
- [ ] Fuzzy safety checks for risky commands (`rm -rf`, `sudo`, etc.)  
- [ ] Multiple LLM provider support (Anthropic, Cohere, etc.)  
- [ ] Interactive learning mode (explain commands before execution)  
- [ ] Configurable execution policies  

