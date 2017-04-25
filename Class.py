__author__ = 'moorerm'

import turtle
from Stack import Stack

class Turtle():
    stack = Stack()
    def __init__(self):
        self.pacman = turtle.Turtle()
        self.currentposX = 0
        self.currentposY = 20
        self.Y = Stack()
        self.X = Stack()

    def check_dots(self):
        """
        post: stops the dots from being drown on certain positions
        """
        a = [-140,-20,20,60,180,220,260] #list for Y values
        for i in a: #loop to traverse through list
            if self.currentposX == -200 and self.currentposY == i or self.currentposX == 200 and self.currentposY == i : #compares X nd Y values
                self.X.pop() #pops top of list
                self.Y.pop() #pops top of list
                self.currentposX = self.X.top() #sets new top
                self.currentposY = self.Y.top() #sets new top
                self.pacman.goto(self.currentposX,self.currentposY) #gos to specific position

        ############### The rest of the code does the exact same thing except it has different values it compares


        b = [-220,-180,-140,-100,-60,20,60,100,140,180]
        for i in b:
            if self.currentposX == -360 and self.currentposY == i or self.currentposX == 360 and self.currentposY == i:
                self.X.pop()
                self.Y.pop()
                self.currentposX = self.X.top()
                self.currentposY = self.Y.top()
                self.pacman.goto(self.currentposX,self.currentposY)

        c = [-140]
        for i in c:
            if self.currentposX == -400 and self.currentposY == i or self.currentposX == 400 and self.currentposY == i:
                self.X.pop()
                self.Y.pop()
                self.currentposX = self.X.top()
                self.currentposY = self.Y.top()
                self.pacman.goto(self.currentposX,self.currentposY)

        d = [-140]
        for i in d:
            if self.currentposX == -440 and self.currentposY == i or self.currentposX == 440 and self.currentposY == i:
                self.X.pop()
                self.Y.pop()
                self.currentposX = self.X.top()
                self.currentposY = self.Y.top()
                self.pacman.goto(self.currentposX,self.currentposY)

        e = [-140,100]
        for i in e:
            if self.currentposX == -320 and self.currentposY == i or self.currentposX == 320 and self.currentposY == i:
                self.X.pop()
                self.Y.pop()
                self.currentposX = self.X.top()
                self.currentposY = self.Y.top()
                self.pacman.goto(self.currentposX,self.currentposY)

        f = [-140,100]
        for i in f:
            if self.currentposX == -280 and self.currentposY == i or self.currentposX == 280 and self.currentposY == i:
                self.X.pop()
                self.Y.pop()
                self.currentposX = self.X.top()
                self.currentposY = self.Y.top()
                self.pacman.goto(self.currentposX,self.currentposY)

        g = [-140,260]
        for i in g:
            if self.currentposX == -160 and self.currentposY == i or self.currentposX == 160 and self.currentposY == i:
                self.X.pop()
                self.Y.pop()
                self.currentposX = self.X.top()
                self.currentposY = self.Y.top()
                self.pacman.goto(self.currentposX,self.currentposY)

        h = [-300,-260,-220,-140,260]
        for i in h:
            if self.currentposX == -120 and self.currentposY == i or self.currentposX == 120 and self.currentposY == i:
                self.X.pop()
                self.Y.pop()
                self.currentposX = self.X.top()
                self.currentposY = self.Y.top()
                self.pacman.goto(self.currentposX,self.currentposY)

        j = [-60,100]
        for i in j:
            if self.currentposX == -80 and self.currentposY == i or self.currentposX == 80 and self.currentposY == i or self.currentposX == 0 and self.currentposY == i:
                self.X.pop()
                self.Y.pop()
                self.currentposX = self.X.top()
                self.currentposY = self.Y.top()
                self.pacman.goto(self.currentposX,self.currentposY)

        k = [-260,-60,100]
        for i in k:
            if self.currentposX == -40 and self.currentposY == i or self.currentposX == 40 and self.currentposY == i:
                self.X.pop()
                self.Y.pop()
                self.currentposX = self.X.top()
                self.currentposY = self.Y.top()
                self.pacman.goto(self.currentposX,self.currentposY)


        l = [-260,-140,-100,-60,100,140,180]
        for i in l:
            if self.currentposX == 0 and self.currentposY == i:
                self.X.pop()
                self.Y.pop()
                self.currentposX = self.X.top()
                self.currentposY = self.Y.top()
                self.pacman.goto(self.currentposX,self.currentposY)

