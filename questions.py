import csv
# tell it where the cvs file is....
# f = open("SnakesQs.csv", "a")

#open and read the file after the appending:
f = open("SnakesQs.csv", "r")
print(f.read())

f.close()