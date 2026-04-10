# Multi-Agent PoC - Text Version

This is the **TEXT version** of the multi-agent system using Google ADK.

## Model

Uses **Gemini 2.5 Flash** (`gemini-2.5-flash`)

## Capabilities

This version supports:
- ✅ Regular text chat (v1beta generateContent API)
- ✅ Function calling and tools
- ✅ Multimodal input (images, documents)
- ✅ Audio file uploads (for analysis, not streaming)
- ✅ Fast and reliable for general use
- ❌ **Does NOT support** real-time microphone streaming (Live API)

## When to Use This Version

Choose the **text version** when you need:
- Reliable text-based chat interactions
- Tool/function calling capabilities
- Image and document analysis
- Audio file transcription/analysis
- Fast responses for general queries

## Available Sub-Agents

The text version orchestrator delegates to 6 specialist agents:

1. **tools_agent** - Weather & COP-USD currency conversion
2. **sql_expert_agent** - SQL queries, database design, optimization
3. **customer_service_agent** - E-commerce support (TiendaCool)
4. **car_repair_agent** - Automotive diagnostics & repair advice
5. **multimodal_fun_agent** - Jokes, GIFs, memes, humor
6. **audio_live_agent** - Audio file analysis (not real-time streaming)

## How to Use

### Start ADK Web UI
```bash
adk web
```

### Select Agent
In the ADK web interface dropdown, select:
- **multi_agent_poc** (this text version)

### Example Prompts (English & Spanish)

#### Weather Queries (tools_agent)

**English:**
```
What's the weather in Bogotá?
How's the weather in New York today?
Tell me about the climate in Tokyo
```

**Spanish:**
```
¿Cómo está el clima en Bogotá?
¿Qué temperatura hace en Medellín?
Cuéntame sobre el clima en Londres
```

#### Currency Conversion (tools_agent)

**English:**
```
Convert 50000 COP to USD
How much is 100,000 Colombian pesos in dollars?
What's the exchange rate for 250,000 COP?
```

**Spanish:**
```
Convierte 50000 pesos colombianos a dólares
¿Cuánto son 100,000 COP en USD?
¿A cuánto está el peso colombiano hoy?
```

#### SQL Help (sql_expert_agent)

**English:**
```
Write a query to get users who made purchases in the last 30 days
Help me create a database schema for an e-commerce store
Optimize this query: SELECT * FROM orders WHERE date > '2024-01-01'
Explain the difference between INNER JOIN and LEFT JOIN
```

**Spanish:**
```
Escribe una consulta para obtener usuarios que compraron en los últimos 30 días
Ayúdame a crear un esquema de base de datos para una tienda en línea
¿Cómo optimizo esta consulta SQL?
Explica la diferencia entre INNER JOIN y LEFT JOIN
```

#### Customer Service (customer_service_agent)

**English:**
```
I need to return an item from order #12345
What's your refund policy?
Where is my package? Order number ORD-2024-001
Do you accept PayPal?
```

**Spanish:**
```
Necesito devolver un producto de mi pedido #12345
¿Cuál es su política de reembolso?
¿Dónde está mi paquete? Número de orden ORD-2024-001
¿Aceptan PayPal?
```

#### Car Repair (car_repair_agent)

**English:**
```
My car makes a squealing noise when I brake
The check engine light came on in my 2015 Honda Civic
How often should I change my oil?
My car won't start, what could be wrong?
```

**Spanish:**
```
Mi carro hace un ruido chillón cuando freno
Se prendió la luz de check engine en mi Honda Civic 2015
¿Cada cuánto debo cambiar el aceite?
Mi carro no enciende, ¿qué puede ser?
```

#### Fun Interactions (multimodal_fun_agent)

**English:**
```
Tell me a programming joke
Make me laugh with a dad joke
Find a funny meme about debugging
Why did the chicken cross the road?
```

**Spanish:**
```
Cuéntame un chiste de programadores
Hazme reír con un chiste malo
Busca un meme gracioso sobre bugs
¿Por qué cruzó el pollo la carretera?
```

#### Audio File Analysis (audio_live_agent)

**English:**
```
[Upload an audio file]
Can you transcribe this audio?
What language is being spoken in this recording?
Summarize what was said in this voice message
```

**Spanish:**
```
[Subir archivo de audio]
¿Puedes transcribir este audio?
¿Qué idioma se habla en esta grabación?
Resume lo que se dijo en este mensaje de voz
```

#### Multi-Step Requests (orchestrator)

**English:**
```
Get weather in Cali and then write a SQL query for today's sales
Convert 100,000 COP to USD and check if that's enough for free shipping
Tell me the weather in Medellín, then tell me a joke about rain
```

**Spanish:**
```
Dame el clima en Cali y luego escribe una consulta SQL para las ventas de hoy
Convierte 100,000 COP a USD y dime si alcanza para envío gratis
Dime el clima en Medellín y luego cuéntame un chiste sobre lluvia
```

#### Mixed Language Examples

**English request with Spanish context:**
```
I want to buy something that costs 200,000 COP, how much is that in dollars?
Then help me ask customer service in Spanish about shipping to Colombia
```

**Spanish request with English context:**
```
¿Cuánto cuesta el envío a Estados Unidos?
And what's the weather like in New York right now?
```

## Architecture

```
root_agent (orchestrator)
├── model: gemini-2.5-flash
├── API: v1beta (generateContent)
└── sub_agents/
    ├── tools_agent
    ├── sql_expert_agent
    ├── customer_service_agent
    ├── car_repair_agent
    ├── multimodal_fun_agent
    └── audio_live_agent
```

## Session State

The orchestrator maintains context across the conversation:
- Last weather city queried
- Last weather report
- Last COP conversion amount
- Weather query count
- Currency conversion count

## Limitations

- **No real-time microphone streaming** - Use `multi_agent_poc_voice` for Live API
- **Text-based interactions only** - Voice responses not available
- Audio files can be uploaded for analysis, but not streamed in real-time

## Need Voice Support?

If you need real-time microphone streaming and voice interactions, use:
- **multi_agent_poc_voice** (voice version)

See: `../multi_agent_poc_voice/README.md`

## Files

- `agent.py` - Root orchestrator with text model
- `model.py` - Model configuration (gemini-2.5-flash)
- `sub_agents/` - All specialist agents
  - `tools_agent.py`
  - `sql_expert_agent.py`
  - `customer_service_agent.py`
  - `car_repair_agent.py`
  - `multimodal_fun_agent.py`
  - `audio_live_agent.py`

## Testing

Run the comprehensive test suite:
```bash
source .venv/bin/activate
python test_final.py
```

All 9 scenarios should pass with 100% success rate.
