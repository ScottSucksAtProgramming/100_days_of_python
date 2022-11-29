# ------------------------------ Resources ------------------------------ #
import requests

# ------------------------------ Class ------------------------------ #


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    GET_ENDPOINT = "https://api.sheety.co/6227c3c1e0cd34ee6217048ebad9bdae/cheapFlightFinder/prices"
    PUT_ENDPOINT = "https://api.sheety.co/6227c3c1e0cd34ee6217048ebad9bdae/cheapFlightFinder/prices/"
    sheet_id = None
    HEADER = {
        "Content-Type": "application/json",
    }

# ------------------------------ Functions ------------------------------ #
    def get_data(self):
        """Returns all data from Google Sheets into a dictionary"""
        response = requests.get(url=self.GET_ENDPOINT, headers=self.HEADER,)
        response.raise_for_status()
        sheet_data = response.json()
        #
        # sheet_data = {
        #     'prices': [
        #         {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 1000, 'id': 2},
        #         {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
        #         {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
        #         {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
        #         {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
        #         {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
        #         {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
        #         {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
        #         {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]}

        return sheet_data

    def update_sheet(self, data):
        """Updates the google sheet with passed in data."""
        for index in range(len(data['prices'])):
            city = data['prices'][index]['city']
            iata_code = data['prices'][index]['iataCode']
            lowest_price = data['prices'][index]['lowestPrice']
            payload = {
                'price': {
                    'city': city,
                    'iataCode': iata_code,
                    'lowestPrice': lowest_price,
                }
                       }
            endpoint = self.PUT_ENDPOINT + f"{data['prices'][index]['id']}"
            response = requests.put(url=endpoint, headers=self.HEADER, json=payload)
        return response

