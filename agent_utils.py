import os

from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool





#define agent and export
agent = Agent(
    'groq:llama-3.1-8b-instant',
    tools=[tavily_search_tool(TAVILY_API_KEY)],
    system_prompt = 'Search Tavily for the given query and return the results.',
)


def reasearch_result(query: str)->str:
    result =agent.run_sync(query)
    return = result.output