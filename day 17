# MAIN
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

qb = []
for a in range(len(question_data)):
    new_q = Question(question_data[a]['text'], question_data[a]['answer'])
    #print(f'{new_q.text} \n{new_q.answer}')
    qb.append(new_q)


quiz = QuizBrain(qb)
while quiz.still_has_questions():
    quiz.next_question()
    
    
#DATA
question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]



#QUIZ_BRAIN
class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self,):
        current_question = self.question_list[self.question_num]
        ans = input(f"Q.{self.question_num+1}: {current_question.text} (True/False): ")
        current_answer = current_question.answer
        if ans == current_answer:
            self.score += 1
            print(f'Answer: {current_answer} \nYour Score:{self.score}'  )
        else:
            print(f'Answer: {current_answer} \nYour Score:{self.score}'  )
        self.question_num+=1

#QUESTION_MODEL
class Question:
    def __init__(self, txt, ans):
        self.text = txt
        self.answer = ans
