"""
Agnostic Model Configuration for Google ADK.

This module defines the primary model (Gemini) and the fallback model (OpenAI GPT-4).
It uses Google ADK's LiteLlm wrapper to manage the multi-model logic.
"""

# from google.adk.models import LiteLlm  # Removed as Gemini native is preferred for multimodal

# ── Agnostic Model Definition ───────────────────────────────────────────

# We use the native Gemini integration for robust multimodal (audio/image) support.
# LiteLlm is avoided here because it currently has incompatible mapping for audio files.
from google.adk.models import Gemini

agnostic_model = Gemini(
    model="gemini-2.0-flash"
)
