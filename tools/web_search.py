# tools/web_search.py

class WebSearchTool:
    def search(self, query: str):
        answer = (
            "Agentic AI systems autonomously plan, "
            "execute, and adapt tasks across tools."
        )

        sources = [
            "https://blogs.nvidia.com/blog/what-is-agentic-ai/",
            "https://www.ibm.com/think/topics/agentic-ai",
            "https://cloud.google.com/discover/what-is-agentic-ai"
        ]

        return answer, sources
