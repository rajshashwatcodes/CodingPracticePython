import random

def get_quote_of_the_day():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The best way to predict the future is to invent it. - Alan Kay",
        "It does not matter how slowly you go as long as you do not stop. - Confucius"
    ]
    return random.choice(quotes)

def main():
    print("Quote of the Day:")
    print(get_quote_of_the_day())

if __name__ == "__main__":
    main()
