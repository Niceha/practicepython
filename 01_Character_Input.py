'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

        Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
            Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

import datetime
loopcount = int(input("Enter number of inputs: "))


def turn_100():
  for i in range(1,loopcount+1):

    name=input("Enter your name : ")
    ages=input("Enter your age : ")
    try:
      age=int(ages)
    except:
      print("Please enter a valid number.")
    
    current_year=datetime.date.today().year ##.year
    diff = int(current_year + (100 - age))
    print("Hi %s you will turn 100 in year %r"%(name,diff))

turn_100()
