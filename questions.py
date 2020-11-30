import csv
# tell it where the cvs file is....
f = open("C:\GEOM67\snakes\PSPSnakesLadders\SnakesQs.csv", "a")
f.close()

#open and read the file after the appending:
f = open("C:\GEOM67\snakes\PSPSnakesLadders\SnakesQs.csv", "r")
print(f.read())

