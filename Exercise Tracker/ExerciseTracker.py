# ------------------------------ Documentation ------------------------------ #
# Module:  ExerciseTracker.py
# DESCRIPTION
#       This program uses a Natural Language Processing AI to track exercises and store them in a Google Sheet. It
#       will take the
#
# Modification History
# 09022021 SK
#       App Creation
#

# ------------------------------ Resources ------------------------------ #
import requests
import datetime as dt
# ------------------------------ Constants ------------------------------ #
#NutritionIX
NUTRITIONIX_APP_ID = "8cafb4f7"
NUTRITIONIX_API_KEY = "d4bc1d044e9caaf80f07bed3f9ef003f"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

NUTRITIONIX_HEADER = {
    "x-app-id":     NUTRITIONIX_APP_ID,
    "x-app-key":    NUTRITIONIX_API_KEY,
    "x-remote-user-id": '0'
}

# Sheety
# Retrieve rows from your sheet
SHEETY_GET_ENDPOINT = "https://api.sheety.co/6227c3c1e0cd34ee6217048ebad9bdae/workoutTracking/workouts"

# Add a row to your sheet
SHEETY_POST_ENDPOINT = "https://api.sheety.co/6227c3c1e0cd34ee6217048ebad9bdae/workoutTracking/workouts"

SHEETY_HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer asdf1234sadl;kj"
}

# ------------------------------ Functions ------------------------------ #


def get_exercise_data(url, headers, data):
    response = requests.post(url=url, headers=headers, data=data)
    response.raise_for_status()
    data = response.json()
    return data


# ------------------------------ Program ------------------------------ #
user_input = input("Tell me what exercises you did: ")

query = {
    "query": user_input,
}


exercise_data = get_exercise_data(url=NUTRITIONIX_ENDPOINT, headers=NUTRITIONIX_HEADER, data=query)

date = dt.date.today()
time = dt.time.now()

for index in range(len(exercise_data)):
    exercise = exercise_data['exercises'][index]['name'].title()
    duration = exercise_data['exercises'][index]['duration_min']
    calories = exercise_data['exercises'][index]['nf_calories']

print(date)
print(time)
# SHEETY_INPUT = {
#     "workout": {
#         "date": "21/07/2020",
#         "time": "15:00:00",
#         "exercise": "Running",
#         "duration": 22,
#         "calories": 130,
#         "id": 2
#     }
# }
#
# response = requests.post(url=SHEETY_POST_ENDPOINT, headers=SHEETY_HEADER, json=SHEETY_INPUT)
# print(response.text)

