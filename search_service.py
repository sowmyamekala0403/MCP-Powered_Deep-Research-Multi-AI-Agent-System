from fastapi import FastAPI
from tavily import TavilyClient
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@app.post("/tool/search")
def search(data: str):
    query = data["query"]

    results = tavily.search(query=query, max_results=5)
    return {
        "results": [
            {
                "title": r["title"],
                "url": r["url"],
                "snippet": r["content"][:300]
            }
            for r in results["results"]
        ]
    }