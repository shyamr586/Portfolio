import requests
from .config import USERNAME,TOKEN

url = f"https://api.github.com/users/{USERNAME}/repos"        
headers = {"Accept":"application/vnd.github.mercy-preview+json"}        
REPOS = requests.get(url, headers=headers, auth=(USERNAME,TOKEN)).json()
