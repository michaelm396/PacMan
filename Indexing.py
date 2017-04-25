__author__ = 'moorerm'

import turtle
from Stack import Stack

class Index():
    stack = Stack() #stack call
    def __init__(self):
        self.indexpacman = turtle.Turtle()
        self.X = -480
        self.Y = -300
        self.pathX = Stack()#Stack()
        self.pathY = Stack()
        self.blockX = Stack()
        self.blockY = Stack()


    def shift(self):
        """
        post: shhift Y values for new row
        """
        self.Y += 40 #move Y values over
        #self.X = -480
        self.indexpacman.goto(self.X,self.Y)  #sets new psotion

    def reset_shift(self):
        """
        post: resets the shift for bottom row
        """
        self.Y = -300 #sets Y value
        self.X += 40
        self.indexpacman.goto(self.X,self.Y) #setts new positon

    def dots(self):
        """
        post: position
        """
        self.Y =+ 40

    def check_dots(self):
        """
        post: compares X and Y values for blocked positons
        """
        a = [-140,-20,20,60,180,220,260] #list for y values
        for i in a: #loop to iterate thru list
            if self.X == -200 and self.Y == i or self.X == 200 and self.Y == i : #compares X and Y values
                self.blockX.push(self.X) #push value into list
                self.blockY.push(self.Y)
                self.Y += 40
                self.indexpacman.goto(self.X,self.Y) #goes to specific position

        b = [-220,-180,-140,-100,-60,20,60,100,140,180]
        for i in b:
            if self.X == -360 and self.Y == i or self.X == 360 and self.Y == i:
                self.blockX.push(-360)
                self.blockY.push(self.Y)
                self.Y += 40
                self.indexpacman.goto(self.X,self.Y)

        c = [-140]
        for i in c:
            if self.X == -400 and self.Y == i or self.X == 400 and self.Y == i:
                self.blockX.push(-400)
                self.blockY.push(self.Y)
                self.Y += 40
                self.indexpacman.goto(self.X,self.Y)

        d = [-140]
        for i in d:
            if self.X == -440 and self.Y == i or self.X == 440 and self.Y == i:
                self.blockX.push(-440)
                self.blockY.push(self.Y)
                self.Y += 40
                self.indexpacman.goto(self.X,self.Y)

        e = [-140,100]
        for i in e:
            if self.X == -320 and self.Y == i or self.X == 320 and self.Y == i:
                self.blockX.push(-320)
                self.blockY.push(self.Y)
                self.Y += 40
                self.indexpacman.goto(self.X,self.Y)

        f = [-140,100]
        for i in f:
            if self.X == -280 and self.Y == i or self.X == 280 and self.Y == i:
                self.blockX.push(-280)
                self.blockY.push(self.Y)
                self.Y += 40
                self.indexpacman.goto(self.X,self.Y)

        g = [-140,260]
        for i in g:
            if self.X == -160 and self.Y == i or self.X == 160 and self.Y == i:
                self.blockX.push(-160)
                self.blockY.push(self.Y)
                self.Y += 40
                self.indexpacman.goto(self.X,self.Y)

        h = [-300,-260,-220,-140,260]
        for i in h:
            if self.X == -120 and self.Y == i or self.X == 120 and self.Y == i:
                self.blockX.push(-120)
                self.blockY.push(self.Y)
                self.Y += 40
                self.indexpacman.goto(self.X,self.Y)

        j = [-60,100]
        for i in j:
            if self.X == -80 and self.Y == i or self.X == 80 and self.Y == i:
                self.blockX.push(-80)
                self.blockY.push(self.Y)
                self.Y += 40
                self.indexpacman.goto(self.X,self.Y)

        k = [-260,-60,100]
        for i in k:
            if self.X == -40 and self.Y == i or self.X == 40 and self.Y == i:
                self.blockX.push(-20)
                self.blockY.push(self.Y)
                self.Y += 40
                self.indexpacman.goto(self.X,self.Y)


        l = [-260,-140,-100,-60,100,140,180]
        for i in l:
            if self.X == 0 and self.Y == i:
                self.blockX.push(20)
                self.blockY.push(self.Y)
                self.Y += 40
                self.indexpacman.goto(self.X,self.Y)



