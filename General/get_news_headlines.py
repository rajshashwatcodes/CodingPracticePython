import requests
from bs4 import BeautifulSoup

def get_news_headlines(url):
    try:
        # Send a request to the website
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all headlines on the page (this may vary depending on the website structure)
        headlines = soup.find_all('h2')  # Example tag, change as needed

        # Extract and return the text of the headlines
        return [headline.get_text(strip=True) for headline in headlines]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the news: {e}")
        return []

def main():
    # URL of the news website (can be changed to any news website of your choice)
    url = 'https://www.bbc.com/news'  # Example URL

    print(f"Fetching news headlines from {url}...\n")

    # Get the news headlines
    headlines = get_news_headlines(url)

    # Display the headlines
    if headlines:
        print("Today's Top Headlines:")
        for idx, headline in enumerate(headlines, start=1):
            print(f"{idx}. {headline}")
    else:
        print("No headlines found.")

if __name__ == "__main__":
    main()
