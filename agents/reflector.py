class ReflectorAgent:
    def run(self, data: dict) -> dict:
        return {
            "action": "RETRY",
            "reason": "Quality threshold not met"
        }
