from Class import Turtle
import turtle
from Stack import Stack
import sys
from Indexing import Index
import time
import random

#Google was my friend
#Shoutout to Logan for giving me the idea to put my face on the screen!


def main():
    """
    Pre: calls on functions
    post:executes function
    param: None
    return: None
    """

    game = Turtle() #class call
    point = Index() #class call
    wn = turtle.Screen() #creates the screen
    wn.setup(1002,642) #screen size
    image = "grid4.gif"
    wn.bgpic(image)
    wn.addshape("Me.gif")
    wn.addshape("Me2.gif")
    wn.addshape("Me3.gif")
    game.pacman.shape("Me.gif")
    game.pacman.penup()

    print"This is PAC-ME-Man Silver Edition-Ultimate-Ultra Mega...Infinity 2.0 Million"
    print"The rules are pretty simple"
    print"The values increment by +40 or -40 depending on direction"
    print"Your task is to find the random point"
    Indexed(point)

    game.pacman.shape("Me.gif")
    print ""
    print"w-up"
    print"a-left"
    print"s-down"
    print"d-right"

    randomX = point.pathX.rand() #rgrabs random value from stacked list
    randomY = point.pathY.rand()
    game.pacman.goto(game.currentposX,game.currentposY) ### initial position is (20,0)
    game.X.push((game.currentposX)) #pushes current position to a stacked list
    game.Y.push((game.currentposY))
    moving(game,randomX,randomY)

    wn.exitonclick()

def moving(game,randomX,randomY):
    """
    pre: waits for user decision to move forward or backwards
    post: executes the motion
    param: game, randomX, randomY
    return: None
    """
    user = raw_input()


    print "The random Value X is:"
    print randomX #random value from X stacked list
    print "The random Value Y is:"
    print randomY

    if user == "a":
        Left(game,randomX,randomY) #function call

    elif user == "w":
        Up(game,randomX,randomY)

    elif user == "s":
        Down(game,randomX,randomY)

    elif user == "d":
        Right(game,randomX,randomY)

    else:
        moving(game,randomX,randomY)

def reset(game):
    game.pacman.speed(1)
    game.pacman.goto(0,20)

def Left(game,randomX,randomY):
    """
    pre: finds the position the user it at currently and moves them to the left by a whole position
    post: returns new position for turtle
    param: game, randomX, randomY
    return: new psotion of turtle
    """
    game.currentposX -= 40
    game.pacman.goto(game.currentposX,game.currentposY) #position on coordinate
    print "Current X:"
    print game.currentposX
    print "Current Y:"
    print game.currentposY
    game.pacman.setheading(180)
    game.X.push((game.currentposX)) #push the value of the position to a  stacked list
    game.Y.push((game.currentposY))
    game.check_dots() #function call
    #print game.X.top()
    game.pacman.dot(10) #stamps a dot on the screen
    wallY(game,randomX,randomY) #functuin call
    rando(randomX,randomY,game)
    moving(game,randomX,randomY)
    #wallX(game)

def Right(game,randomX,randomY):
    """
    pre: finds the position the user it at currently and moves them to the left by a whole position
    post: returns new position for turtle
    param: game, randomX, randomY
    return: new position of turtle
    Commenting does the exact same thing as Left() except the direction changes
    """
    game.currentposX += 40
    game.pacman.goto(game.currentposX,game.currentposY)
    print "Current X:"
    print game.currentposX
    print "Current Y:"
    print game.currentposY
    game.pacman.setheading(0)
    game.X.push((game.currentposX))
    game.Y.push((game.currentposY))
    game.check_dots()
    game.pacman.dot(10)
    #print game.X.top()
    wallY(game,randomX,randomY)
    rando(randomX,randomY,game)
    moving(game,randomX,randomY)


