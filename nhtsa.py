from urllib.request import urlopen
import requests
import json


'''
First option:
'''
url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/TESLA?format=json"
response = requests.get(url)
jsondata = response.json()
#print(json.dumps(jsondata, indent = 2,))
print("\n*******************" * 2)
"""
Dictionaries map keys to values and store them in an array or collection.
The keys must be of a hashable type, which means that they must have a hash value that never changes during the key’s lifetime.
"""
# Get the JSON response and store it as a Python dict
my_dictionary = requests.get(url).json()
print("Tesla Models:\n", json.dumps(my_dictionary, indent=2))


'''
Second Option: caution prints at least 200 lines
url ="https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"
response = requests.get(url)
jsondata = response.json()
# Get the JSON response and store it as a Python dict
my_dictionary = requests.get(url).json()
print("All Makes:\n", json.dumps(my_dictionary, indent=2))
