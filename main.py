import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, ItemHelpers

load_dotenv()

@function_tool
def get_weather(city: str):
    """Get weather by city"""
    return "30 degrees"


if __name__ == "__main__":
    asyncio.run(get_weather("Madrid"))
