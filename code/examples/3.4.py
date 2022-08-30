#user input
startPoint = abs(float(input("Enter the height from which the ball is dropped: ")))
INDEX_BOUNCE = float(input("Enter the bounciness index of the ball: "))
numBounce = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
#defined variables
totalDistance = 0
while numBounce != 0: #loops for how many bounces the user inputted
    #compute total distance based on startpoint and the index of the bounce
    newHeight = (startPoint * INDEX_BOUNCE) 
    totalDistance += startPoint + newHeight
    startPoint = newHeight 
    numBounce -= 1

#give output
print("Total distance traveled is:", totalDistance, "units.")