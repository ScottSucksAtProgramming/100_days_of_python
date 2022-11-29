# ------------------------------ Documentation ------------------------------ #
# Module:  CheapFlightFinder.py
# This program is the capstone for day 39 of #100 Days Of Code and will be used to search for cheap flights by
# tracking flight prices on a Google Sheet, comparing them to live flight prices from an API and then sending a
# message when a cheap flight is found.
#
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
#
# Modification History
# 09-04-2021 SK - Project Started.

# Things To Do
# Todone 1: Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air
#  Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you
#  want the city code (not the airport code see here).
#       Todone 1a: Get city names from Google Sheet.
#               - This should be done in the data_manager class.
#       Todone 1b: Compare names with entries from Flight Search API and get IATA Codes
#       Todone 1c: Save codes to google sheet.
#
# Todo 2: Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the
#  cities in the Google Sheet.
#
# Todo 3: If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number
#  with the Twilio API.
#
# Todo 4: The SMS should include the departure airport IATA code, destination airport IATA code, departure city,
#  destination city, flight price and flight dates. e.g.
#
# Todo 5: Add logic so it only checks for new iata codes if they are missing, and it only updates the sheet if a code
#  was found
# ------------------------------ Resources ------------------------------ #
import data_manager
import flight_search
import flight_data
# ------------------------------ Program Code ------------------------------ #
# First we pull the city name, iata code, and max price from the google sheet and save as variable.
data_manager = data_manager.DataManager()
cities_data = data_manager.get_data()


# Search for missing iata_codes in Flight Search API, add them to the cities_data variable.
flight_search = flight_search.FlightSearch()
cities_data = flight_search.get_iata_codes(data=cities_data)

# # Update missing IATA codes on the google sheet.
# response = data_manager.update_sheet(data=cities_data)

# Search for flights.
all_flights = flight_search.get_flights(cities_data)

# Save flights to dictionary.
flight_data = flight_data.FlightData()
cheap_flights = flight_data.get_flight_info(all_flights)

flight_data.format_message(cheap_flights)
