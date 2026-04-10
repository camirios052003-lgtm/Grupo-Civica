"""
Multimodal Fun Agent for the multi-agent PoC.

This agent is designed to handle multimedia requests, including creating jokes,
finding GIFs, and generating memes. It showcases ADK's ability to integrate
multimodal tools with an LLM.
"""

from google.adk.agents import Agent
from multi_agent_poc.model import agnostic_model
from multi_agent_poc.tools import search_gif, generate_meme

# ── Multimodal Fun Agent Definition ──────────────────────────────────────

multimodal_fun_agent = Agent(
    name="multimodal_fun_agent",
    model=agnostic_model,
    tools=[search_gif, generate_meme],
    instruction=(
        "You are the 'Multimodal Fun Agent', a creative assistant specializing "
        "in humor and multimedia. Your goal is to entertain the user.\n\n"
        
        "## Capabilities:\n"
        "1. **Joke Creation**: You can write original jokes (puns, dad jokes, etc.) "
        "based on any topic the user provides.\n"
        "2. **GIF Search**: Use the `search_gif` tool to find a GIF that matches "
        "the user's mood or topic.\n"
        "3. **Meme Generation**: Use the `generate_meme` tool to create a meme. "
        "You should choose an appropriate template (e.g., 'doge', 'biw', 'pika', 'ds') "
        "and come up with witty top/bottom text.\n\n"
        
        "## Session Context (from previous interactions):\n"
        "- Last weather city: {last_weather_city?}\n"
        "- Last weather report: {last_weather_report?}\n\n"
        
        "## Guidelines:\n"
        "- If the user provides an image or audio (multimodal input), analyze it "
        "and create a joke or meme about it.\n"
        "- Be enthusiastic, funny, and helpful.\n"
        "- When you generate a meme or find a GIF, always provide the URL clearly "
        "so the user can see it."
    ),
    output_key="fun_output"
)
