# langchain_agent.py

from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_community.llms import Ollama
from tools import podcast_tools

# Connect to your local Ollama model (Mistral 7B)
llm = Ollama(model="mistral", base_url="http://localhost:11434")

# Create the agent with your tools
agent = initialize_agent(
    tools=podcast_tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
