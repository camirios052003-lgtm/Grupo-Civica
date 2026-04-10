"""
Function tools for the multi-agent PoC.

These Python functions are automatically wrapped as FunctionTool objects
by ADK when assigned to an agent's `tools` list.

State Integration:
  Both tools now accept an optional `tool_context` parameter. When present,
  ADK automatically injects the ToolContext, allowing tools to read from
  and write to the shared session state. This enables downstream agents
  (e.g., SQL Expert) to access the results produced by these tools.
"""

import random
import json
from datetime import datetime
from google.adk.tools import ToolContext


# ── Weather Tool ─────────────────────────────────────────────────────────

def get_weather(city: str, tool_context: ToolContext) -> dict:
    """
    Retrieves mock weather data for a given city.

    Saves the weather result to session state under:
      - 'last_weather_city' → city name
      - 'last_weather_data' → full weather report (JSON string)

    Args:
        city: The name of the city to get weather for.
        tool_context: The ADK ToolContext (auto-injected) for state access.

    Returns:
        A dictionary with the weather report or an error message.
    """
    # Simulated weather data for supported cities
    weather_db = {
        "bogota": {
            "temp_celsius": 18,
            "temp_fahrenheit": 64,
            "condition": "Partly cloudy with light rain",
            "humidity": 72,
            "wind_kmh": 15,
        },
        "new york": {
            "temp_celsius": 22,
            "temp_fahrenheit": 72,
            "condition": "Sunny with clear skies",
            "humidity": 45,
            "wind_kmh": 10,
        },
        "london": {
            "temp_celsius": 15,
            "temp_fahrenheit": 59,
            "condition": "Overcast with drizzle",
            "humidity": 80,
            "wind_kmh": 20,
        },
        "tokyo": {
            "temp_celsius": 28,
            "temp_fahrenheit": 82,
            "condition": "Warm and humid with afternoon thunderstorms",
            "humidity": 65,
            "wind_kmh": 8,
        },
        "medellin": {
            "temp_celsius": 24,
            "temp_fahrenheit": 75,
            "condition": "Pleasant with occasional clouds",
            "humidity": 60,
            "wind_kmh": 12,
        },
    }

    city_lower = city.strip().lower()

    if city_lower not in weather_db:
        return {
            "status": "error",
            "message": (
                f"Weather data for '{city}' is not available. "
                f"Supported cities: {', '.join(c.title() for c in weather_db)}"
            ),
        }

    data = weather_db[city_lower]
    report = (
        f"Weather in {city.title()}: {data['condition']}. "
        f"Temperature: {data['temp_celsius']}°C ({data['temp_fahrenheit']}°F). "
        f"Humidity: {data['humidity']}%. "
        f"Wind: {data['wind_kmh']} km/h."
    )

    result = {"status": "success", "report": report}

    # ── Save to session state ────────────────────────────────────────
    tool_context.state["last_weather_city"] = city.title()
    tool_context.state["last_weather_data"] = json.dumps(data)
    tool_context.state["last_weather_report"] = report

    # Track weather query history count
    count = tool_context.state.get("weather_query_count", 0)
    tool_context.state["weather_query_count"] = count + 1

    return result


# ── COP → USD Conversion Tool ───────────────────────────────────────────

def convert_cop_to_usd(amount_cop: float, tool_context: ToolContext) -> dict:
    """
    Converts Colombian Pesos (COP) to US Dollars (USD).

    Uses a simulated, slightly fluctuating exchange rate around 4,150 COP/USD.
    Saves the conversion result to session state under:
      - 'last_conversion_cop' → original amount in COP
      - 'last_conversion_usd' → converted amount in USD
      - 'last_conversion_rate' → rate used

    Args:
        amount_cop: The amount in Colombian Pesos to convert.
        tool_context: The ADK ToolContext (auto-injected) for state access.

    Returns:
        A dictionary with the conversion result.
    """
    if amount_cop <= 0:
        return {
            "status": "error",
            "message": "The amount must be a positive number.",
        }

    # Simulated exchange rate with small random fluctuation
    base_rate = 4150
    fluctuation = random.uniform(-50, 50)
    rate = base_rate + fluctuation
    usd_amount = amount_cop / rate

    result = {
        "status": "success",
        "amount_cop": f"{amount_cop:,.2f} COP",
        "amount_usd": f"${usd_amount:,.2f} USD",
        "exchange_rate": f"1 USD = {rate:,.2f} COP",
        "note": "Simulated rate for demonstration purposes.",
    }

    # ── Save to session state ────────────────────────────────────────
    tool_context.state["last_conversion_cop"] = amount_cop
    tool_context.state["last_conversion_usd"] = round(usd_amount, 2)
    tool_context.state["last_conversion_rate"] = round(rate, 2)

    # Track conversion count
    count = tool_context.state.get("conversion_count", 0)
    tool_context.state["conversion_count"] = count + 1

    return result


# ── Multimedia & Fun Tools ──────────────────────────────────────────────

def search_gif(query: str) -> dict:
    """
    Searches for a GIF based on a keyword.
    In this PoC, it returns a curated Giphy search link or a placeholder.
    
    Args:
        query: The topic or emotion for the GIF (e.g., 'happy dancing', 'coding').
    """
    clean_query = query.strip().replace(" ", "-")
    gif_url = f"https://giphy.com/search/{clean_query}"
    
    # Mocking a direct GIF result for the UI
    mock_gifs = {
        "coding": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJycXJycXJycXJycXJycXJycXJycXJycXJycXJycXJycXJycSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26tn33aiTi1jkl6H6/giphy.gif",
        "happy": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJycXJycXJycXJycXJycXJycXJycXJycXJycXJycXJycXJycXJycSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0HlU7f6-G3Cyc_kI/giphy.gif",
        "funny": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJycXJycXJycXJycXJycXJycXJycXJycXJycXJycXJycXJycXJycSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKVUn7iM8FMEU24/giphy.gif"
    }
    
    direct_url = mock_gifs.get(clean_query.lower(), "https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif")

    return {
        "status": "success",
        "query": query,
        "gif_search_url": gif_url,
        "direct_gif_url": direct_url,
        "message": f"Found a GIF for '{query}'! You can view it here: {gif_url}"
    }

def generate_meme(template: str, top_text: str, bottom_text: str) -> dict:
    """
    Generates a meme image using the memegen.link service.
    
    Args:
        template: The meme template ID (e.g., 'doge', 'biw', 'ds', 'pika').
        top_text: Text for the top of the meme.
        bottom_text: Text for the bottom of the meme.
    """
    # Sanitize text for URL (memegen.link uses _ for spaces and ~q for ?)
    def sanitize(text):
        return text.replace(" ", "_").replace("?", "~q").replace("/", "~s")
    
    t = sanitize(template or "doge")
    top = sanitize(top_text or " ")
    bot = sanitize(bottom_text or " ")
    
    meme_url = f"https://api.memegen.link/images/{t}/{top}/{bot}.png"
    
    return {
        "status": "success",
        "meme_url": meme_url,
        "template_used": template,
        "message": f"Generated your meme! Check it out: {meme_url}"
    }
