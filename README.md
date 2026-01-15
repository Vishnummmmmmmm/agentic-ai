===========================================================
        AGENTIC AI SYSTEM — PRODUCTION READY
===========================================================

A modular, tool-driven AI system that answers questions
using controlled logic, memory, and verified sources.

NOT a chatbot.
NOT ChatGPT.
NOT a black-box model.

===========================================================
OVERVIEW
===========================================================

✔ Accepts any user question
✔ Searches trusted external sources
✔ Generates structured answers
✔ Returns answer + sources
✔ Deployable as a scalable API
✔ Runs independently of ChatGPT / OpenAI

===========================================================
API KEY CONFIGURATION
===========================================================

For security reasons, API keys are NOT included.

Create a `.env` file in the project root:

    API_KEY=your_own_api_key_here

✔ `.env` is ignored via .gitignore
✔ API key is loaded at runtime
✔ Users must provide their own key

===========================================================
PROBLEM THIS SOLVES
===========================================================

Traditional Chatbots:
- Hallucinate answers
- No source verification
- Expensive to scale
- No workflow control
- Poor enterprise fit

This System:
- Uses explicit reasoning
- Calls tools intentionally
- Stores memory
- Returns traceable sources
- Designed for production

===========================================================
HOW IT WORKS
===========================================================

[ User Question ]
        |
        v
[ Planner Agent ]
        |
        v
[ Executor Agent ]
        |
        v
[ Tools + Search ]
        |
        v
[ Memory Store ]
        |
        v
[ Answer + Sources ]

===========================================================
WHY MULTIPLE FILES?
===========================================================

Single File System ❌
- Hard to maintain
- Not scalable
- Breaks easily
- No separation of logic

Multi-File System ✅
- Clean architecture
- Industry standard
- Scalable
- Maintainable

-----------------------------------------------------------
FILE STRUCTURE
-----------------------------------------------------------

api.py                 -> API entry point
agents/planner.py      -> Decision logic
agents/executor.py     -> Task execution
tools/web_search.py    -> External data access
memory/                -> Knowledge storage
Dockerfile             -> Production container

===========================================================
CHATBOT vs THIS SYSTEM
===========================================================

+----------------------+----------------+----------------+
| Feature              | Chatbot        | This System   |
+----------------------+----------------+----------------+
| Pretrained replies   | YES            | NO             |
| Tool usage           | NO             | YES            |
| Source tracking      | NO             | YES            |
| Memory               | NO             | YES            |
| Autonomous actions   | NO             | YES            |
| Production ready     | NO             | YES            |
+----------------------+----------------+----------------+

Chatbots talk.
This system ACTS.

===========================================================
CHATGPT vs THIS SYSTEM
===========================================================

+----------------------+----------------+----------------+
| Aspect               | ChatGPT        | This System   |
+----------------------+----------------+----------------+
| Black-box model      | YES            | NO             |
| Custom logic         | NO             | YES            |
| Cost control         | NO             | YES            |
| Data privacy         | NO             | YES            |
| Enterprise workflows | NO             | YES            |
| Offline / Private    | NO             | YES            |
+----------------------+----------------+----------------+

ChatGPT = General Intelligence
This     = Task-Driven Intelligence

===========================================================
USE CASES
===========================================================

✔ Enterprise automation
✔ Internal knowledge systems
✔ Compliance-safe AI
✔ Research assistants
✔ Autonomous agents
✔ Finance / Legal / Healthcare AI

===========================================================
API & SWAGGER
===========================================================

Swagger UI:
http://127.0.0.1:8000/docs

Health Check:
http://127.0.0.1:8000/

===========================================================
DOCKER DEPLOYMENT
===========================================================

Build:
docker build -t agentic-ai .

Run:
docker run -p 8000:8000 agentic-ai

===========================================================
TECH STACK
===========================================================

- Python 3.11
- FastAPI
- Gunicorn + Uvicorn
- Docker
- Sentence Transformers
- Modular Agent Architecture

===========================================================
WHY THIS PROJECT EXISTS
===========================================================

✔ Demonstrates Agentic AI
✔ Shows real system design
✔ Production-ready architecture
✔ Real-world AI engineering

THIS IS NOT A DEMO CHATBOT.
THIS IS AN AI SYSTEM.

===========================================================
AUTHOR
===========================================================

Vishnu
Building agentic systems, not chatbots.

===========================================================
