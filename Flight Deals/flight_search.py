# ------------------------------ Resources ------------------------------ #
import requests
import datetime as dt

# ------------------------------ Class ------------------------------ #


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    API_KEY = "CfsO89LuKHJ-7c0jWZ6noOTyteyO8KfJ"
    LOCATIONS_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
    FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
    HEADERS = {
        "content-type": "application/json; charset=utf-8",
        "apikey": API_KEY,
    }

    # ------------------------------ Functions ------------------------------ #

    def get_iata_codes(self, data):
        """Returns the data with missing iata_codes added."""
        for index in range(len(data['prices'])):
            if data['prices'][index]['iataCode'] == "":

                parameters = {
                    "term": data['price'][index]['city'],
                    "locale": "en-US",
                    "location_types": "city",
                    "limit": "1",

                }

                response = requests.get(url=self.LOCATIONS_ENDPOINT, params=parameters, headers=self.HEADERS)
                info = response.json()
                iata_code = info['locations'][0]['code']
                data['price'][index]['iataCode'] = iata_code
                print(f"IATA Code for {data['prices'][index]['city']} added.")
            else:
                print(f"IATA code for {data['prices'][index]['city']} already saved.")
        return data

    def get_flights(self, data):
        """Returns flight search data for all cities."""
        flights = []
        today = dt.datetime.today().date()
        end_date = today + dt.timedelta(weeks=24)
        home_city = "NYC"
        fly_to_list = ",".join([data['prices'][index]['iataCode'] for index in range(len(data['prices']))])
        for index in range(len(data['prices'])):
            parameters = {
                "fly_from": home_city,
                "fly_to": data['prices'][index]['iataCode'],
                "dateFrom": today.strftime("%d/%m/%Y"),
                "dateTo": end_date.strftime("%d/%m/%Y"),
                "one_for_city": 1,
                "curr": "USD",
                "flight_type": "round",
                "nights_in_dst_from": 2,
                "nights_in_dst_to": 14,
                "price_to": data['prices'][index]['lowestPrice'],
            }
            try:
                response = requests.get(url=self.FLIGHT_SEARCH_ENDPOINT, headers=self.HEADERS, params=parameters)
            except IndexError:
                pass
            else:
                response.raise_for_status()
                flights.append(response.json())
        return flights
