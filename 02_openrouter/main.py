import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI

load_dotenv()

set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

agent = Agent(
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-chat-v3-0324:free", openai_client=client),
    name="Asma",
    instructions="you are a helpful assistant",
)

async def main():
    result = await Runner.run(agent, "what is your name?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())