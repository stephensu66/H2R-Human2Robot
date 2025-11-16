
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.agents import create_agent
import os

load_dotenv()

llmModal = ChatOpenAI(
    model="deepseek-chat",
    temperature=0,
    api_key=os.getenv.DEEPSEEK_API_KEY,
    base_url=os.getenv.DEEPSEEK_API_BASE_URL
)

agent = create_agent(
    model="deepseek-chat",
    tools=[],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
