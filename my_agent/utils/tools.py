import os
from dotenv import load_dotenv
from typing import Literal
from tavily import TavilyClient

load_dotenv()


def get_tavily_client():
    """Get Tavily client with error handling."""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY environment variable is not set")
    return TavilyClient(api_key=api_key)


def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search using Tavily API.
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return (1-10)
        topic: Search topic category
        include_raw_content: Whether to include raw page content
        
    Returns:
        Search results from Tavily API
        
    Raises:
        ValueError: If query is empty or API key is missing
    """
    if not query or not query.strip():
        raise ValueError("Query cannot be empty")
    
    if max_results < 1 or max_results > 10:
        raise ValueError("max_results must be between 1 and 10")
    
    client = get_tavily_client()
    
    try:
        return client.search(
            query,
            max_results=max_results,
            include_raw_content=include_raw_content,
            topic=topic,
        )
    except Exception as e:
        raise RuntimeError(f"Search failed: {str(e)}")