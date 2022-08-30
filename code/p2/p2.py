'''
Project Name: turtle patterns
Author: drew adams
Due Date: 10/02/2020
Course: CS1400-x03

Draw 3 different shapes of different colors using the turtle module and our own custom functions.
We learned that we need to make frequent use of penup/pendown and to remember to use begin_fill.
'''

from random import randint
from turtle import colormode, setup, Turtle


def create_house(t):
    ''' draw a house using the passed turtle '''
    EAVE_ANGLE = 28.072486921385
    
    # set house color
    t.fillcolor(192,192,192)
    t.begin_fill()
    
    # move and create the left side of the house
    t.setheading(180)
    t.penup()
    t.forward(60)
    t.right(90)
    t.pendown()
    t.forward(60)
    
    # create the roof and the right side side of the house
    t.right(90-EAVE_ANGLE)
    t.forward(68)
    t.right(2*EAVE_ANGLE)
    t.forward(68)
    t.right(90-EAVE_ANGLE)
    t.forward(60)
    t.right(90)
    t.forward(120)
    t.end_fill()
    
    # create the door
    t.penup()
    t.goto(-10,0)
    t.setheading(90)
    
    # set door color
    t.fillcolor(191,187,172)
    t.pendown()
    t.begin_fill()
    
    # loop the sides of the door
    for _ in range(2):
        t.forward(40)
        t.right(90)
        t.forward(20)
        t.right(90)
    t.end_fill()
    
    
def create_grass(t, width):
    ''' draw grass of random blade heights '''
    # pick up and orient the turtle
    t.penup()
    t. setheading(0)
    
    # setup grass color
    t.pencolor(0,109,0)
    t.fillcolor(0,109,0)
    
    # set the turtle to the left of the house
    start = (width/3)-(width/2)
    t.goto(start, 0)
    t.pendown()
    
    # draw grass blades with random heights in front of the house
    print('position: ', t.position())
    while t.position()[0] < abs(start):
        blade_length = randint(1,3)
        t.left(90)
        t.forward(blade_length)
        t.right(180)
        t.forward(blade_length)
        t.left(90)
        t.forward(1)
        
        
def create_sun(t, height, width):
    ''' draw a simple sun '''
    # navigate to a spot inside the window
    t.penup()
    x = (width/2)-60
    y = (height/2)-60
    t.goto(x,y)
    
    # begin drawing
    t.pendown()
    t.pencolor(180, 180, 0)
    t.fillcolor(255, 255, 0)
    t.begin_fill()
    t.circle(20)
    t.end_fill()


def main():
    '''
    Program starts here.
    '''
    MIN_HEIGHT = 300
    MIN_WIDTH = 300
    
    
    try:
        # ask for height and width of the application window
        height = int(input('Enter the window height: '))
        width = int(input('Enter the window width: '))
    except ValueError:
        print("Enter positive integers for width and height.")
        return
    
    if MIN_WIDTH < 1 or MIN_HEIGHT < 1:
        print("Enter positive integers for width and height greater than 299.")
        return 
    
    # create the turtle
    colormode(255)
    setup(width=width, height=height, startx=None, starty=None)
    t = Turtle()
    t.speed(0)
    
    # start drawing the house
    create_house(t)
    create_grass(t, width)
    create_sun(t, height, width)


if __name__ == "__main__":
    main()