def count_word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def main():
    print("Welcome to the Word Frequency Counter!")
    text = input("Enter some text: ")
    word_frequency = count_word_frequency(text)
    print("\nWord frequency:")
    for word, freq in word_frequency.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
