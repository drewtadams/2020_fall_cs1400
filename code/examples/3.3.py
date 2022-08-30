# Modify the code below:
import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
userNumber= int(((smaller+larger)/2))
count = 0
while True:
    count += 1
    myNumber=myNumber
    userNumber= int((smaller+larger)/2) 
    print("your number is", userNumber)
    str(input("Enter =, <, or >: "))

    if userNumber < myNumber:
        smaller=smaller
        larger= userNumber-1
        print(smaller, larger)
    elif userNumber > myNumber:
        larger= larger
        smaller= userNumber+1
        print(smaller, larger)
    else:
        print("You've got it in", count, "tries!")
        break