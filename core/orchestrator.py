from core.config import Config
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent
from agents.critic import CriticAgent
from agents.reflector import ReflectorAgent

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.verifier = VerifierAgent()
        self.critic = CriticAgent()
        self.reflector = ReflectorAgent()

    def run(self, goal: str):
        plan = self.planner.run(goal)
        results = []

        for task in plan["tasks"]:
            retries = 0

            while retries <= Config.MAX_RETRIES:
                execution = self.executor.run(task)
                verification = self.verifier.run(execution)
                critique = self.critic.run(execution)

                if (
                    verification["status"] == "PASS"
                    and critique["confidence"] >= Config.MIN_CONFIDENCE
                ):
                    results.append(execution)
                    break

                reflection = self.reflector.run({
                    "task": task,
                    "issues": verification.get("issues", [])
                })

                retries += 1

                if retries > Config.MAX_RETRIES:
                    raise RuntimeError("Task failed after retries")

        return results
