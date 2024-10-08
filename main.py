import requests
from datetime import datetime

USERNAME = USR # your own username
TOKEN = TKN # your own token
GRAPH_ID = "graph1"

# Create user
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Test Graph",
    "unit": "min",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# resp = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(resp.text)

# Create a pixel
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "30"
}

# resp = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

# Update a pixel
update_endpoint = f"{pixel_endpoint}/{today.strftime("%Y%m%d")}"

new_data = {
    "quantity": "60"
}

# resp = requests.put(url=update_endpoint, json=new_data, headers=headers)
# print(resp.text)

# Delete a pixel
delete_endpoint = update_endpoint

resp = requests.delete(url=delete_endpoint, headers=headers)
print(resp.text)