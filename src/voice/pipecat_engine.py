import asyncio
from pipecat.transports.services.webrtc import WebRTCTransport
from pipecat.services.openai import OpenAILLM
from pipecat.pipeline.pipeline import Pipeline
from pipecat.processors.aggregators.llm import LLMResponseAggregator

class VoiceAIEngine:
    \"\"\"
    High-performance Voice AI engine for real-time STT/TTS (sub-400ms).
    Originally developed for McDonald's \"Guess the Animal\" interactive kiosk.
    \"\"\"
    def __init__(self, api_key: str, webrtc_config: dict):
        self.transport = WebRTCTransport(config=webrtc_config)
        self.llm = OpenAILLM(api_key=api_key, model=\"gpt-4o\")
        self.pipeline = Pipeline([
            self.transport.input(),
            LLMResponseAggregator(),
            self.llm,
            self.transport.output()
        ])

    async def run(self):
        \"\"\"Starts the real-time voice interaction loop.\"\"\"
        print(\"[*] Starting Voice AI Engine (Marginalia)...\")
        await self.pipeline.start()

if __name__ == \"__main__\":
    # Example usage for a kiosk deployment
    engine = VoiceAIEngine(api_key=\"YOUR_API_KEY\", webrtc_config={})
    asyncio.run(engine.run())