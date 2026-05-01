import requests

SERVICES = {
    "search": "http://localhost:8001/tool/search",
    "scrape": "http://localhost:8002/tool/scrape"
}

def call_tool(tool_name, payload):
    url = SERVICES.get(tool_name)

    if not url:
        raise ValueError(f"Unknown tool: {tool_name}")

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}