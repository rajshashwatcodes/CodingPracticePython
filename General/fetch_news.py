import requests
import json

API_KEY = 'YOUR_NEWSAPI_KEY'  # Replace with your actual NewsAPI key
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'
COUNTRY = 'us'  # Change to your preferred country code

def fetch_news(api_key, country):
    params = {
        'apiKey': api_key,
        'country': country
    }
    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return None

def display_headlines(news_data):
    if news_data and 'articles' in news_data:
        print(f"Top headlines from {COUNTRY.upper()}:")
        for i, article in enumerate(news_data['articles'], start=1):
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   URL: {article['url']}\n")
    else:
        print("No news data available.")

if __name__ == '__main__':
    news_data = fetch_news(API_KEY, COUNTRY)
    display_headlines(news_data)
