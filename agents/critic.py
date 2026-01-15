class CriticAgent:
    def review(self, answer: str) -> str:
        if not answer or len(answer) < 10:
            return "❌ Answer is insufficient"
        return answer
