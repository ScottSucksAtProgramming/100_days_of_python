# import smtplib
#
#
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()  # Ensures a secure connection.
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="scottkostolni@gmail.com",
#         msg="Subject: Hello, Scott\n\nHey fucker!!")

# Pick a random quote from the list of quotes, and then save it to a variable.
import random
with open("quotes.txt", mode="r") as file:
    today_quote = random.choice(file.readlines())

import datetime as dt
import smtplib as sl
# How to send a basic E-mail with smtplib.
my_email = "sktest1025@gmail.com"
my_password = "heyyouguys"
# set current datetime to today.
now = dt.datetime.now()
weekday = now.weekday()
# Week starts at 0, Today is Wednesday, so that would be 2. Lets test to see if current day is wednesday.
if weekday == 0:
    with sl.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ScottKostolni@gmail.com",
                            msg=f"Subject:Weekly Motivational Quote from Scott's Python Script\n\n {today_quote}.")






# # get the current time
# now = dt.datetime.now()
# print(now)
#
# # get part of the time string
# year = now.year
# print(year)
#
# # Create a date time object
# date_of_birth = dt.datetime(year=1986, month=1, day=2,)
# print(date_of_birth)