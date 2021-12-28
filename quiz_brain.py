
class Quiz_Brain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    
    def next_question(self):
        current_position = self.question_list[self.question_number]
        self.question_number += 1
        ask = input(f"Q{self.question_number}: {current_position.text} (True/False): ").lower()
        self.check_answer(ask, current_position.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("You are wrong!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score} points")