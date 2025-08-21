# 🖥️ LLM-Powered Terminal Assistant (Text to CMD)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python)](https://www.python.org/)  
[![OpenAI](https://img.shields.io/badge/OpenAI-API-orange?logo=openai)](https://platform.openai.com/)  

---

## 🌟 Overview

This project is a **CLI tool powered by LLMs** 🤖 that converts **plain English instructions into terminal commands**.  
Think of it as a smart developer assistant for your shell 🐚.

---

## 🎯 Features

- 📝 Convert **natural language → terminal commands**
- ⚡ Option to auto-execute suggested commands
- 🔒 Safe: you choose whether to run the command or not
- 🌐 Powered by **OpenAI GPT models**

---

## 🛠️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/text-to-cmd-ai.git
cd text-to-cmd-ai
pip install -r requirements.txt
```

Set your API key:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

---

## ▶️ Usage

Example:

```bash
$ python ask.py "list all .txt files"
🤖 Suggested command: ls *.txt
⚡ Do you want to run this command? (y/n): y
```

---

## 📂 Project Structure

```
text-to-cmd-ai/
│── ask.py           # Main CLI tool
│── requirements.txt # Dependencies
│── README.md        # Documentation
```

---

## 🚀 Roadmap

- [ ] Add Windows/PowerShell support 🪟  
- [ ] Add fuzzy safety checks for dangerous commands  
- [ ] Add support for multiple LLM providers  

---

## ⭐ Support

If this project helps you, give it a ⭐ on GitHub 🙌  

---

## 📜 License

MIT License  

⚡️ *Talk to your terminal like never before!* 🖥️🤖
