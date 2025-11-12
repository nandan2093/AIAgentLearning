"""
ADK Agent Configuration
Place this file in a directory and run: adk web <directory_name>
"""
from dotenv import load_dotenv
import os
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from google.genai import types

# Load environment variables
load_dotenv()

# Configure retry options
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504]
)

# Define the agent - this will be automatically discovered by ADK
helpful_assistant = Agent(
    name="helpful-assistant",
    model=Gemini(
        model="gemini-1.5-flash",
        retry_options=retry_config,
        api_key=os.getenv("GOOGLE_API_KEY")
    ),
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)

print("✅ Agent 'helpful_assistant' configured!")