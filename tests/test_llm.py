import os
import pytest

from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

def test_gpt():
    """Test ChatOpenAI model invocation."""
    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.5,
        max_completion_tokens=100,
        top_p=0.9,
        timeout=5,
        max_retries=3
    )

    response = model.invoke("Hello!")

    assert response is not None
    assert hasattr(response, 'content')
    assert len(response.content) > 0
    print(f"Response: {response.content}")


if __name__ == "__main__":

    pytest.main(["-v",__file__])