# # App/wiki_search.py
# import requests

# def get_wikipedia_summary(query: str) -> str:
#     """
#     Fetch a summary from Wikipedia for the given query.
#     """
#     try:
#         # Wikipedia API endpoint
#         url = "https://en.wikipedia.org/w/api.php"
#         params = {
#             "action": "query",
#             "format": "json",
#             "prop": "extracts",
#             "exintro": True,
#             "explaintext": True,
#             "titles": query
#         }

#         response = requests.get(url, params=params)
#         data = response.json()

#         pages = data.get("query", {}).get("pages", {})
#         for page_id, page_data in pages.items():
#             if "extract" in page_data and page_data["extract"]:
#                 return page_data["extract"]

#         return "No relevant information found on Wikipedia."
#     except Exception as e:
#         return f"Error fetching from Wikipedia: {str(e)}"
