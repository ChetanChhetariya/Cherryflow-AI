"""
Cherryflow-AI — Base Agent
All agents inherit from this class.
"""

import os
import anthropic
from datetime import datetime


class BaseAgent:
    def __init__(self, agent_name: str, system_prompt: str, model: str = "claude-sonnet-4-20250514"):
        self.agent_name = agent_name
        self.model = model
        self.system_prompt = system_prompt
        self.client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        self.conversation_history = []

    def chat(self, user_message: str) -> str:
        """Send a message to Claude and get a response."""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=self.system_prompt,
            messages=self.conversation_history
        )

        assistant_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message

    def reset_conversation(self):
        """Clear conversation history."""
        self.conversation_history = []

    def log(self, message: str):
        """Simple logger with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{self.agent_name}] {message}")
