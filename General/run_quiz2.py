import random

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

def ask_question(question):
    print("\n" + question.question)
    for i, option in enumerate(question.options):
        print(f"{i + 1}. {option}")
    
    user_answer = input("Your answer (1/2/3/4): ")
    return int(user_answer) - 1

def run_quiz(questions):
    score = 0
    for question in questions:
        user_answer = ask_question(question)
        if question.options[user_answer] == question.answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question.answer}")
    print(f"\nYour final score is {score} out of {len(questions)}")

def main():
    questions = [
        Question("What is the capital of France?", ["Berlin", "London", "Paris", "Rome"], "Paris"),
        Question("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
        Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], "Mars"),
        Question("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"], "Harper Lee"),
    ]
    
    random.shuffle(questions)
    run_quiz(questions)

if __name__ == "__main__":
    main()
