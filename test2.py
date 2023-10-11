import requests

req = requests.get('http://localhost:5000/test_route')

print(req.status_code)
print(req.text)