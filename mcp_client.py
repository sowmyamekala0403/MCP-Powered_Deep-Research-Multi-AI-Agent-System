import requests

SERVICES = {
    "search": "https://mcp-powered-deep-research-multi-ai-agent-2bva.onrender.com/tool/search",
    "scrape": "https://mcp-powered-deep-research-multi-ai-agent-wx42.onrender.com/tool/scrape"
}

def call_tool(tool_name, payload):
    url = SERVICES[tool_name]

    try:
        response = requests.post(url, json=payload, timeout=30)
        return response.json()
    except Exception as e:
        return {
            "error": "Tool request failed",
            "details": str(e)
        }