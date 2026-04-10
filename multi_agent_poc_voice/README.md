# Multi-Agent PoC - Voice Version

This is the **VOICE version** of the multi-agent system using Google ADK with Live API support.

## Model

Uses **Gemini 2.5 Flash Native Audio** (`gemini-2.5-flash-native-audio-latest`)

## Capabilities

This version supports:
- ✅ Real-time microphone streaming (v1alpha bidiGenerateContent API)
- ✅ Voice input/output interactions
- ✅ Audio transcription in real-time
- ✅ Natural voice conversations
- ✅ Multilingual audio support
- ⚠️ **Limited text chat support** (may have compatibility issues with some features)

## When to Use This Version

Choose the **voice version** when you need:
- Real-time microphone input via ADK Web UI
- Voice-to-voice conversations
- Live audio streaming
- Natural spoken interactions
- Hands-free operation

## Available Sub-Agents

The voice version orchestrator delegates to the same 6 specialist agents:

1. **tools_agent** - Weather & COP-USD currency conversion
2. **sql_expert_agent** - SQL queries, database design, optimization
3. **customer_service_agent** - E-commerce support (TiendaCool)
4. **car_repair_agent** - Automotive diagnostics & repair advice
5. **multimodal_fun_agent** - Jokes, GIFs, memes, humor
6. **audio_live_agent** - Real-time audio conversations

## How to Use

### Start ADK Web UI
```bash
adk web
```

### Select Agent
In the ADK web interface dropdown, select:
- **multi_agent_poc_voice** (this voice version)

### Enable Microphone

1. Click the **microphone button** in the ADK Web UI
2. Allow microphone permissions in your browser
3. Speak your request
4. The agent will respond with voice output

### Example Voice Interactions (English & Spanish)

#### Weather Queries (Spoken) 🌤️

**English:**
> "What's the weather like in Bogotá?"
> "Tell me the weather forecast for New York"
> "How hot is it in Medellín right now?"

**Spanish:**
> "¿Cómo está el clima en Bogotá?"
> "Dime el pronóstico del tiempo para Nueva York"
> "¿Qué temperatura hace en Medellín ahora?"

#### Currency Conversion (Spoken) 💱

**English:**
> "How much is fifty thousand Colombian pesos in US dollars?"
> "Convert one hundred thousand COP to USD"
> "What's the exchange rate for Colombian pesos today?"

**Spanish:**
> "¿Cuánto son cincuenta mil pesos colombianos en dólares?"
> "Convierte cien mil COP a USD"
> "¿A cuánto está el peso colombiano hoy?"

#### SQL Help (Spoken) 🗄️

**English:**
> "I need help writing a query to find users who haven't logged in for 90 days"
> "How do I create a table for customer orders?"
> "Explain what an inner join does"

**Spanish:**
> "Necesito ayuda escribiendo una consulta para encontrar usuarios inactivos"
> "¿Cómo creo una tabla para pedidos de clientes?"
> "Explica qué hace un inner join"

#### Customer Service (Spoken) 🛍️

**English:**
> "I want to return an item from my recent order"
> "Where's my package? My order number is O-R-D dash two zero two four dash zero zero one"
> "What's your refund policy?"
> "Do you accept PayPal?"

**Spanish:**
> "Quiero devolver un artículo de mi pedido reciente"
> "¿Dónde está mi paquete? Mi número de orden es O-R-D guión dos cero dos cuatro guión cero cero uno"
> "¿Cuál es su política de reembolsos?"
> "¿Aceptan PayPal?"

#### Car Repair (Spoken) 🚗

**English:**
> "My check engine light came on and the car is shaking"
> "There's a squealing noise when I brake"
> "How often should I change my oil in a Honda Civic?"
> "My car won't start, what should I check?"

**Spanish:**
> "Se prendió la luz de check engine y el carro está temblando"
> "Hay un ruido chillón cuando freno"
> "¿Cada cuánto debo cambiar el aceite en un Honda Civic?"
> "Mi carro no enciende, ¿qué debo revisar?"

#### Fun Interactions (Spoken) 😄

**English:**
> "Tell me a joke about programmers"
> "Make me laugh with a dad joke"
> "Why did the chicken cross the road?"
> "Tell me something funny about artificial intelligence"

**Spanish:**
> "Cuéntame un chiste de programadores"
> "Hazme reír con un chiste malo"
> "¿Por qué cruzó el pollo la carretera?"
> "Dime algo gracioso sobre inteligencia artificial"

#### Voice Conversations (Spoken) 🎙️

**English:**
> "Let's have a voice conversation about my day"
> "I want to chat about the weather and make some plans"
> "Can we talk about what's on my mind?"

**Spanish:**
> "Quiero tener una conversación de voz sobre mi día"
> "Hablemos sobre el clima y hacer algunos planes"
> "¿Podemos hablar sobre lo que estoy pensando?"

#### Audio Transcription (Spoken) 🎵

