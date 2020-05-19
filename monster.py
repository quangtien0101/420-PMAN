#!/usr/local/bin/python3.7

from random import seed
from random import randint

class Monster:
    def __init__ (self, location, view, map_dimension, food):
        self.location = location # a list [x,y], pacman current location
        self.food = food # an int, the total number of food, map provided
        self.view = view # an interger 5

        self.legal_actions = ["up","down","left","right","still"]        


    def remove_actions(self, direction):        
        try:
            self.legal_actions.remove(direction)
        except ValueError:
            print ("directions not in current legal actions")


    def move(self):
        print("Monster randomly moving")

     
    def random_move(self, move):
        #if there is just one possible move
        if (len(move) == 1):
            return move[0]

        #forcing pacman to move instead of standing still while it's possible
        self.remove_actions("still")

        seed(1)
        value = randint(0,len(move)-1)
        return move[value]
