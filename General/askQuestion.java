import java.util.Scanner;

class Question {
    private String question;
    private String[] options;
    private char correctAnswer;

    public Question(String question, String[] options, char correctAnswer) {
        this.question = question;
        this.options = options;
        this.correctAnswer = correctAnswer;
    }

    public boolean askQuestion() {
        Scanner scanner = new Scanner(System.in);
        System.out.println(question);

        for (int i = 0; i < options.length; i++) {
            System.out.println((char)('A' + i) + ". " + options[i]);
        }

        System.out.print("Your answer: ");
        char answer = scanner.nextLine().toUpperCase().charAt(0);

        return answer == correctAnswer;
    }
}

public class QuizGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Question[] questions = new Question[]{
            new Question("What is the capital of France?", new String[]{"Paris", "London", "Berlin", "Madrid"}, 'A'),
            new Question("Which planet is known as the Red Planet?", new String[]{"Earth", "Mars", "Jupiter", "Saturn"}, 'B'),
            new Question("What is the largest mammal?", new String[]{"Elephant", "Whale", "Shark", "Giraffe"}, 'B')
        };

        int score = 0;

        System.out.println("Welcome to the Quiz Game!");
        System.out.println("Answer the following questions:");

        for (Question question : questions) {
            if (question.askQuestion()) {
                System.out.println("Correct!\n");
                score++;
            } else {
                System.out.println("Wrong answer.\n");
            }
        }

        System.out.println("You completed the quiz!");
        System.out.println("Your score: " + score + "/" + questions.length);

        scanner.close();
    }
}
