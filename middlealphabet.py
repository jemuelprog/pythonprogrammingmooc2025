letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")
middleletter = 0

if (letter1 > letter2 and letter1 < letter3) or (letter1 < letter2 and letter1 > letter3):
    middleletter = letter1
elif (letter2 > letter1 and letter2 < letter3) or (letter2 < letter1 and letter2 > letter3):
    middleletter = letter2
else:
    middleletter = letter3
print(f"The letter in the middle is {middleletter}")