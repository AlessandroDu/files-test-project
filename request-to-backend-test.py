import requests
response = requests.get('http://localhost:8000/api/files/1')
print(response.json())