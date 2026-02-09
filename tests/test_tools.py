import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest

from dotenv import load_dotenv

load_dotenv()

from my_agent.utils import internet_search


def test_internet_search():
    """Test internet search with real API."""
    result = internet_search("Python programming", max_results=2)
    
    assert result is not None
    assert "results" in result
    assert len(result["results"]) <= 2
    assert result["results"][0]["title"] is not None
    assert result["results"][0]["url"] is not None


if __name__ == "__main__":
    pytest.main(["-v", __file__])