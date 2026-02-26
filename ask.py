#!/usr/bin/env python3

import sys
from openai import OpenAI

client = OpenAI()


def ask_gpt(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful Linux command assistant. Only output the command itself. Return the command itself, no markdown, no explanation, no nothing.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    return (
        response.choices[0]
        .message.content.strip()
        .replace("```", "")
        .replace("bash", "")
        .strip()
    )

def main():
    if len(sys.argv) < 2:
        print("Usage: gptcmd.py 'Describe what you want to do'")
        sys.exit(1)
    user_prompt = " ".join(sys.argv[1:])
    command = ask_gpt(user_prompt)
    print(command)

if __name__ == "__main__":
    main()
