# Simple Quiz Game

questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["A. Harper Lee", "B. Jane Austen", "C. Mark Twain", "D. J.K. Rowling"],
        "answer": "A"
    },
    {
        "question": "What is the square root of 64?",
        "choices": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    }
]

def run_quiz(questions):
    score = 0
    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}: {question['question']}")
        for choice in question['choices']:
            print(choice)
        answer = input("Your answer (A, B, C, D): ").strip().upper()
        if answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}")
    print(f"\nYour final score is {score}/{len(questions)}")

def main():
    print("Welcome to the Quiz Game!")
    run_quiz(questions)
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
