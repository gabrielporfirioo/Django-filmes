import requests
from dotenv import load_dotenv
import os

load_dotenv(override=True)

def get_movie_from_omdb(title):
  
    url = f"http://www.omdbapi.com/?t={title}&apikey={os.getenv('API_KEY')}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            return {
                'title': data['Title'],
                'year': data['Year'],
                'plot': data['Plot'],
                'poster': data['Poster']
            }
        else:
            return None  
    return None  
