class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q. {self.question_number}: {current_question.text} (True/False): ")
        return self.check_answer(ans, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if correct_answer.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"You're score is: {self.score}/{self.question_number}")
        print("\n")
