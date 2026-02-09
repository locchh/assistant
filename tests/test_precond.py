import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest

from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def env_vars():
    """Fixture that reads .env.example and returns list of environment variable names."""
    env_vars = []
    env_path = ".env.example"
    
    with open(env_path) as f:
        lines = f.readlines()
    
    for line in lines:
        # Extract env var name (everything before the '=')
        line = line.strip()
        if line and '=' in line:
            var_name = line.split('=')[0]
            if var_name[0]=='"' and var_name[-1]=='"':
                var_name = var_name[1:-1]
            env_vars.append(var_name)
    
    return env_vars


def test_load_environment_variables(env_vars):
    """Test loading environment variables from .env.example and assert they are not None."""
    # Assert each environment variable is not None
    for var in env_vars:
        assert len(os.getenv(var)) > 0, f"Environment variable {var} should not be empty"
        assert os.getenv(var) is not None, f"Environment variable {var} should not be None"


if __name__ == "__main__":

    pytest.main(["-v",__file__])