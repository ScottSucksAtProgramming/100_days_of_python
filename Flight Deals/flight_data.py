# ------------------------------ Resources ------------------------------ #
import datetime as dt
import notification_manager
# ------------------------------ Class ------------------------------ #


class FlightData:
    cheap_flights = []
    # This class is responsible for structuring the flight data.
    pass

# ------------------------------ Functions ------------------------------ #
    def get_flight_info(self, flight_data):
        """Returns cheap flight info in dictionary."""
        for index in range(len(flight_data)):
            try:
                fly_from = flight_data[index]['data'][0]['flyFrom']
                city_from = flight_data[index]['data'][0]['cityFrom']
                fly_to = flight_data[index]['data'][0]['flyTo']
                city_to = flight_data[index]['data'][0]['cityTo']
                price = int(flight_data[index]['data'][0]['price'])
                length = flight_data[index]['data'][0]['nightsInDest']
                departure_str = flight_data[index]['data'][0]['local_departure'].split('T')[0]
                departure_format = dt.datetime.strptime(departure_str, "%Y-%m-%d")
                return_date = (departure_format + dt.timedelta(days=length)).strftime('%m/%d/%Y')
                departure_date = departure_format.date().strftime('%m/%d/%Y')

                flight = {'fly_from': fly_from, 'city_from': city_from, 'fly_to': fly_to, 'city_to': city_to,
                          'price': price, 'departure_date': departure_date, "return_date": return_date}
                self.cheap_flights.append(flight)
            except IndexError:
                pass
        return self.cheap_flights

    def format_message(self, cheap_flight_data):
        for index in range(len(cheap_flight_data)):
            message = f"Fly from {cheap_flight_data[index]['city_from']}-{cheap_flight_data[index]['fly_from']} to " \
                      f"{cheap_flight_data[index]['city_to']}-{cheap_flight_data[index]['fly_to']}, " \
                      f"{cheap_flight_data[index]['departure_date']} to {cheap_flight_data[index]['return_date']} " \
                      f"for ${cheap_flight_data[index]['price']}."
            print(message)
            # notifier = notification_manager.NotificationManager()
            # notifier.send_message(message)
