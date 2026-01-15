🚀 Agentic AI System (Production-Ready)
📌 Overview

This project is a custom-built Agentic AI system designed to autonomously answer user questions using controlled logic, tools, and memory, instead of relying on large black-box models like ChatGPT.

It is not a chatbot wrapper and does not depend on ChatGPT or OpenAI APIs.

The system:

Accepts any user question

Searches trusted sources

Generates an answer

Returns both the answer and its sources

Can be deployed as a scalable production API

🧠 What Problem Does This Solve?

Traditional chatbots:

Hallucinate answers

Cannot verify sources

Are expensive

Are not controllable

Do not follow enterprise workflows

This system solves that by:

Using explicit reasoning steps

Calling tools deliberately

Storing and reusing memory

Returning traceable outputs

Running independently of ChatGPT

⚙️ How It Works (High Level)

User sends a question via API

Planner decides what needs to be done

Executor performs actions (search, fetch data)

Memory stores useful results

Final answer is returned with sources

🧩 Why Multiple Files? Why Not One File?
❌ Single File Problems

Hard to maintain

Impossible to scale

No separation of responsibility

Breaks easily in production

✅ Multi-File Architecture Benefits
File	Responsibility
api.py	API entry point
agents/planner.py	Decides actions
agents/executor.py	Executes tasks
tools/web_search.py	External data
memory/	Knowledge storage
Dockerfile	Production container

This mirrors real industry systems used by companies like Google, Amazon, and Nvidia.

ChatGPT is general intelligence.
This system is task-driven intelligence.

🎯 Where Is This Used?

Enterprise automation

Internal knowledge systems

Compliance-safe AI

Research assistants

Autonomous agents

Domain-specific AI (finance, legal, healthcare)

🌐 API & Swagger

Once running, access:

Swagger UI:

http://127.0.0.1:8000/docs


Health Check:

http://127.0.0.1:8000/

🐳 Docker (Production Deployment)

Build image:

docker build -t agentic-ai .


Run container:

docker run -p 8000:8000 agentic-ai


Uses:

Gunicorn

Uvicorn workers

FastAPI

📦 Tech Stack

Python 3.11

FastAPI

Uvicorn + Gunicorn

Docker

Sentence Transformers

Modular Agent Architecture

🚀 Why This Exists

This project demonstrates:

Agentic AI

System design

Production readiness

Real-world AI engineering

It is not a demo chatbot — it is an AI system.

🧑‍💻 Author

Vishnu
Building agentic systems, not chatbots.