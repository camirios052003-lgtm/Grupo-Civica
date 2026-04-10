"""
Car Repair Expert Agent — specializes in automotive diagnostics and repair advice.

This agent uses the ADK Skills feature to load a comprehensive car repair
knowledge base, including diagnostic tables and maintenance schedules.
It does NOT perform actual repairs; it provides expert guidance.
"""

import pathlib
import yaml

from google.adk.agents import Agent
from google.adk.skills import models
from google.adk.tools.skill_toolset import SkillToolset
from multi_agent_poc.model import agnostic_model

def load_skill_from_dir(path: pathlib.Path) -> models.Skill:
    """Polyfill for loading a skill from a directory."""
    skill_md = path / "SKILL.md"
    content = skill_md.read_text(encoding="utf-8")
    
    parts = content.split("---")
    if len(parts) >= 3:
        frontmatter = yaml.safe_load(parts[1])
        instructions_parts = [parts[i] for i in range(2, len(parts))]
        instructions = "---".join(instructions_parts).strip()
    else:
        frontmatter = {"name": "car-repair", "description": "Car repair skill"}
        instructions = content.strip()
    
    references = {}
    ref_dir = path / "references"
    if ref_dir.exists():
        for ref_file in ref_dir.glob("*.md"):
            references[ref_file.name] = ref_file.read_text(encoding="utf-8")
            
    return models.Skill(
        frontmatter=models.Frontmatter(
            name=frontmatter.get("name", "skill"),
            description=frontmatter.get("description", "A skill")
        ),
        instructions=instructions,
        resources=models.Resources(references=references)
    )

# ── Load the car repair skill from the skills directory ──────────────────
car_repair_skill = load_skill_from_dir(
    pathlib.Path(__file__).parent.parent / "skills" / "car_repair"
)

car_repair_toolset = SkillToolset(skills=[car_repair_skill])


# ── Agent Definition ─────────────────────────────────────────────────────
car_repair_agent = Agent(
    name="car_repair_agent",
    model=agnostic_model,
    description=(
        "Expert automotive mechanic agent that can diagnose car problems, "
        "recommend repairs, estimate costs (in USD and COP), and provide "
        "maintenance schedules. Delegate to this agent when the user asks "
        "about car issues, strange noises, warning lights, vehicle maintenance, "
        "or anything related to automotive repair."
    ),
    instruction=(
        "You are a seasoned automotive expert and certified mechanic with "
        "over 20 years of experience. You help users diagnose car problems, "
        "understand maintenance needs, and make informed repair decisions.\n\n"
        "## Session Context (from previous interactions):\n"
        "- Last weather city: {last_weather_city?}\n"
        "- Last weather report: {last_weather_report?}\n"
        "Use weather context if relevant (e.g., rainy conditions affect "
        "driving safety recommendations).\n\n"
        "## How to Help:\n"
        "1. Use the **car-repair-expert** skill to look up diagnostic "
        "reference data and maintenance schedules.\n"
        "2. When diagnosing issues, always ask about:\n"
        "   - Vehicle make, model, and year\n"
        "   - Specific symptoms (sounds, smells, lights, timing)\n"
        "   - Recent service history if relevant\n"
        "3. Provide cost estimates in **both USD and COP**.\n"
        "4. Rate severity: Low / Medium / High / Critical.\n"
        "5. Always prioritize **safety** — if brakes, steering, or tires "
        "are involved, recommend immediate professional inspection.\n\n"
        "## IMPORTANT: Scope Boundaries\n"
        "- You can ONLY handle automotive repair and maintenance topics.\n"
        "- If the user asks about weather, SQL, currency conversion, or "
        "customer service, complete ONLY your car-repair-related part and "
        "IMMEDIATELY transfer back to the orchestrator.\n"
        "- NEVER try to answer questions outside automotive topics."
    ),
    tools=[car_repair_toolset],
    output_key="car_repair_output",
)
