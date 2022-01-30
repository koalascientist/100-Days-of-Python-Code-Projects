from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# The question_bank variable contains a list of question objects that contain the text of the question
# and the answer to the question.
for entry in question_data:
    question = Question(entry["question"], entry["correct_answer"])
    question_bank.append(question)

# Start the quiz game
quiz = QuizBrain(question_bank)

# While there are still questions, continue the game
while quiz.still_has_questions():
    quiz.next_question()

# Final words
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