**English:**
> "Can you transcribe this audio file?"
> "What's being said in this recording?"
> "Listen to this voice message and summarize it"

**Spanish:**
> "¿Puedes transcribir este archivo de audio?"
> "¿Qué se dice en esta grabación?"
> "Escucha este mensaje de voz y resúmelo"

#### Multi-Step Requests (Spoken) 🔄

**English:**
> "First, tell me the weather in Cali, then write a SQL query for today's sales"
> "Convert one hundred thousand pesos to dollars and check if that's enough for free shipping"
> "What's the weather in Medellín? And then tell me a joke about rain"

**Spanish:**
> "Primero, dime el clima en Cali, luego escribe una consulta SQL para las ventas de hoy"
> "Convierte cien mil pesos a dólares y revisa si alcanza para envío gratis"
> "¿Cómo está el clima en Medellín? Y luego cuéntame un chiste sobre lluvia"

#### Mixed Language Examples (Bilingual) 🌍

**English → Spanish:**
> "What's the weather in Bogotá? And then help me ask customer service in Spanish about shipping times"

**Spanish → English:**
> "¿Cuánto cuesta el envío a Estados Unidos? And what's the weather like in New York right now?"

**Code-switching (natural bilingual speech):**
> "Necesito saber el weather en Bogotá and también convert fifty thousand pesos to dollars por favor"

### Voice Tips 🎤

- **Speak naturally** - The agent understands conversational language
- **Use pauses** - Take breaks between different requests
- **Speak clearly** - Especially for numbers and order IDs
- **Mix languages** - Spanish and English both work seamlessly
- **Ask follow-ups** - The agent remembers context from earlier in the conversation
- **Spell when needed** - For order numbers, say "O-R-D dash 1-2-3-4-5"

## Architecture

```
root_agent (orchestrator_voice)
├── model: gemini-2.5-flash-native-audio-latest
├── API: v1alpha (bidiGenerateContent - Live API)
└── sub_agents/
    ├── tools_agent
    ├── sql_expert_agent
    ├── customer_service_agent
    ├── car_repair_agent
    ├── multimodal_fun_agent
    └── audio_live_agent
```

## Voice-Specific Features

- **Real-time transcription** - See what you say as text
- **Natural voice responses** - Agent speaks back conversationally
- **Context awareness** - Maintains conversation context across turns
- **Emotion and tone** - Natural-sounding voice with appropriate emotion
- **Interruption handling** - Can handle mid-sentence clarifications

## Session State

The orchestrator maintains context across the conversation:
- Last weather city queried
- Last weather report
- Last COP conversion amount
- Weather query count
- Currency conversion count

## Microphone Button

The microphone button in ADK Web UI:
- **Green/Active**: Recording your voice
- **Gray/Inactive**: Not recording
- Click to toggle recording on/off

## Important Notes

⚠️ **Model Limitation**: This version uses the Native Audio model which is optimized for Live API (v1alpha). Text chat functionality may be limited compared to the text version.

⚠️ **API Compatibility**: The Live API (v1alpha) is different from the standard text API (v1beta). Some text-based features may not work as expected.

## Troubleshooting

### Microphone Not Working
- Ensure browser permissions are granted
- Check that the correct agent (multi_agent_poc_voice) is selected
- Verify model is `gemini-2.5-flash-native-audio-latest`

### Text Chat Issues
If you encounter errors with text chat:
- Switch to **multi_agent_poc** (text version) for pure text interactions
- Use voice input instead of typing

### WebSocket Connection Errors
- Check that ADK web server is running
- Restart the server: `adk web`
- Clear browser cache and reload

## Need Text-Only Support?

If you need reliable text chat without voice features, use:
- **multi_agent_poc** (text version)

See: `../multi_agent_poc/README.md`

## Files

- `agent_voice.py` - Root orchestrator with voice model
- Shared sub-agents from `../multi_agent_poc/sub_agents/`

## Testing

Test the audio agent:
```bash
# Start ADK web in another terminal
adk web

# Run test (requires server running)
source .venv/bin/activate
python test_audio_agent.py
```

The test should confirm the audio agent responds to voice conversation requests.

## Key Difference from Text Version

| Feature | Text Version | Voice Version |
|---------|--------------|---------------|
| Model | gemini-2.5-flash | gemini-2.5-flash-native-audio-latest |
| API | v1beta (generateContent) | v1alpha (bidiGenerateContent) |
| Microphone | ❌ Not supported | ✅ Real-time streaming |
| Text chat | ✅ Fully supported | ⚠️ Limited support |
| Voice output | ❌ Not available | ✅ Natural voice |
| Function calling | ✅ Full support | ⚠️ May vary |
| Best for | Text interactions | Voice conversations |

## Recommendation

- **Use multi_agent_poc** (text) for: Reliable text chat, tools, function calling
- **Use multi_agent_poc_voice** (voice) for: Microphone input, voice conversations

Choose based on your primary interaction mode!
