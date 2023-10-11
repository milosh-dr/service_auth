# Testowanie się nie sprawdza

import requests
from requests.auth import HTTPBasicAuth

# Define your API endpoint and payload (if any)
url = 'http://localhost:5000/login'

# Define your username and password
username = 'milosh-dr@wp.pl'
password = 'D@nusia12'

response = requests.post(url, auth=HTTPBasicAuth(username, password))

# # Create a session with Basic Authentication
# with requests.Session() as session:
#     # Encode the credentials and add them to the request headers
#     session.auth = HTTPBasicAuth(username, password)

#     # Send a POST request with the headers and data
#     response = session.post(url)

# Check the response
if response.status_code == 200:
    print("Request was successful!")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
    print('-'*50)
    print(response.text)