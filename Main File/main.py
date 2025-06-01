import requests
import datetime
from newsapi import NewsApiClient
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))
NEWS_PARAMS = {"q": COMPANY_NAME, "language": "en"}



alphavantage_response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHAVANTAGE_API_KEY}').json()

yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
day_before_yesterday = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime('%Y-%m-%d')

yesterday_close = alphavantage_response["Time Series (Daily)"][yesterday]["4. close"]
day_before_yesterday_close = alphavantage_response["Time Series (Daily)"][day_before_yesterday]["4. close"]

stock_change = int(((float(yesterday_close) - float(day_before_yesterday_close)) / float(day_before_yesterday_close)) * 100)
print(stock_change)
if stock_change > 5:
    get_news()
elif stock_change < -5:
    get_news()



def get_news():
    news_response = NEWS_API_KEY.get_everything(**NEWS_PARAMS)
    news_1 = news_response["articles"][0]
    news_2 = news_response["articles"][1]
    news_3 = news_response["articles"][2]
    news_1_title = news_1["title"]
    news_1_description = news_1["description"]
    news_1_content = news_1["content"]
    news_2_title = news_2["title"]
    news_2_description = news_2["description"]
    news_2_content = news_2["content"]
    news_3_title = news_3["title"]
    news_3_description = news_3["description"]
    news_3_content = news_3["content"]
    if stock_change > 5:
        return f"TSLA: 🔺{stock_change}%\n\n" \
            f"1st News\n 1)Headline: {news_1_title}\n2) Description: {news_1_description}\n3)Content: {news_1_content}\n\n" \
            f"2nd News\n 1)Headline: {news_2_title}\n2)Description: {news_2_description}\n3)Content: {news_2_content}\n\n" \
            f"3rd News\n 1)Headline: {news_3_title}\n2)Description: {news_3_description}\n3)Content: {news_3_content}\n\n"
    elif stock_change < -5:
        return f"TSLA: 🔻{stock_change}%\n\n" \
            f"1st News\n 1)Headline: {news_1_title}\n2) Description: {news_1_description}\n3)Content: {news_1_content}\n\n" \
            f"2nd News\n 1)Headline: {news_2_title}\n2)Description: {news_2_description}\n3)Content: {news_2_content}\n\n" \
            f"3rd News\n 1)Headline: {news_3_title}\n2)Description: {news_3_description}\n3)Content: {news_3_content}\n\n"
    else:
        return "No news"

def send_news_via_whatsapp():
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',  
        body=get_news(),                
        to='whatsapp:+917710910842'     
    )

    print("Message SID:", message.sid)
send_news_via_whatsapp()