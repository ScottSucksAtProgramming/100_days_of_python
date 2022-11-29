# ------------------------------ Resources ------------------------------ #
import requests
import datetime
# ------------------------------ Documentation ------------------------------ #
# Module:  HabitTracker.py
# This project will track a habit using the Pixela API.
#
#
# Modification History
#

# ------------------------------ Pixela Constants ------------------------------ #

PIXELA_ENDPOINT = "https://pixe.la"
PIXELA_TOKEN = "haen20210829"
PIXELA_USERNAME = "sktest1025"
GRAPH_ID = "sktestmedgraph"

USER_PARAMS = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes",
}

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/v1/users/{PIXELA_USERNAME}/graphs"
GRAPH_CONFIG = {
    "id":       GRAPH_ID,
    "name":     "Meditation Habit",
    "unit":     "Minutes",
    "type":     "int",
    "color":    "sora",
}

HEADER = {
    'X-USER-TOKEN': PIXELA_TOKEN,
}
TODAY = datetime.datetime.today().strftime("%Y%m%d")

ADD_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"
ADD_PIXEL_PARAMS = {
    "date":     TODAY,
    "quantity": "5",
}
DATE = TODAY
QTY = "15"
UPDATE_PIXEL_ENDPOINT = f"{ADD_PIXEL_ENDPOINT}/{TODAY}"
UPDATE_PIXEL_PARAMS = {
    "quantity": QTY,
}
# ------------------------------ Account Creation ------------------------------ #
# This has been completed and does not need to be run again unless creating a new account.
# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
# print(response)
# print(response.text)
# My Graph: https://pixe.la/@sktest1025

# ------------------------------ Graph Creation------------------------------ #
# This has also been completed and doesn't need to be done again unless creating a new graph.
# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADER)
# print(response.text)

# ------------------------------ Create a Pixel ------------------------------ #

# response = requests.post(url=ADD_PIXEL_ENDPOINT, json=ADD_PIXEL_PARAMS, headers=HEADER)
# print(response)
# print(response.text)

# ------------------------------ Update a Pixel ------------------------------ #
response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=UPDATE_PIXEL_PARAMS, headers=HEADER)
print(response.text)