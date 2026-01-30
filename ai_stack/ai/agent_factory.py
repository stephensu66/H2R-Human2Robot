
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.agents import create_agent
from ai.prompt import system_propmt

def build_agent():
  llmModal = ChatOpenAI(
    model="qwen-plus",
    temperature=0,
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
  )

  return create_agent(
        model=llmModal,
        tools=[],
        system_prompt= system_propmt
  )