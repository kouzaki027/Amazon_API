from urllib.request import urlopen
import requests
import json

API_URL = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"
response = requests.get(API_URK)
shibaList = response.json()
shibaPictureURL = shibaList[0]

print(shibaPictureURL, "\n")
