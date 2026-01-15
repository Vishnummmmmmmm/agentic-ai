# agents/executor.py

from tools.web_search import WebSearchTool


class ExecutorAgent:
    def __init__(self):
        self.web = WebSearchTool()

    def run(self, task: dict):
        if task["tool"] == "web_search":
            return self.web.search(task["query"])

        return None, []
