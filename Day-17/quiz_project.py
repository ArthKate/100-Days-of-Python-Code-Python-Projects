from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(item["text"], item["answer"]) for item in question_data]


#quiz = QuizBrain(question_bank)

def take_quiz():
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")

take_quiz()