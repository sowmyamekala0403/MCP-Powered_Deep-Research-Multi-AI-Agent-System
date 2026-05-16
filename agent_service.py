from fastapi import FastAPI
from mcp_client import call_tool
from groq import Groq
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# CORS for frontend/UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Groq LLM client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# MCP Services 
SERVICES = {
    "search": "https://search-service.onrender.com/tool/search",
    "scrape": "https://scrape-service.onrender.com/tool/scrape"
}


@app.post("/agent/query")
def agent(data: dict):
    try:
        query = data["query"]

        # 🔷 STEP 1: SEARCH
        search_result = call_tool("search", {"query": query})

        if not search_result or "results" not in search_result:
            return {
                "error": "Search failed",
                "debug": search_result
            }

        contents = []

        # 🔷 STEP 2: SCRAPE TOP LINKS
        for r in search_result["results"][:3]:
            url = r.get("url")

            if not url:
                continue

            scrape = call_tool("scrape", {"url": url})

            if scrape and "content" in scrape:
                contents.append(scrape["content"])

        combined_text = "\n\n".join(contents)

        if not combined_text.strip():
            return {"error": "No content scraped from URLs"}

        # 🔷 STEP 3: LLM SUMMARIZATION
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a research assistant. Summarize clearly, structured and concise."
                },
                {
                    "role": "user",
                    "content": f"Summarize the following research:\n{combined_text[:8000]}"
                }
            ]
        )

        summary = response.choices[0].message.content

        # 🔷 FINAL OUTPUT
        return {
            "query": query,
            "summary": summary,
            "sources": [r["url"] for r in search_result["results"][:3]]
        }

    except Exception as e:
        return {
            "error": "Agent failed",
            "details": str(e)
        }
