import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Initialize the VADER sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyze the sentiment of the provided text using VADER sentiment analyzer.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        str: The sentiment category: 'Positive', 'Negative', or 'Neutral'.
    """
    # Compute the sentiment scores
    sentiment_scores = sid.polarity_scores(text)
    
    # Determine the sentiment category
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment

def main():
    print("Sentiment Analysis Tool")
    print("=======================")
    while True:
        # Get user input
        user_input = input("Enter a sentence to analyze (or 'quit' to exit): ")
        
        # Exit the loop if the user types 'quit'
        if user_input.lower() == 'quit':
            break
        
        # Analyze the sentiment of the input text
        sentiment = analyze_sentiment(user_input)
        
        # Print the result
        print(f"Sentiment: {sentiment}\n")

if __name__ == "__main__":
    main()
