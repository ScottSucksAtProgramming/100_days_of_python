# ----------------------- Resources -----------------------#
import requests
import smtplib
# ----------------------- Documentation -----------------------#
# Job request on Upwork.com for a daily e-mail that contains a 7-Day Weather Forecast for seven different locations.
# This sounds pretty straight forward. I've already got an OWM API account set up.
# Requested data - High Temp; Low Temp; Humidity: Condition id;
# Todo 1: Pull weather data.
# Todo 2: Format weather data.
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
    "exclude": "current,minutely,hourly,alerts",
    "units": "imperial"
}

# List of Locations w/ Data
LOCATIONS = [
    {
        'Name': "Orlando, FL",
        'Postal': "32821",
        'Parameters':
        {
            "lat": 28.538336,
            "lon": -81.379234,
            "appid": API_KEY,
            "exclude": "current,minutely,hourly,alerts",
            "units": "imperial"
        }

    },
    {
        'Name': "Tampa, Fl",
        'Postal': "33612",
        'Parameters':
        {
            "lat": 27.950575,
            "lon": -82.457176,
            "appid": API_KEY,
            "exclude": "current,minutely,hourly,alerts",
            "units": "imperial"
        }

    },
    {
        'Name': "San Diego, CA",
        'Postal': "92109",
        'Parameters':
        {
            "lat": 32.715736,
            "lon": -117.161087,
            "appid": API_KEY,
            "exclude": "current,minutely,hourly,alerts",
            "units": "imperial"
        }

    },
    {
        'Name': "Chula Vista, CA",
        'Postal': "91911",
        'Parameters':
        {
            "lat": 32.640072,
            "lon": -117.084038,
            "appid": API_KEY,
            "exclude": "current,minutely,hourly,alerts",
            "units": "imperial"
        }

    },
    {
        'Name': "Williamsburg, VA",
        'Postal': "23187",
        'Parameters':
        {
            "lat": 37.275558,
            "lon": -76.709023,
            "appid": API_KEY,
            "exclude": "current,minutely,hourly,alerts",
            "units": "imperial"
        }

    },
    {
        'Name': "Langhorne, PA",
        'Postal': "19047",
        'Parameters':
        {
            "lat": 40.176769,
            "lon": -74.917007,
            "appid": API_KEY,
            "exclude": "current,minutely,hourly,alerts",
            "units": "imperial"
        }

    },
    {
        'Name': "San Antonio, TX",
        'Postal': "78251",
        'Parameters':
            {
                "lat": 29.424122,
                "lon": -98.493629,
                "appid": API_KEY,
                "exclude": "current,minutely,hourly,alerts",
                "units": "imperial"
            }

    },

]

# E-Mail Constants
my_email = "sktest1025@gmail.com"
my_password = "heyyouguys"

weather_report = []
# -----------------------  Functions -----------------------#


def get_forecast(url, params):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


# -----------------------  Weather API Call -----------------------#

for loc in range(len(LOCATIONS)):
    weather_data = get_forecast(URL, LOCATIONS[loc]['Parameters'])

    # Getting the weather specifics that we want.
    loc_info = f"\n7-Day Forecast for {LOCATIONS[loc]['Name']}"
    weather_report.append(loc_info)
    for day in range(7):
        high_temp = '{:.1f}'.format(round(weather_data['daily'][day]["temp"]['max'], 1))
        low_temp = '{:.1f}'.format(round(weather_data['daily'][day]["temp"]['min'], 1))
        humidity = weather_data['daily'][day]['humidity']
        condition = weather_data['daily'][day]['weather'][0]['description'].title()
        if day == 0:
            readable_day = "Today"
        else:
            readable_day = f"Day {day + 1}"
        daily_forecast = (f"{readable_day}:    High Temp: {high_temp}F    Low Temp: {low_temp}F    "
                          f"Humidity: {humidity}%    Weather Condition: {condition}.")
        weather_report.append(daily_forecast)
#
# for _ in range(len(weather_report)):
#     print(weather_report[_])

x = "\n".join(str(weather_report[_]) for _ in range(len(weather_report)))

# -----------------------  Send E-mail -----------------------#
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()  # Ensures a secure connection.
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="scottkostolni@gmail.com",
        msg=f"Subject: Here's Your Weather Report.\n\n{x}")