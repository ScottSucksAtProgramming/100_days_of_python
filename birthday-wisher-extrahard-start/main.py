# ------------------------------- Resources ------------------------------- #
import datetime

import pandas as pd
import datetime as dt
import random as rd
import smtplib as smtp
# ------------------------------- Todos ------------------------------- #

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

# Todo 1: Load birthdays.csv into a data frame. - DONE
# Todo 2: Translate birthdays in csv to date time. - DONE
# Todo 3: Compare birthdays with current date and save name and e-mail address to a list. - DONE
# Todo 4: Go through recipients list and create a variable with a random birthday letter.-
# Todo 5: Text replace the [Name] to the name from the recipients list. Then save the new letter as a variable,
#  with all formatting.

# ------------------------------- Constants ------------------------------- #
ID = 0
MY_EMAIL = "sktest1025@gmail.com"
MY_PASSWORD = "heyyouguys"

# ------------------------------- Functions ------------------------------- #


def send_email(person, to_email, message):
    with smtp.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_email,
            msg=f"Subject: Happy Birthday {person},\n\n{message}")


# ------------------------------- Preparation ------------------------------- #

# Lets load up the birthday list into something usable.
df = pd.read_csv("birthdays.csv")

# Gets today's date and saves it to variable.
today = dt.date.today()

# Initialize the dictionary that's going to hold the recipients of our birthday e-mails.
recipients = []
persons = []


# ------------------------------- Find Recipients ------------------------------- #
# Loop through each row in the data frame.
for (index, row) in df.iterrows():

    # Creates a datetime object from the birthday of each person in the csv file.
    day = df["day"][index]
    month = df["month"][index]
    year = df["year"][index]
    birth_date = datetime.date(day=day, month=month, year=year)

    # Compare the person's birthday with today's date. If it's a match, add that person name and e-mail
    # to the recipients list.
    if birth_date.day == today.day and birth_date.month == today.month:
        persons = row['name'], row['email']
    recipients.append(persons)

    if len(recipients) == 0:
        print("No birthdays today.")


# ------------------------------- Build Letters ------------------------------- #
# I want to come back and try populate this list by reading the file names from the directory.
letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter = rd.choice(letter_list)

# Load up letter text.
blank_letter = open(f"./letter_templates/{letter}", "r").read()

# Loop Number 2!

for index in range(len(recipients)):
    name = recipients[index][0]
    email = recipients[index][1]
    finished_letter = blank_letter.replace("[NAME]", name)
    send_email(person=name, to_email=email, message=finished_letter)
