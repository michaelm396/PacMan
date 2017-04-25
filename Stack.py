# Stack.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014

import random

class Stack(object):

    #------------------------------------------------------------

    def __init__(self):

        '''post: creates an empty LIFO stack'''

        self.items = []

    def __str__(self):

        return str(self.items)
    __repr__ = __str__
    #------------------------------------------------------------

    def push(self, item):
        
        '''post: places x on top of the stack'''

        self.items.append(item)

    #------------------------------------------------------------

    def pop(self):

        '''post: removes and returns the top element of 
        the stack'''

        return self.items.pop()

    #------------------------------------------------------------

    def top(self):

        '''post: returns the top element of the stack without 
        removing it'''

        return self.items[-1]

    #------------------------------------------------------------

    def size(self):

        '''post: returns the number of elements in the stack'''

        return len(self.items)
    def rand(self):
        """
        post: returns  random obejct in the stck list
        #########################used as Big O analysis computation
        """

        return random.choice(self.items)

    def high_score(self):
        """
        returns the highest score in the stack list
        """

        return min(self.items)