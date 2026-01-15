# agents/planner.py

class PlannerAgent:
    def plan(self, query: str):
        return {
            "tool": "web_search",
            "query": query
        }
