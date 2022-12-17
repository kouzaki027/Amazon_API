from urllib.request import urlopen
import requests
import json

url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/TESLA?format=json"
"""
try:
    response = requests.get('https://httpbin.org/get')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
"""
response = requests.get(url)
jsondata = response.json()

#print(json.dumps(jsondata, indent = 2,))
#print ( type(jsondata))
# what data structure are we working with

#print("Count: ", jsondata[ 'Count'])
# total count of results

#print("searchcriteria: ", jsondata[ 'SearchCriteria'])
# what was passed intot he rest api query

#print("results: ", jsondata[ 'Results'])
# echo the whole results dictionary out;

#print(jsondata["Results"][0]['Make_ID'])
# grab the first one just as a test ; in this case 441 is the make_id

# OK, so enumerate through the whole results set
# Find dictionary matching value in list
# brute force loop

'''
First Option:
'''
print ("First approach to scrap data:")
res = None
for x in jsondata["Results"]:
  print("  ", x)
  if (  x["Model_Name"] ==  "Model 3"  ):
      res = x
      print ( "Wohoo! We found MODEL 3 = model id", x["Model_ID"] )
      break

print ("Wohoo! We deduced that MODEL 3 = ", str(res)  )
print("")

'''
Second Option: In this method, we are simply using a function and passing the name we want to search and the test_list and with the help of list comprehension, we return>
'''
print ("Second approach to scrap data:")
def search(name, test_list ):
    return [element for element in test_list if element['Model_Name'] == name]
res = search("Model 3", jsondata["Results"])
print(res)
print()

"""
aaaaaaaa
<class 'dict'>
Count:  6
searchcriteria:  Make:TESLA
results:  [{'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 1685, 'Model_Name': 'Model S'}, {'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 2071, 'Model_Name': 'Roadster'}, {'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 10199, 'Model_Name': 'Model X'}, {'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 17834, 'Model_Name': 'Model 3'}, {'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 27027, 'Model_Name': 'Model Y'}, {'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 30834, 'Model_Name': 'Semi'}]
441
{'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 1685, 'Model_Name': 'Model S'}
Model S
{'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 2071, 'Model_Name': 'Roadster'}
Roadster
{'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 10199, 'Model_Name': 'Model X'}
Model X
{'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 17834, 'Model_Name': 'Model 3'}
Model 3
{'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 27027, 'Model_Name': 'Model Y'}
Model Y
{'Make_ID': 441, 'Make_Name': 'TESLA', 'Model_ID': 30834, 'Model_Name': 'Semi'}
Semi
"""
"""
{
  "Count": 6,
  "Message": "Response returned successfully",
  "SearchCriteria": "Make:TESLA",
  "Results": [
    {
      "Make_ID": 441,
      "Make_Name": "TESLA",
      "Model_ID": 1685,
      "Model_Name": "Model S"
    },
    {
      "Make_ID": 441,
      "Make_Name": "TESLA",
      "Model_ID": 2071,
      "Model_Name": "Roadster"
    },
    {
      "Make_ID": 441,
      "Make_Name": "TESLA",
      "Model_ID": 10199,
      "Model_Name": "Model X"
    },
    {
      "Make_ID": 441,
      "Make_Name": "TESLA",
      "Model_ID": 17834,
      "Model_Name": "Model 3"
    },
    {
      "Make_ID": 441,
      "Make_Name": "TESLA",
      "Model_ID": 27027,
      "Model_Name": "Model Y"
    },
    {
      "Make_ID": 441,
      "Make_Name": "TESLA",
      "Model_ID": 30834,
      "Model_Name": "Semi"
    }
  ]
}
"""
