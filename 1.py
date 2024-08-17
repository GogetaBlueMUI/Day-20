questions_and_answers = [
    ('What is the capital of France?', 'Paris'),
    ('What is 2 + 2?', '4'),
    ('What is the largest planet in our solar system?', 'Jupiter')
]

score = 0

def ask_question(question, correct_answer):
    user_answer = input(question + ' ')
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")
        return False

for question, correct_answer in questions_and_answers:
    if ask_question(question, correct_answer):
        score += 1

print(f"Game over! Your final score is: {score}/{len(questions_and_answers)}")
