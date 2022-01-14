from question_model import Question
from data import question_data2
from quiz_brain import QuizBrain

question_bank = []
for items in question_data2:
    question_bank.append(Question(items["question"], items["correct_answer"]))
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You have completed your quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
