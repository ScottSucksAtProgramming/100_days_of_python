# ------------------------------- Resources ------------------------------- #
import requests
import datetime
import smtplib
import time
# ------------------------------- Constants ------------------------------- #


MY_LAT = 40.681129
MY_LONG = -73.469170
MY_EMAIL = "sktest1025@gmail.com"
MY_PASSWORD = "heyyouguys"


# ------------------------------- Functions ------------------------------- #


def iss_close(lat, long):
    """Returns 'True' if the ISS is close to home latitude and longitude."""
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    iss_latitude = float(iss_data['iss_position']['latitude'])
    iss_longitude = float(iss_data['iss_position']['longitude'])

    if (lat - 5) < iss_latitude < (lat + 5) and (long - 5) < iss_longitude < (long + 5):
        return True
    else:
        return False


def is_night():
    """Returns 'True' if current time is between sunset and sunrise"""
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunrise_hour = int(sunrise.split('T')[1].split(":")[0])
    sunset_hour = int(sunset.split('T')[1].split(":")[0])
    time_now = datetime.datetime.now()

    if sunrise_hour < int(time_now.hour) > sunset_hour:
        return True
    else:
        return False


def send_message():
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Ensures a secure connection.
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="scottkostolni@gmail.com",
                msg="Subject: The ISS Appears\n\nYou can view the ISS in the night sky!!")
    except smtplib.SMTPResponseException as e:
        log_entry = f"{datetime.datetime.now()} - There was an error sending the message."
        print(log_entry)
        error_code = e.smtp_code
        error_message = e.smtp_error
        full_error = f"Error Code: {error_code}. Error Message: {error_message}"
        print(full_error)
        with open("./log.txt", mode="a") as log:
            log.write(f"{log_entry}\n{full_error}\n\n")
        pass
    else:
        log_entry = f"{datetime.datetime.now()} - E-mail Sent."
        print(log_entry)
        with open("./log.txt", mode="a") as log:
            log.write(f"{log_entry}\n\n")


# ------------------------------- Program Code ------------------------------- #
while True:
    if iss_close(lat=MY_LAT, long=MY_LONG):
        if is_night():
            log_entry = f"{datetime.datetime.now()} - The time is right, sending e-mail."
            print(log_entry)
            with open("./log.txt", mode="a") as log:
                log.write(f"{log_entry}\n\n")
            send_message()
        else:
            log_entry = f"{datetime.datetime.now()} - It is not the right time."
            print(log_entry)
            with open("./log.txt", mode="a") as log:
                log.write(f"{log_entry}\n\n")

    else:
        log_entry = f"{datetime.datetime.now()} - The ISS is not close."
        print(log_entry)
        with open("./log.txt", mode="a") as log:
            log.write(f"{log_entry}\n\n")
    time.sleep(60)

