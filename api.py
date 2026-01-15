# api.py

from fastapi import FastAPI
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent

app = FastAPI()

planner = PlannerAgent()
executor = ExecutorAgent()


@app.get("/")
def health():
    return {"status": "Agentic AI API running"}


@app.post("/query")
def query_agent(data: dict):
    plan = planner.plan(data["query"])
    answer, sources = executor.run(plan)

    return {
        "answer": answer,
        "sources": sources
    }
