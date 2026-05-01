from fastapi import FastAPI
from mcp_client import call_tool
from openai import OpenAI
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
load_dotenv()

app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/agent/query")
def agent(data: dict):
    query = data["query"]

    # Step 1: Search
    search_result = call_tool("search", {"query": query})

    if "results" not in search_result:
        return {"error": "Search failed"}

    contents = []

    # Step 2: Scrape top 3 links
    for r in search_result["results"][:3]:
        scrape = call_tool("scrape", {"url": r["url"]})
        if "content" in scrape:
            contents.append(scrape["content"])

    combined_text = "\n\n".join(contents)

    # Step 3: Summarize using LLM
    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "You are a research assistant. Summarize clearly and concisely."
        },
        {
            "role": "user",
            "content": f"Summarize this:\n{combined_text[:8000]}"
        }
    ]
)
    summary = response.choices[0].message.content

    return {
        "summary": summary,
        "sources": [r["url"] for r in search_result["results"][:3]]
    }