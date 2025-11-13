# agent_utils.py
import os
from pathlib import Path
from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool

# Load environment variables from a .env file if present
# Requires python-dotenv to be installed: pip install python-dotenv
try:
    from dotenv import load_dotenv

    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path, override=False)
except Exception:
    pass

# Read API keys from environment (will include values from .env if loaded)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Define and export the agent
agent = Agent(
    "groq:llama-3.1-8b-instant",
    tools=[tavily_search_tool(TAVILY_API_KEY)],
    system_prompt="Search Tavily for the given query and return the results.",
)

def get_search_results(query: str) -> str:
    result = agent.run_sync(query)
    return result.output