import requests
from bs4 import BeautifulSoup

def get_latest_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        headlines = soup.find_all('h2', class_='headline')  # Adjust class based on the website structure
        
        for index, headline in enumerate(headlines, start=1):
            print(f"{index}. {headline.text.strip()}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the news: {e}")

if __name__ == "__main__":
    news_url = "https://www.example-news-website.com"  # Replace with the actual news website URL
    print("Latest News Headlines:\n")
    get_latest_news(news_url)