def Up(game,randomX,randomY):
    """
    pre: finds the position the user it at currently and moves them to the left by a whole position
    post: returns new position for turtle
    param: game, randomX, randomY
    return: new position of turtle
    Commenting does the exact same thing as Left() except the direction changes
    """
    game.currentposY += 40
    game.pacman.goto(game.currentposX,game.currentposY)
    print "Current X:"
    print game.currentposX
    print "Current Y:"
    print game.currentposY
    game.pacman.setheading(90)
    game.X.push((game.currentposX))
    game.Y.push((game.currentposY))
    game.check_dots()
    game.pacman.dot(10)

    #print game.X.top()
    rando(randomX,randomY,game)
    moving(game,randomX,randomY)

def Down(game,randomX,randomY):
    """
    pre: finds the position the user it at currently and moves them to the left by a whole position
    post: returns new position for turtle
    param: game, randomX, randomY
    return: new position
    Commenting does the exact same thing as Left() except the direction changes
    """
    game.currentposY -= 40
    game.pacman.goto(game.currentposX,game.currentposY)
    print "Current X:"
    print game.currentposX
    print "Current Y:"
    print game.currentposY
    game.pacman.setheading(270)
    game.X.push((game.currentposX))
    game.Y.push((game.currentposY))
    game.check_dots()
    game.pacman.dot(10)
    #print game.X.top()
    rando(randomX,randomY,game)
    moving(game,randomX,randomY)


def wallY(game,randomX,randomY):
    """
    pre: finds the position the user it at currently and checks for mathving function
    post: returns new postion of turtle
    param: game, randomX, randomY
    return: postion through swirl
    """
    if game.currentposY == -20 and game.currentposX == -480: #compare values
        game.Y.pop() #pops list
        game.currentposY = 20 #sets new position
        game.currentposX = 480
        game.Y.push((game.currentposY)) #push the value of that position in a stack list
        game.pacman.goto(game.currentposX,game.currentposY)
        game.pacman.dot(15) #dot for pacman

    elif game.currentposY == 20 and game.currentposX == 480: #compare values
        game.Y.pop()
        game.currentposY = -20
        game.currentposX = -480
        game.Y.push((game.currentposY))
        game.pacman.goto(game.currentposX,game.currentposY)
        game.pacman.dot(15)

    else:
        moving(game,randomX,randomY) #function call

def rando(randomX,randomY,game):
    """
    pre: compares current position to random position
    post: ends progam once condition is met
    param: randomX, randomY, game
    return: end of program

    """
    if game.currentposX == randomX and game.currentposY == randomY: #compares values
        reset(game)
        p = 0 #generic variable for loop
        q=0
        t=0
        game.pacman.shape("Me.gif") #shape of turtle
        game.pacman.speed(7)
        while p != 5: #generic loop to spin character
            game.pacman.circle(p) #makes the turtle spin
            game.pacman.shape("Me.gif") #turtle shape
            p += 1
        while q != 3:
            game.pacman.circle(p)
            game.pacman.shape("Me2.gif")
            q += 1
        while t != 2:
            game.pacman.circle(p)
            game.pacman.shape("Me3.gif")
            t+=1


        print"You've Found the random point"
        print "It took you the following moves to reach your goal:"
        print game.X.size()
        print"Thanks for Playing :)"
        sys.exit() #exits terminal

    #print random.choice(point.pathY)

def Indexed(point):
    """
    pre: finds corner of coordinate map
    post: places dots on every point except specific ones
    param: point
    return: points on map
    """
    point.indexpacman.penup() #penup
    point.pathX.push((point.X)) #pushes value to list
    point.pathY.push((point.Y))
    point.indexpacman.goto(point.X,point.Y)
    while point.X != 480: #checks for top of map
        if point.Y == -300: #checks for top of map and resets
            point.X += 0
        else:
            point.reset_shift() #function call
        while point.Y != 340: #checks for top of map
            point.check_dots() #function call
            point.indexpacman.color('yellow')
            point.indexpacman.up() #penup
            point.indexpacman.dot(10) #don
            point.indexpacman.speed(0)
            point.shift() #shifts value
            point.pathY.push((point.Y)) #pushes value to list
            point.pathX.push((point.X))


main()

