"""
Model Configuration for Google ADK - Text Version

This is the TEXT version of the multi-agent system.
Uses Gemini 2.5 Flash for reliable text chat, tools, and function calling.

For VOICE/Live API support, see: multi_agent_poc_voice package
"""

from google.adk.models import Gemini

# ── Text Model: For Regular Agents (Text Chat, Tools, etc.) ─────────────
agnostic_model = Gemini(
    model="gemini-2.5-flash",
    # This model supports:
    # - Regular text chat (v1beta generateContent)
    # - Function calling and tools
    # - Multimodal input (images, documents)
    # - Audio file uploads
    # - Fast and reliable for general use
    # - All 6 sub-agents work perfectly
)
