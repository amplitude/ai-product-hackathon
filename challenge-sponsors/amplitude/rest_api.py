import os

import requests

# store your amplitude api + secret keys in environment variables
# find keys on your project's page (fill in your org-url): https://analytics.amplitude.com/<org-url>/settings/projects
api_key = os.environ['AMPLITUDE_API_KEY']
secret_key = os.environ['AMPLITUDE_SECRET_KEY']

# fetch active users over two months
endpoint = 'https://amplitude.com/api/2/users?start=20230501&end=20230630'
response = requests.get(endpoint, auth=(api_key, secret_key))
print(response.json())
