from langfuse import Langfuse
from langfuse.openai import openai

class LLMOpsObservability:
    \"\"\"
    LLM-Ops observability with Langfuse for real-time monitoring.
    Used for model debugging, performance tracking, and production roll-outs.
    \"\"\"
    def __init__(self, public_key: str, secret_key: str, host: str):
        self.langfuse = Langfuse(
            public_key=public_key, 
            secret_key=secret_key, 
            host=host
        )

    def track_call(self, prompt: str, response: str, metadata: dict):
        \"\"\"Tracks an LLM call with metadata (cost, latency, user_id).\"\"\"
        trace = self.langfuse.trace(
            name=\"voice-kiosk-interaction\",
            user_id=metadata.get(\"user_id\"),
            metadata=metadata
        )
        trace.span(
            name=\"llm-generation\",
            input=prompt,
            output=response,
            metadata=metadata
        )
        print(\"[*] Trace logged to Langfuse.\")

if __name__ == \"__main__\":
    # Example usage for LLM-Ops monitoring in production
    monitor = LLMOpsObservability(public_key=\"PK\", secret_key=\"SK\", host=\"https://cloud.langfuse.com\")
    # monitor.track_call(prompt=\"Hi!\", response=\"Hello!\", metadata={\"model\": \"llama-3.1\", \"latency\": 0.350})