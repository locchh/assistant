# assistant

## Structure

```
my-app/
├── my_agent                # all project code lies within here
│   ├── utils               # utilities for your graph
│   │   ├── __init__.py
│   │   └── tools.py        # tools for your graph
│   ├── __init__.py
│   └── agent.py            # code for constructing your graph
├── .env                    # environment variables
├── requirements.txt        # package dependencies
└── langgraph.json          # configuration file for LangGraph
```

## Setup & Run

```bash
# Install dependencies
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Run the agent for development
langgraph dev --no-browser
# Access the agent at http://localhost:2024

# Run the agent as a persistent service (runs forever, auto-restarts)
langgraph up -d docker-compose.yml --wait

# Run on port 9000 instead of default 8123
#langgraph up -d docker-compose.yml --wait --port 9000

# Stop and remove containers
docker stop assistant-langgraph-api-1 assistant-langgraph-redis-1 assistant-langgraph-postgres-1
docker rm assistant-langgraph-api-1 assistant-langgraph-redis-1 assistant-langgraph-postgres-1

# ONLY if you want to DELETE all data (threads, checkpoints, etc.)
# docker volume rm assistant_langgraph-data

# Start the agent again (data is preserved)
docker start assistant-langgraph-postgres-1 assistant-langgraph-redis-1 assistant-langgraph-api-1

# Rebuild and restart (after code changes)
langgraph up -d docker-compose.yml --wait --recreate

# Restart all containers (keeps data)
docker restart assistant-langgraph-api-1 assistant-langgraph-redis-1 assistant-langgraph-postgres-1

# View container logs
docker logs assistant-langgraph-api-1 -f

# After making changes to the agent code, rebuild and restart:
langgraph up -d docker-compose.yml --wait --recreate

# Setup UI
git clone https://github.com/langchain-ai/agent-chat-ui.git
cd agent-chat-ui
npm install
npm run dev
# Access the UI at http://localhost:3000
# Connect to the agent at http://localhost:2024 or http://localhost:8123 with agent id "my_agent"
```

## Testing with curl

```bash
# Health check
curl -s http://localhost:8123/ok

# List registered assistants
curl -s -X POST http://localhost:8123/assistants/search -H "Content-Type: application/json" -d '{}'

# Send a message (streaming)
curl -s -X POST http://localhost:8123/runs/stream \
  -H "Content-Type: application/json" \
  -d '{
    "assistant_id": "my_agent",
    "input": {"messages": [{"role": "human", "content": "Hello!"}]},
    "stream_mode": ["messages-tuple"]
  }'

# Create a thread (for persistent conversations)
curl -s -X POST http://localhost:8123/threads \
  -H "Content-Type: application/json" \
  -d '{}'

# Send a message to a thread (replace THREAD_ID)
curl -s -X POST http://localhost:8123/runs/stream \
  -H "Content-Type: application/json" \
  -d '{
    "assistant_id": "my_agent",
    "thread_id": "THREAD_ID",
    "input": {"messages": [{"role": "human", "content": "Search the internet for LangGraph"}]},
    "stream_mode": ["messages-tuple"]
  }'

# List threads
curl -s -X POST http://localhost:8123/threads/search \
  -H "Content-Type: application/json" \
  -d '{}'
```

## Related to

[LangChain Quickstart](https://docs.langchain.com/oss/python/langchain/quickstart)

[LangGraph Quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart)

[DeepAgents Quickstart](https://docs.langchain.com/oss/python/deepagents/quickstart)

[Frameworks, runtimes, and harnesses](https://docs.langchain.com/oss/python/concepts/products)

[Build a SQL agent](https://docs.langchain.com/oss/python/langchain/sql-agent)

[Local development & testing](https://docs.langchain.com/langsmith/local-dev-testing)

[Application structure](https://docs.langchain.com/langsmith/application-structure)

[Agent server](https://docs.langchain.com/langsmith/agent-server)

[Server API reference](https://docs.langchain.com/langsmith/server-api-ref)

[Langgraph CLI](https://docs.langchain.com/langsmith/cli)

[Agent chat UI](https://github.com/langchain-ai/agent-chat-ui)