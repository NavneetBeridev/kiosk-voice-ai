import unittest
from src.llm.gameplay_logic import GuessTheAnimalGame

class AutomatedEvaluation(unittest.TestCase):
    \"\"\"
    Automated evaluation pipeline for model performance.
    Used for regression testing and continuous improvement.
    \"\"\"
    def setUp(self):
        self.game = GuessTheAnimalGame()
        self.test_cases = [
            {\"input\": \"Large gray animal with a trunk\", \"target\": \"Elephant\", \"expected_correct\": True},
            {\"input\": \"Small bird with colorful feathers\", \"target\": \"Parrot\", \"expected_correct\": True},
            {\"input\": \"A very fast turtle\", \"target\": \"Cheetah\", \"expected_correct\": False},
        ]

    def test_accuracy(self):
        \"\"\"Evaluates LLM output accuracy for gameplay logic.\"\"\"
        correct_count = 0
        for case in self.test_cases:
            result = self.game.forward(
                history=[], 
                child_input=case[\"input\"], 
                target_animal=case[\"target\"]
            )
            if result.is_correct == case[\"expected_correct\"]:
                correct_count += 1
        
        accuracy = (correct_count / len(self.test_cases)) * 100
        print(f\"[*] Evaluation Accuracy: {accuracy}%\")
        self.assertGreaterEqual(accuracy, 80.0)

if __name__ == \"__main__\":
    unittest.main()