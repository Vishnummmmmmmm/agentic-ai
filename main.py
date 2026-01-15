from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from memory.vector_store import VectorMemory

def main():
    goal = "What is Agentic AI and how is it used in industry?"

    planner = PlannerAgent()
    executor = ExecutorAgent()
    memory = VectorMemory()

    print("\n🔁 Checking memory...")
    past = memory.search(goal)
    for p in past:
        print("📌 Past memory:", p)

    tasks = planner.run(goal)

    for task in tasks:
        answer, sources = executor.run(task)

        print("\n✅ ANSWER:\n", answer)
        print("\n🔗 SOURCES:")
        for s in sources:
            print("-", s)

        memory.add(answer)

if __name__ == "__main__":
    main()
