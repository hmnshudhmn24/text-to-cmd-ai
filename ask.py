#!/usr/bin/env python3
import sys
import openai
import subprocess

# Replace with your own API key or set via environment variable
openai.api_key = "YOUR_OPENAI_API_KEY"

def translate_to_cmd(instruction):
    prompt = f"Translate the following natural language instruction into a Linux terminal command: {instruction}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=0
    )
    return response.choices[0].text.strip()

def main():
    if len(sys.argv) < 2:
        print("Usage: ask "your instruction here"")
        sys.exit(1)

    instruction = " ".join(sys.argv[1:])
    command = translate_to_cmd(instruction)
    print(f"🤖 Suggested command: {command}")

    choice = input("⚡ Do you want to run this command? (y/n): ")
    if choice.lower() == 'y':
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()
