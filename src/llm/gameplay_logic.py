import dspy
from typing import List, Dict

class KioskGameSignature(dspy.Signature):
    \"\"\"
    Interactive gameplay logic for McDonald's kiosks.
    Identifies the animal based on a child's description and manages game state.
    \"\"\"
    history: List[Dict[str, str]] = dspy.InputField(desc=\"The previous conversation history.\")
    child_input: str = dspy.InputField(desc=\"The child's voice input from the STT stream.\")
    target_animal: str = dspy.InputField(desc=\"The animal the child is trying to describe.\")
    
    response: str = dspy.OutputField(desc=\"The AI's guiding response for the next turn.\")
    is_correct: bool = dspy.OutputField(desc=\"True if the child correctly identified the animal.\")

class GuessTheAnimalGame(dspy.Module):
    \"\"\"
    LLM-driven gameplay state management using DSPy.
    Optimized for high-accuracy and real-time STT/TTS integration.
    \"\"\"
    def __init__(self, model_name: str = \"anthropic.claude-3-5-sonnet-20240620\"):
        super().__init__()
        self.lm = dspy.LM(model_name)
        self.predictor = dspy.ChainOfThought(KioskGameSignature)

    def forward(self, history: List[Dict[str, str]], child_input: str, target_animal: str):
        with dspy.settings.context(lm=self.lm):
            return self.predictor(history=history, child_input=child_input, target_animal=target_animal)

if __name__ == \"__main__\":
    # Example initialization for a mobile device deployment
    game = GuessTheAnimalGame()
    result = game.forward(
        history=[],
        child_input=\"It's a big yellow cat with black stripes and a loud roar!\",
        target_animal=\"Tiger\"
    )
    print(f\"[*] AI Response: {result.response}\")
    print(f\"[*] Correct: {result.is_correct}\")