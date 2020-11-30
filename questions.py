import csv
# tell it where the cvs file is....
f = open("SnakesQs.csv", "a")
f.close()


#open and read the file after the appending:
f = open("SnakesQs.csv", "r")
print(f.read())

