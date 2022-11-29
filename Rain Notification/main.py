# ----------------------- Resources -----------------------#
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os
# ----------------------- Constants -----------------------#
# OpenWeatherMap Info
URL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "120bb69764d7841c0c93614d77251aa6"
MY_LAT = 40.681129
MY_LONG = -73.469170
PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
    "units": "imperial"
}

# Twilio Constants
ACCOUNT_SID = "ACdacacc82fba19b16eff6728e586e50e4"
AUTH_TOKEN = "25549272e3fb5727ab55bf1d4ee79fc7"
PHONE_NUMBER = "+18507798572"
MY_NUMBER = "+15164450913"

# -----------------------  Weather API Call -----------------------#


def get_forecast(url, params):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


weather_data = get_forecast(URL, PARAMETERS)

gonna_rain = False
# Check for rain.
for hour in range(12):
    twelve_hour_forecast = weather_data['hourly'][hour]['weather'][0]['id']
    if twelve_hour_forecast < 700:
        gonna_rain = True

# -----------------------  Send SMS Message -----------------------#

if gonna_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)

    message = client.messages \
        .create(
             body="It's going to rain today. Bring an umbrella.",
             from_=PHONE_NUMBER,
             to=MY_NUMBER
         )

    print(message.sid)
