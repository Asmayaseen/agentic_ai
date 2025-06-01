import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, RunConfig, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, set_default_openai_client, set_default_openai_api
from openai import AsyncOpenAI

load_dotenv()

set_tracing_disabled(disabled=True)
set_default_openai_api("chat_completions")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

set_default_openai_client(client)

agent = Agent(
    name="Asma",
    instructions="you are a helpful assistant",
    model=OpenAIChatCompletionsModel(
        model="deepseek/deepseek-chat-v3-0324:free",
        openai_client=client
    ),
)

async def main():
    config = RunConfig(
        model=OpenAIChatCompletionsModel(
            model="deepseek/deepseek-chat-v3-0324:free",
            openai_client=client
        ),
        tracing_disabled=True,
    )

    result = await Runner.run(agent, "what is your name?", run_config=config)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())