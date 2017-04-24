import requests

url = "https://api.ciscospark.com/v1/rooms"

headers = {
    'authorization': "Bearer <API_TOKEN>",
    'content-type': "application/json",
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
