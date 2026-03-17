import os 
from prettyPrint import * 

# printing the title 
text = '' 
with open('title.txt') as file:
    text = file.read()

centerPrint(text)
divPrint()
print()

menu = ""
menu += "(1) Connect to Plotter\n"
menu += "(2) Exit"

# start of menu driven program 
print(menu)
print()
while True:
    inp = input("GenZ_CNC > ")
    match inp:
        case '1': 
            print('Case 1')
        case '2':
            break
        case _: 
            print("Option not available! Choose from the following: ")
            print(menu)
