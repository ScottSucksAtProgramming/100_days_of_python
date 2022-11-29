# ------------------------------ Resources ------------------------------ #
import requests
import datetime
from twilio.rest import Client

# ------------------------------ Documentation ------------------------------ #
# Todone 1: When price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# Todone 2: Use https://newsapi.org Instead of printing ("Get News"), actually get the first 3 news pieces for the
# COMPANY_NAME.
# Todone 3: Use https://www.twilio.com Send a separate message with the percentage change and each article's title and
#  description to your phone number.

# ------------------------------ DateTime ------------------------------ #
# Use datetime to assign the dates we want into variables, date_yesterday and date_day_before.
date_yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
date_day_before = str(datetime.date.today() - datetime.timedelta(days=2))

# ------------------------------ Alphavantage Constants ------------------------------ #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = '30XPH9Z1N6IINOPT'
STOCK_URL = "https://www.alphavantage.co/query"

STOCK_PARAMETERS = {
    'function':     'TIME_SERIES_DAILY',
    'symbol':       STOCK,
    'datatype':     'json',
    'apikey':       STOCK_API_KEY
}

# ------------------------------ NewsAPI Constants ------------------------------ #
NEWS_API_KEY = "d3da76c2d7f041d2802ec14c052e6b46"
NEWS_URL = "http://newsapi.org/v2/everything"
NEWS_PARAMETERS = {
    "apiKey":       NEWS_API_KEY,
    "qInTitle":     COMPANY_NAME,
    "from":         date_yesterday,
}

# ------------------------------ Twilio Constants ------------------------------ #
ACCOUNT_SID = "ACdacacc82fba19b16eff6728e586e50e4"
AUTH_TOKEN = "25549272e3fb5727ab55bf1d4ee79fc7"
TWILIO_NUMBER = "+18507798572"
MY_NUMBER = "+15164450913"

# ------------------------------ Functions ------------------------------ #


def get_stock_data(url, parameters):
    """Returns stock data for the stock defined in parameters from Alphavantage API as json"""
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    return response.json()


def get_news(url, parameters,):
    """Returns the news for the COMPANY_NAME from NewsAPI.org as json"""
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    return response.json()


# ------------------------------ Parse Data ------------------------------ #
# First we get the stock data via API and store it in the variable STOCK_DATA.
stock_data = get_stock_data(url=STOCK_URL, parameters=STOCK_PARAMETERS)

# Now we can pull apart the stock data and get the specific prices we need.
day_before_price = round(float(stock_data['Time Series (Daily)'][date_day_before]['4. close']), 2)
yesterday_price = round(float(stock_data['Time Series (Daily)'][date_yesterday]['4. close']), 2)
difference = round(day_before_price - yesterday_price, 2)
percent_change = round((difference / day_before_price) * 100, 2)


# We only care about a change of 5% or more. So we write us an if statement to see if that's true.
send_message = False
news = []
if percent_change >= 5 or percent_change <= -5:
    # Print out the numbers for reference.
    print(f"{date_day_before} Closing Price: S{day_before_price}")
    print(f"{date_yesterday} Closing Price: ${yesterday_price}")
    print(f"With a difference of ${difference} or {percent_change}%")

    news_data = get_news(url=NEWS_URL, parameters=NEWS_PARAMETERS)

    # Lets start pulling out the information we want in our text messages.

    send_message = True
    try:
        for num in range(3):
            headline = f"Headline: {news_data['articles'][num]['title']}"
            brief = f"Brief: {news_data['articles'][num]['content'][:200]}\n"
            news.append(headline)
            news.append(brief)
    except IndexError:
        pass

# ------------------------------ Format Message ------------------------------ #
if percent_change > 0:
    delta = f"🔺 {percent_change}%"
else:
    delta = f"🔻 {percent_change}%"

msg = " \n".join(news)

# ------------------------------ Send Message ------------------------------ #
if send_message:
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"TSLA: {delta}\n\n{msg}",
                         from_=TWILIO_NUMBER,
                         to=MY_NUMBER
                     )

    print(message.sid)
else:
    pass
