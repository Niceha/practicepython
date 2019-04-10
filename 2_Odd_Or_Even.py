'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

        If the number is a multiple of 4, print out a different message.
        Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

def evn_odd():
  num=input("Enter any number to test : ")
  check=int(input("Enter any number to check as divisor : "))
  try:
    usern=int(num)
  except:
    print("Please enter a valid number.")
      
  if usern%2==0 and usern%4!=0:
    print("You have entered even number")
  elif usern%4 == 0:
    print("Multiple of 4")
  else:
    print("You have entered an odd number")

  if usern%check==0 :
    print("%r divides %r"%(check,usern/check))
  else:
    print("%r isnt divisible by %r"%(usern,check))

evn_odd()
