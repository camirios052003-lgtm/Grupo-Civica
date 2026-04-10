#!/usr/bin/env python3
"""
Test script for Audio Live Agent
"""

import httpx
import asyncio
import uuid

BASE_URL = "http://127.0.0.1:8000"
APP_NAME = "multi_agent_poc"
USER_ID = "test_user"

async def test_audio_agent():
    """Test the audio agent with a simple voice-related query"""

    print("="*80)
    print("Testing Audio Live Agent")
    print("="*80)

    session_id = str(uuid.uuid4())

    async with httpx.AsyncClient(timeout=120.0) as client:
        # Create session
        await client.post(
            f"{BASE_URL}/apps/{APP_NAME}/users/{USER_ID}/sessions",
            json={"sessionId": session_id}
        )

        # Test message
        message = "I want to have a voice conversation"

        print(f"\nUser: {message}\n")

        response = await client.post(
            f"{BASE_URL}/run",
            json={
                "appName": APP_NAME,
                "userId": USER_ID,
                "sessionId": session_id,
                "newMessage": {
                    "parts": [{"text": message}],
                    "role": "user"
                },
                "streaming": False
            }
        )

        if response.status_code == 200:
            events = response.json()

            # Extract response
            agent_response = ""
            for event in events:
                if isinstance(event, dict) and "content" in event:
                    content = event["content"]
                    if isinstance(content, dict) and "parts" in content:
                        for part in content["parts"]:
                            if isinstance(part, dict) and "text" in part:
                                agent_response += part["text"]

            print(f"Agent Response:\n{agent_response}\n")
            print("="*80)
            print("✓ Audio Agent Test PASSED")
            print("="*80)
        else:
            print(f"✗ Test FAILED: {response.status_code}")
            print(response.text)

if __name__ == "__main__":
    asyncio.run(test_audio_agent())
