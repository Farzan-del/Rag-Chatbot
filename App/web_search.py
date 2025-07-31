# # App/web_search.py
# import requests

# def get_web_search_results(query: str) -> list:
#     """
#     Fetch search results from DuckDuckGo Instant Answer API.
#     Returns top snippets as a list for Gemini.
#     """
#     url = "https://api.duckduckgo.com/"
#     params = {
#         "q": query,
#         "format": "json",
#         "no_html": 1,
#         "skip_disambig": 1
#     }
#     try:
#         response = requests.get(url, params=params)
#         data = response.json()

#         snippets = []

#         # Primary answer from DuckDuckGo
#         if "AbstractText" in data and data["AbstractText"]:
#             snippets.append(data["AbstractText"])

#         # Related topics
#         if "RelatedTopics" in data:
#             for topic in data["RelatedTopics"]:
#                 if isinstance(topic, dict) and "Text" in topic:
#                     snippets.append(topic["Text"])
#                 elif "Topics" in topic:
#                     for sub_topic in topic["Topics"]:
#                         if "Text" in sub_topic:
#                             snippets.append(sub_topic["Text"])

#         # Ensure we have at least some content
#         if not snippets:
#             snippets.append("No relevant web results found.")

#         return snippets[:5]  # Limit to 5 results
#     except Exception as e:
#         return [f"Error fetching web results: {str(e)}"]

import requests
import os

# Google API Key and Search Engine ID (configure in environment or hardcode for now)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "Add_your_api_key_here")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID", "Your_search_engine_id_here")

def get_web_search_results(query: str, num_results: int = 5) -> list:
    """
    Fetch search results from Google Custom Search API.
    Returns top snippets as a list for Gemini.
    """
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query,
        "num": num_results
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()

        snippets = []
        for item in data.get("items", []):
            title = item.get("title", "")
            snippet = item.get("snippet", "")
            link = item.get("link", "")
            snippets.append(f"{title}: {snippet} (Source: {link})")

        # Ensure we have some content
        if not snippets:
            snippets.append("No relevant web results found.")

        return snippets[:num_results]
    except Exception as e:
        return [f"Error fetching web results: {str(e)}"]
