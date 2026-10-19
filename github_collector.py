import requests

def search_requests(query):

     params = {"q" : query , "per_page": 5}
     response = requests.get("https://api.github.com/search/repositories",params=params , timeout=10)

     response.raise_for_status()
     data = response.json()

     for item in data["items"]:
          return data["items"]
       

   
