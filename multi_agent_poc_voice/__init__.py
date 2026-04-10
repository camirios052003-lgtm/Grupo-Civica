"""
Multi-Agent PoC - Voice Edition

This is the VOICE version of the multi-agent system.
Uses gemini-2.5-flash-native-audio-latest for Live API support.

Use this when you want to use the microphone button!
"""

from .agent_voice import root_agent

__all__ = ["root_agent"]
