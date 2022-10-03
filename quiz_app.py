quiz = {
    "question1": {
        "question": "What is the capital of France ?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany ?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy ?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of France ?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal ?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland ?",
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Austria ?",
        "answer": "Vienna"
    }
}

score = 0

for key,value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1
        print("Your score is:" + str(score))

    else:
        print("Wrong")
        print("The correct answer is " + str(value['answer']))
        print("Your score is " + str(score))

print("Your total score is " + str(score) + " is out of " + str(len(quiz)))
print("Your percentage is " + str((score * 100)//len(quiz)))