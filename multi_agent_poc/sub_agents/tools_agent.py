"""
Tools Agent — specializes in calling external tools.

This agent has access to the weather and COP-USD conversion tools.
The root orchestrator delegates tool-related questions here.
"""

from google.adk.agents import Agent
from multi_agent_poc.tools import get_weather, convert_cop_to_usd
from multi_agent_poc.model import agnostic_model


tools_agent = Agent(
    name="tools_agent",
    model=agnostic_model,
    description=(
        "Specialist agent that can retrieve weather information for cities "
        "and convert Colombian Pesos (COP) to US Dollars (USD). "
        "Delegate to this agent when the user asks about weather forecasts, "
        "climate conditions, or currency conversion between COP and USD."
    ),
    instruction=(
        "You are a helpful tools specialist. You have access to two tools:\n\n"
        "1. **get_weather**: Use this when the user asks about weather in a city. "
        "Supported cities are: Bogota, New York, London, Tokyo, and Medellin.\n\n"
        "2. **convert_cop_to_usd**: Use this when the user wants to convert "
        "Colombian Pesos (COP) to US Dollars (USD). Ask for the amount in COP "
        "if not provided.\n\n"
        "Always present results in a friendly and well-formatted way. "
        "If a city is not supported, let the user know which cities are available.\n\n"
        "## IMPORTANT: Scope Boundaries\n"
        "- You can ONLY handle weather lookups and COP-to-USD conversion.\n"
        "- If the user's request includes tasks outside your scope (e.g., SQL "
        "queries, customer service, general questions), complete ONLY your part "
        "(weather or currency) and then IMMEDIATELY transfer back to the "
        "orchestrator so it can delegate the remaining tasks to the "
        "appropriate specialist.\n"
        "- NEVER try to answer questions about SQL, databases, orders, "
        "returns, or any topic outside weather and currency conversion."
    ),
    tools=[get_weather, convert_cop_to_usd],
    output_key="tools_agent_output",
)
