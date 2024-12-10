# from langchain.tools import tool
# import requests
# import json
# import os

# class SearchTools():
#     @tool("Search the web")
#     def search_internet(query):
#         """
#         Useful to search the internet about a given 
#         topic and return relevant results.
#         """
#         top_result_to_return = 5
#         url = "https://google.serper.dev/search"
#         payload = json.dumps({"q" : query})
#         headers = {
#             'X-API-Key': os.environ['SERPER_KEY'],
#             'content-type' : 'application/json'
#         }
#         response = requests.request("POST", url, headers = headers, data = payload)
#         # Check if there is an organic key
#         if 'organic' not in response.json():
#             return "Sorry, I couldn't find any relevant results."
#         else:
#             results = response.json()['organic']
#             string = []
#             for result in results[:top_result_to_return]:
#                 try:
#                     date = result.get('date','Date not available')
#                     string.append('\n'.join([
#                         f"Title: {result['title']}", 
#                         f"Link: {result['link']}",
#                         f"Date: {date}",
#                         f"Snippet: {result['snippet']}","\n-----------------"
#                     ]))
#                 except KeyError:
#                     next
#             return '\n'.join(string)

from langchain.tools import tool
import requests
import os
import warnings
warnings.filterwarnings("ignore")

class SearchTools():
    @tool("Search the web")
    def search_internet(query):
        """
        Useful to search the internet about a given 
        topic and return relevant results.
        """
        top_result_to_return = 5
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1&no_html=1"
        
        response = requests.get(url)
        
        # Check if the API returned a valid response
        if response.status_code != 200:
            return f"Error: Received status code {response.status_code} from DuckDuckGo."
        
        # Parse the response JSON
        try:
            results = response.json()
            related_topics = results.get('RelatedTopics', [])
            
            if not related_topics:
                return "Sorry, I couldn't find any relevant results."
            
            string = []
            for result in related_topics[:top_result_to_return]:
                if 'Text' in result and 'FirstURL' in result:
                    string.append('\n'.join([
                        f"Title: {result['Text']}",
                        f"Link: {result['FirstURL']}",
                        "\n-----------------"
                    ]))
            
            return '\n'.join(string) if string else "Sorry, I couldn't find any relevant results."
        
        except ValueError:
            return "Error: Unable to parse the response from DuckDuckGo."
