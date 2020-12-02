import csv
import random
# tell it where the cvs file is....
# f = open("SnakesQs.csv", "a")

#open and read the file after the appending:
# f = open("SnakesQs.csv", "r")

with open('SnakesQs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    question = []
    option1 = []
    option2 = []
    option3 = []
    option4 = []
    answers = []

    for row in readCSV:
        questions = row[0]
        A = row[1]
        B = row[2]
        C = row[3]
        D = row[4]
        answer = row[5]

        question.append(questions)
        option1.append(A)
        option2.append(B)
        option3.append(C)
        option4.append(D)
        answers.append(answer)

    # random question selection
    nums = [1,2]
    q = random.choice(nums)
    print("This is Question:" + str(q))
    print(q)
    print("The correct answer is:" + str(answers[q]))

    print("Question: " + question[q])
    print("A) " + option1[q])
    print("B) " + option2[q])
    print("C) " + option3[q])
    print("D) " + option4[q])
    
    print("Please answer this question using letters A, B, C, D")

    user_answer = input(">>")
    if user_answer == answers[q]:
        print("You've got it!")