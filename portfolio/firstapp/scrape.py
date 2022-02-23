import requests
# from .config import USERNAME,TOKEN
import os

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
url = f"https://api.github.com/users/{USERNAME}/repos"        
headers = {"Accept":"application/vnd.github.mercy-preview+json"}        
REPOS = requests.get(url, headers=headers, auth=(USERNAME,TOKEN)).json()
