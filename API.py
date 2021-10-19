import requests
query1 = 'number'
response = requests.get("http://api.open-notify.org/astros.json", params=query1)
print(response)
print(response.text)


print(response.json())

#query = {'lat':'45', 'lon':'180'}
#response1 = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
#print(response1.json())
