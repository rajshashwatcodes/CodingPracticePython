def count_words(sentence):
    # Split the sentence into words using whitespace as delimiter
    words = sentence.split()
    # Return the number of words in the sentence
    return len(words)

def main():
    print("Welcome to the Word Counter!")
    sentence = input("Enter a sentence: ")
    word_count = count_words(sentence)
    print(f"The number of words in the sentence is: {word_count}")

if __name__ == "__main__":
    main()
