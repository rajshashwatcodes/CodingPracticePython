def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Berlin"],
            "answer": "A"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen"],
            "answer": "A"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. H2O", "B. CO2", "C. NaCl"],
            "answer": "A"
        }
    ]

    score = 0

    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")

    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        for option in question['options']:
            print(option)
        user_answer = input("Your answer (A/B/C): ").upper()
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print(f"\nQuiz completed! Your score: {score}/{len(questions)}")

run_quiz()
