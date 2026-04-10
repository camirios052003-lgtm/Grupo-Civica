#!/usr/bin/env python3
"""
Final test script for multi-agent PoC scenarios
Creates sessions and tests all scenarios from the README
"""

import httpx
import asyncio
import uuid
import json

BASE_URL = "http://127.0.0.1:8000"
APP_NAME = "multi_agent_poc"
USER_ID = "test_user"

async def create_session(client: httpx.AsyncClient, session_id: str):
    """Create a new session"""
    response = await client.post(
        f"{BASE_URL}/apps/{APP_NAME}/users/{USER_ID}/sessions",
        json={"sessionId": session_id}
    )
    return response.status_code == 200

async def send_message(client: httpx.AsyncClient, session_id: str, message: str):
    """Send a message to a session"""
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
    return response

async def extract_response_text(events):
    """Extract response text from events"""
    response_text = ""
    for event in events:
        if isinstance(event, dict):
            # Try different event structures
            if "content" in event:
                content = event["content"]
                if isinstance(content, dict) and "parts" in content:
                    for part in content["parts"]:
                        if isinstance(part, dict) and "text" in part:
                            response_text += part["text"]
    return response_text

async def test_scenario(scenario_num: int, scenario_name: str, user_message: str):
    """Test a single scenario"""
    print(f"\n{'='*80}")
    print(f"SCENARIO {scenario_num}: {scenario_name}")
    print(f"{'='*80}")
    print(f"USER: {user_message}\n")

    session_id = str(uuid.uuid4())

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            # Step 1: Create session
            session_created = await create_session(client, session_id)
            if not session_created:
                print("AGENT RESPONSE:")
                print("ERROR: Failed to create session")
                print(f"\n{'-'*80}")
                print(f"Status: ✗ FAILED (Session Creation)")
                print(f"{'-'*80}")
                return False

            # Step 2: Send message
            response = await send_message(client, session_id, user_message)

            if response.status_code == 200:
                events = response.json()
                agent_response = await extract_response_text(events)

                if not agent_response:
                    # If no text extracted, show raw event info
                    agent_response = f"Success - {len(events)} events received"

                print(f"AGENT RESPONSE:")
                print(f"{agent_response}")
                print(f"\n{'-'*80}")
                print(f"Status: ✓ SUCCESS")
                print(f"{'-'*80}")
                return True
            else:
                print(f"AGENT RESPONSE:")
                print(f"HTTP {response.status_code}: {response.text[:500]}")
                print(f"\n{'-'*80}")
                print(f"Status: ✗ FAILED")
                print(f"{'-'*80}")
                return False

    except Exception as e:
        print(f"AGENT RESPONSE:")
        print(f"ERROR: {str(e)}")
        print(f"\n{'-'*80}")
        print(f"Status: ✗ FAILED")
        print(f"{'-'*80}")
        return False

async def run_all_tests():
    """Run all test scenarios from the README"""

    print("\n" + "="*80)
    print("MULTI-AGENT POC - COMPREHENSIVE SCENARIO TESTING")
    print("Testing all scenarios from README.md")
    print("="*80)

    results = []

    # Test 1: Weather Tool
    results.append(await test_scenario(
        1, "Weather Tool",
        "What's the weather in Bogota?"
    ))
    await asyncio.sleep(2)

    # Test 2: Currency Conversion
    results.append(await test_scenario(
        2, "Currency Conversion",
        "Convert 1,000,000 COP to USD"
    ))
    await asyncio.sleep(2)

    # Test 3: SQL Expert
    results.append(await test_scenario(
        3, "SQL Expert",
        "Write a SQL query to find the top 5 customers by total purchases"
    ))
    await asyncio.sleep(2)

    # Test 4: Customer Service
    results.append(await test_scenario(
        4, "Customer Service",
        "What is your return policy?"
    ))
    await asyncio.sleep(2)

    # Test 5: Customer Service (Spanish)
    results.append(await test_scenario(
        5, "Customer Service - Bilingual",
        "Quiero revisar el estado de mi pedido #12345"
    ))
    await asyncio.sleep(2)

    # Test 6: Multi-Agent Orchestration
    results.append(await test_scenario(
        6, "Multi-Agent Orchestration",
        "What's the weather in Medellin, then write a SQL query to save that weather data"
    ))
    await asyncio.sleep(2)

    # Test 7: Car Repair Expert
    results.append(await test_scenario(
        7, "Car Repair Expert",
        "My 2019 Toyota Corolla is making a squealing noise when I brake. What could be wrong?"
    ))
    await asyncio.sleep(2)

    # Test 8: Multimodal Fun Agent
    results.append(await test_scenario(
        8, "Multimodal Fun Agent",
        "Tell me a joke about robots"
    ))
    await asyncio.sleep(2)

    # Test 9: Complex Multi-Agent
    results.append(await test_scenario(
        9, "Complex Multi-Agent Flow",
        "Convert 2,000,000 COP to USD, then tell me if that's enough to fix squealing brakes"
    ))

    # Print summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    total = len(results)
    passed = sum(results)
    failed = total - passed

    print(f"Total Tests: {total}")
    print(f"Passed: {passed} ✓")
    print(f"Failed: {failed} ✗")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    print("="*80 + "\n")

    return results

if __name__ == "__main__":
    asyncio.run(run_all_tests())
