# test_mcp.py

from mcp_client import call_tool

# Step 1: search
search_result = call_tool("search", {"query": "latest AI news"})
print(search_result)

# Step 2: scrape first result
if "results" in search_result and len(search_result["results"]) > 0:
    first_url = search_result["results"][0]["url"]

    scrape_result = call_tool("scrape", {"url": first_url})
    print(scrape_result)