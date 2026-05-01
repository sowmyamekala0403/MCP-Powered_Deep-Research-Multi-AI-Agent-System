# MCP-Powered_Deep-Research-Multi-AI-Agent-System  
# MCP-Powered Deep Research AI Agent

This project is an AI-based research assistant that can search the web, extract useful content, and generate a summarized answer for a given query.

The main idea behind this project is to simulate how real-world AI agents work by breaking tasks into smaller services instead of doing everything in one place.

---

## 🔍 What this project does

- Takes a user query from UI  
- Searches the web for relevant results  
- Extracts meaningful content from web pages  
- Generates a summarized answer using an LLM  

---

## 🧠 How I built it

Initially, I built this project as a **single service (without MCP)** where everything was handled in one file:
- search
- scraping
- summarization  

### Problem with that approach:
It worked, but:
- code was tightly coupled  
- hard to debug  
- not scalable  

---

## 🔧 Current Approach (MCP style)

I redesigned the system into **separate services**:

- `search_service.py` → handles web search  
- `scrape_service.py` → extracts webpage content  
- `agent_service.py` → coordinates everything  

So now the flow is:

User → Agent → Search → Scrape → LLM → Response  

### Why this is better:
- easier to maintain  
- services can be reused  
- follows real-world architecture  

---

## 🛠 Tech used

- Python  
- FastAPI  
- Requests, BeautifulSoup  
- Tavily API (for search)  
- Groq (for LLM)  
- HTML, CSS, JavaScript  

---

## 📁 Project structure
agent_service.py
search_service.py
scrape_service.py
mcp_client.py
index.html
requirements.txt


---

## ⚙️ How to run this project

### 1. Clone the repo

```bash
git clone https://github.com/sowmyamekala0403/MCP-Powered_Deep-Research-Multi-AI-Agent-System.git
cd MCP-Powered_Deep-Research-Multi-AI-Agent-System
2. Create virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Add environment variables

Create a .env file:

GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
▶️ Running the project

Open 3 terminals:

Terminal 1
uvicorn search_service:app --port 8001 --reload
Terminal 2
uvicorn scrape_service:app --port 8002 --reload
Terminal 3
uvicorn agent_service:app --port 8003 --reload
Start frontend
python -m http.server 5500

Open in browser:

http://localhost:5500
💡 What I learned
How to design systems using microservices
How real AI agents use tools
Difference between monolithic vs modular systems
Handling APIs and integrating LLMs
🚀 Future improvements
Better UI (chat style)
Streaming responses
More tools (PDF, DB search, etc.)
Deployment
👩‍💻 Author

Sowmya Mekala


---

# 🔥 Why this is better

- Sounds like **you actually built it**
- Shows **learning journey**
- Explains **before vs after (very important in interviews)**

---

# 🔷 Next step

Now run:

```bash
git add README.md
git commit -m "docs: added project README"
git push