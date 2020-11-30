import csv
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
        answer = [5]

        question.append(questions)
        option1.append(A)
        option2.append(B)
        option3.append(C)
        option4.append(D)
        answers.append(answer)

    print(question)
    print(option1)
    print(option2)
    print(option3)
    print(option4)