import os
from dotenv import load_dotenv

load_dotenv()

import textwrap

from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

from my_agent.utils import internet_search


# Define tools
@tool
def search_internet(query: str) -> str:
    """Search the internet for information."""
    return internet_search(query)

# Define system prompt
SYSTEM_PROMPT = textwrap.dedent("""
    You are a helpful assistant.

    You have the following tools available:
    - search_internet: Search the internet for information

    When answering questions, use the search_internet tool to find relevant information.
    """).strip()


# Configure model
model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.5,
        max_completion_tokens=1000,
        top_p=0.9,
        timeout=5,
        max_retries=3
    )

def create_my_agent(use_checkpointer: bool = False):
    """Create and return the agent with tools and model."""
    checkpointer = InMemorySaver() if use_checkpointer else None
    return create_agent(
        model=model,
        tools=[search_internet],
        system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer
    )

# Create the agent
agent = create_my_agent(use_checkpointer=False)