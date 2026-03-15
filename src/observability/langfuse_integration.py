import logging
from typing import Dict, Any, Optional
from langfuse import Langfuse
from langfuse.openai import openai

logger = logging.getLogger(\"Observability\")

class LLMOpsMonitor:
    \"\"\"
    Production monitoring and observability for LLM-driven interactions.
    Langfuse integration for latency tracking, cost analysis, and model debugging.
    \"\"\"
    def __init__(self, public_key: str, secret_key: str, host: str):
        self._langfuse = Langfuse(
            public_key=public_key, 
            secret_key=secret_key, 
            host=host
        )
        logger.info(\"Observability monitor active for Langfuse\")

    def log_turn(self, prompt: str, completion: str, metadata: Dict[str, Any], user_id: Optional[str] = None):
        \"\"\"Logs a single interaction turn with full metadata tracing.\"\"\"
        try:
            trace = self._langfuse.trace(
                name=\"kiosk-voice-turn\",
                user_id=user_id,
                metadata=metadata
            )
            trace.span(
                name=\"inference-execution\",
                input=prompt,
                output=completion,
                metadata=metadata
            )
        except Exception as e:
            logger.warning(f\"Trace logging failed: {e}\")

if __name__ == \"__main__\":
    # Mocking turn observability
    monitor = LLMOpsMonitor(\"pk\", \"sk\", \"https://cloud.langfuse.com\")
    # monitor.log_turn(\"hi\", \"hello\", {\"model\": \"llama-3.1\", \"latency\": 0.355})