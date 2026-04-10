# 🤖 Multi-Agent PoC — Google ADK

A **Proof of Concept** multi-agent system built with the [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/).

## 🏗️ Architecture

```
                    ┌─────────────────────┐
                    │   ROOT ORCHESTRATOR  │
                    │    (Agnostic LLM)    │
                    └──────────┬──────────┘
                               │
            ┌──────────────────┼──────────────────┐
            ▼                  ▼                  ▼
   ┌────────────────┐ ┌───────────────┐ ┌─────────────────────┐
   │  Tools Agent   │ │  SQL Expert   │ │ Customer Service     │
   │                │ │  Agent        │ │ Agent                │
   │ • get_weather  │ │               │ │                      │
   │ • cop_to_usd   │ │ (LLM Skill)  │ │ (LLM Skill)          │
   └────────────────┘ └───────────────┘ └─────────────────────┘
```

### Components

| Component | Type | Description |
|---|---|---|
| **Orchestrator** | Root Agent | Routes user requests to the right specialist |
| **Tools Agent** | Sub-Agent + Tools | Weather lookups & COP→USD conversion |
| **SQL Expert** | Sub-Agent (LLM Skill) | Writes, debugs & optimizes SQL queries |
| **Customer Service** | Sub-Agent (LLM Skill) | Handles support for "TiendaCool" e-commerce |
| **Car Repair Expert** | Sub-Agent (ADK Skill) | Automotive diagnostics with knowledge base |
| **Multimodal Fun** | Sub-Agent + Tools | Jokes, GIFs, memes, and creative content |
| **Audio Live** | Sub-Agent (Gemini Live API) | Real-time audio streaming & voice conversations |

## 📋 Prerequisites

