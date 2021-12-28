from data import question_data
from question_model import Question
from quiz_brain import Quiz_Brain


logo = ''''
             _     
            (_)    
  __ _ _   _ _ ____
 / _` | | | | |_  /
| (_| | |_| | |/ / 
 \__, |\__,_|_/___|
    | |            
    |_|       
'''
print(logo)


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz_Brain(question_bank)   
while quiz.still_has_questions():
    quiz.next_question()    
    
print("Congratulations! You've completed the Quizz Game!")
print(f"Your final score: {quiz.score} points")
