# This program allows us to update questions using csv files
# Creator Honglin (Jim) Wei
# Modified: Dec 4, 2020

# import the correct modules
import csv
import random

def MultiChoice():
    # opening the csv file
    with open('SnakesQs.csv') as csvfile:
        # the csv file reader uses comma as delimiter
        readCSV = csv.reader(csvfile, delimiter=',')
        # generate blank lists to store the question variables
        question = []
        option1 = []
        option2 = []
        option3 = []
        option4 = []
        answers = []

        # loops into the csv to pull column variable into list
        for row in readCSV:
            # column 0 in csv is the question, col 1 is choice A etc.
            Q = row[0]
            A = row[1]
            B = row[2]
            C = row[3]
            D = row[4]
            answer = row[5]
            
            # puts the variables back into the empty lists with append
            question.append(Q)
            option1.append(A)
            option2.append(B)
            option3.append(C)
            option4.append(D)
            answers.append(answer)
        
        # closing the csv file
        csvfile.close()

        # print("amount of rows:" + str(len(question)))
        length = len(question)
        nums = []
        nums.extend(range(1,length))
        
        counter = 0
        while counter < 3:
            # we shuffle the questions so the questions are random
            random.shuffle(nums)
            
            q = nums[0]
            # print("This is Question:" + str(q))
            # print(q)
            # print("The correct answer is:" + str(answers[q]))

            print("Question: " + question[q])
            print("A) " + option1[q])
            print("B) " + option2[q])
            print("C) " + option3[q])
            print("D) " + option4[q])
            
            print("Please answer this question using letters A, B, C, D")

            # Prompts user for input
            user_answer = input(">>")
            # Conditionals based on success or failure
            if user_answer.upper() == answers[q]:
                print("You've got it!")
                break
            else:
                print("Sorry that's not it, try again")
                counter += 1
                print("That's strike", counter, "!\n")
                if counter == 3:
                    print("GAME OVER")
                    exit(0)

# calling function individually for testing
# MultiChoice()