- Python 3.10+
- [Google AI Studio API key](https://aistudio.google.com/apikey) (Primary model)
- [OpenAI API key](https://platform.openai.com/api-keys) (Backup/Fallback model)

## ⚡ Running Locally (Step-by-Step)

```bash
# 1. Create virtual environment
python -m venv .venv

# 2. Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your API keys in .env file
# Edit .env and add:
# GOOGLE_API_KEY=your_key_here
# OPENAI_API_KEY=your_key_here

# 5. Start the ADK web interface
adk web
```

Then open **http://localhost:8000** and select **`multi_agent_poc`** from the dropdown.

## 🚀 Quick Start

### 1. Clone & Enter the project

```bash
cd /Users/leonardotalero/Documents/PoC_adk
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Edit the `.env` file and replace the placeholder:

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_REAL_KEY_HERE
OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE
```

### 5. Run with ADK Web UI 🎉

```bash
adk web
```

Then open **http://localhost:8000** in your browser.

Select **`multi_agent_poc`** from the agent dropdown to start chatting!

## 💬 Example Prompts to Try

### 🌦️ Weather Tool
> "What's the weather in Bogota?"
> "Compare the weather between Medellin and Tokyo."
> "I'm going to London tomorrow, what should I pack based on the weather?"

### 💰 Currency Conversion Tool
> "Convert 1,000,000 COP to USD."
> "How much is 500,000 Colombian Pesos in dollars?"
> "If I have 2.5 million pesos and want to buy a $600 USD phone, do I have enough money?"

### 🗃️ SQL Expert Skill
> "Write a SQL query to find the top 10 customers by total purchases."
> "Create a table for 'Products' with name, price, and stock in PostgreSQL."
> "Explain how a LEFT JOIN differs from an INNER JOIN with a clear example."
> "How do I optimize a slow query that involves multiple joins on a large table?"
> "Show me how to use a window function to calculate a running total of sales."

### 🛒 Customer Service Skill
> "I want to check the status of my order #12345."
> "What is your return policy?"
> "Me gustaría hacer una devolución porque el producto llegó roto." *(Bilingual support)*
> "Do you accept payment via Nequi or PSE?"
> "My order #99887 is late and I'm very frustrated, I need help now!"

### 🔀 Multi-Agent / Orchestration
> "Hello! First, give me the weather in Medellin. Then, help me write a SQL query to save that info."
> "If I have 1,500,000 COP, how many dollars is that? Also, can I use that to buy a product at TiendaCool?"
> "Help me! I'm failing to write a query, and I also need to know the weather in New York."

### 🔧 Car Repair Expert (ADK Skill)
> "My 2019 Toyota Corolla is making a squealing noise when I brake. What could be wrong?"
> "What maintenance should I do at 50,000 km?"
> "My car won't start — I hear a clicking sound. What should I check?"
> "How much does a timing belt replacement cost in Colombia?"
> "My check engine light is on and the car is overheating. Is it safe to keep driving?"

### 🎭 Multimodal & Fun Agent
> "Tell me a joke about a robot and find a funny coding GIF."
> "Generate a 'pika' meme saying 'When the code works' on top and 'on the first try' on bottom."
> "Write a dad joke about electric cars."
> "Give me a 'doge' meme about AI taking over the world."
> "Analyze this image [attach image] and make a funny meme about it."

### 🎙️ Audio Live Agent (Gemini Live API)
> "I want to have a voice conversation" *(Enables real-time audio chat)*
> "Transcribe this audio file for me" *[attach audio file]*
> "Can you respond to me with voice?" *(Audio output generation)*
> "Listen to this voice message and tell me what it says" *[attach voice message]*
> "I want to practice my Spanish pronunciation" *(Voice-based language learning)*

### 🔄 Multi-Agent / Orchestration (Advanced)
> "Tell me the weather in Bogota, then show me a funny GIF about it."
> "If 1,000,000 COP is $240 USD, do I have enough money to fix a squealing brake? And also, write a SQL query to log this."
> "Listen to this audio [attach audio] — is my engine knocking? Then tell me a joke to cheer me up."
> "My car won't start and it's raining in London. What should I do? Find me a GIF for my situation."
> "I need to return an item to TiendaCool. Can you write a SQL query to find all my previous orders first?"

## 🤖 Agnostic LLM & Fallback Support

This PoC implements a **Model-Agnostic** strategy using the **LiteLLM** integration within ADK. This allows the system to remain resilient even if the primary model provider experiences downtime or rate limiting.

- **Primary Model**: `gemini/gemini-2.0-flash` (Google)
- **Backup Model**: `openai/gpt-4` (OpenAI)

The configuration is centralized in `multi_agent_poc/model.py`, meaning all agents automatically benefit from this fallback logic. If a request to Gemini fails, ADK intelligently retries the request using GPT-4.

## 🧠 Session State (Shared Memory Between Agents)

This PoC uses **ADK Session State** to enable agents to share data with each other during a conversation. State acts as a shared scratchpad where tools write results and agents read them.

### How It Works

State is managed at three levels:

| Mechanism | Where | What it does |
|---|---|---|
| **`ToolContext.state`** | Inside `tools.py` | Tools write their results (weather data, conversion amounts) directly into session state |
| **`output_key`** | On each sub-agent | Every sub-agent's final response is automatically saved to a named state key |
| **Instruction references** | In agent prompts | Agents are told which state keys to check for data from previous steps |

### State Keys Reference

#### Written by Tools (via `ToolContext`)

| Key | Written by | Example Value |
|---|---|---|
| `last_weather_city` | `get_weather` | `"Medellin"` |
| `last_weather_data` | `get_weather` | `'{"temp_celsius": 24, ...}'` (JSON) |
| `last_weather_report` | `get_weather` | `"Weather in Medellin: Pleasant..."` |
| `weather_query_count` | `get_weather` | `3` |
| `last_conversion_cop` | `convert_cop_to_usd` | `1000000.0` |
| `last_conversion_usd` | `convert_cop_to_usd` | `240.96` |
| `last_conversion_rate` | `convert_cop_to_usd` | `4152.35` |
| `conversion_count` | `convert_cop_to_usd` | `2` |

#### Written by Agents (via `output_key`)

| Key | Written by | Contains |
|---|---|---|
| `tools_agent_output` | Tools Agent | Full text response from the tools specialist |
| `sql_expert_output` | SQL Expert Agent | Full text response with SQL queries |
| `customer_service_output` | Customer Service Agent | Full support response |

### 💡 Example: Cross-Agent Data Flow with State

Try this multi-step conversation to see state in action:

**Step 1** — Ask for weather data:
> "What's the weather in Bogota?"

*→ `tools_agent` fetches weather → saves `last_weather_city=Bogota` and `last_weather_data={...}` to state*

**Step 2** — Ask SQL to use that data:
> "Now write me an INSERT query to store that weather data in a PostgreSQL table"

*→ `sql_expert_agent` reads `last_weather_city` and `last_weather_data` from state → writes a concrete INSERT with real values (18°C, 72% humidity, etc.)*

**Step 3** — Convert currency:
> "Convert 2,000,000 COP to USD"

*→ `tools_agent` does conversion → saves `last_conversion_usd=481.93` to state*

**Step 4** — Customer service uses that context:
> "I'd like to buy a product worth $500 USD at TiendaCool. Do I have enough based on my last conversion?"

*→ `customer_service_agent` can reference the conversion data from state*

### 🔄 State Scope Prefixes (Advanced)

ADK supports scoping state with prefixes:

| Prefix | Scope | Persistence | Example |
|---|---|---|---|
| *(none)* | Current session | Session lifetime | `state["last_weather_city"]` |
| `user:` | Per user, all sessions | Persistent | `state["user:preferred_language"]` |
| `app:` | All users, all sessions | Persistent | `state["app:api_version"]` |
| `temp:` | Current invocation only | Discarded after turn | `state["temp:raw_api_response"]` |

## 📁 Project Structure

```
PoC_adk/
├── .env                         # API key configuration
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── multi_agent_poc/             # ADK agent package
    ├── __init__.py              # Package init (imports agent)
    ├── model.py                 # Centralized Agnostic LLM configuration
    ├── agent.py                 # Root orchestrator (root_agent)
    ├── tools.py                 # Function tools (weather, COP→USD)
    ├── skills/                  # ADK Skills (knowledge packs)
    │   └── car_repair/          # Car repair expert skill
    │       ├── SKILL.md         # Skill definition + instructions
    │       └── references/      # Reference materials
    │           ├── common_problems.md       # Diagnostic tables
    │           └── maintenance_schedule.md  # Service intervals
    └── sub_agents/              # Specialist sub-agents
        ├── __init__.py
        ├── tools_agent.py       # Agent with weather & currency tools
        ├── sql_expert_agent.py  # SQL expert (LLM skill)
        ├── customer_service_agent.py  # Customer support (LLM skill)
        ├── car_repair_agent.py  # Car repair expert (ADK Skill)
        ├── multimodal_fun_agent.py  # Jokes, GIFs, memes (Multimodal)
        └── audio_live_agent.py  # Real-time audio streaming (Gemini Live API)
```

## 🔑 Key Concepts Demonstrated

1. **Multi-Agent Architecture** — Root agent delegates to specialized sub-agents
2. **Function Tools** — `get_weather` and `convert_cop_to_usd` are plain Python functions auto-wrapped by ADK
3. **LLM Skills** — SQL Expert and Customer Service agents use only prompt engineering (no tools)
4. **ADK Skills** — Car Repair Expert uses the `SkillToolset` feature with file-based skill definitions (`SKILL.md` + `references/`)
5. **LLM-Driven Delegation** — Gemini reads sub-agent descriptions and routes autonomously
6. **Agnostic LLM & Fallback** — Centralized model configuration using `LiteLlm` with primary (Gemini) and backup (GPT-4) support
7. **Session State** — Tools save results via `ToolContext.state`, agents read/write via `output_key`, enabling cross-agent data sharing
8. **Multimodal Fun** — `multimodal_fun_agent` handles creative tasks and multimodal input (jokes/GIFs/memes)
9. **Audio Streaming** — `audio_live_agent` uses Gemini Live API for real-time audio conversations and voice interactions
10. **ADK Web UI** — `adk web` provides a chat interface for testing

## 📚 Resources

- [ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Quickstart](https://google.github.io/adk-docs/get-started/quickstart/)
- [Multi-Agent Systems Guide](https://google.github.io/adk-docs/agents/multi-agents/)
- [Google AI Studio](https://aistudio.google.com/)
