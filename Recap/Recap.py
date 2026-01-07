# Simple multiple-choice quiz (3 questions, options a, b, c)

questions = [
    {
        "text": """Which data type in Python can store a sequence of items that can change?
a) string
b) list
c) tuple""",
        "correct": "b"
    },
    {
        "text": """Which keyword is used to write a conditional in Python?
a) if
b) for
c) def""",
        "correct": "a"
    },
    {
        "text": """What does the function input() do?
a) Prints text to the screen
b) Stops the program
c) Reads text typed by the user""",
        "correct": "c"
    }
]


def run_quiz():
    """
    Goes through all questions, asks the user for an answer,
    validates the input (a, b, or c) with try/except,
    and counts how many answers are correct.
    Returns the final score.
    """
    print("Welcome to the quiz!\n")
    score = 0

    for q in questions:
        print(q["text"])          # show the full question with options

        # input + validation with try/except
        while True:
            try:
                answer = input("Your answer (a, b, or c): ").strip().lower()

                # check if the answer is one of the valid options
                if answer not in ("a", "b", "c"):
                    # if not valid, raise an error on purpose
                    raise ValueError

                # if we get here, the answer is valid → exit the loop
                break

            except ValueError:
                print("Invalid input. Please type only 'a', 'b', or 'c'.\n")

        if answer == q["correct"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong.\n")

    return score


def grade(score):
    """
    Prints the result of the quiz.
    - PASSED if score is 2 or 3
    - FAILED if score is 1 or 0
    """
    print("=== Quiz result ===")
    print("You got", score, "out of 3.")

    if score >= 2:
        print("Result: PASSED")
    else:
        print("Result: FAILED")


# Run the quiz and show the grade
final_score = run_quiz()
grade(final_score)
