#!/usr/local/bin/python3.7
from misc import *
from random import seed
from random import randint

import copy

class Monster:
    def __init__ (self, location, view, map_dimension):

        self.location = location # a list [x,y], pacman current location
        self.view = view # an interger 5

        self.legal_actions = ["up","down","left","right","still"]        

        self.symbol = Symbol()
        self.my_symbol = self.symbol.monster

        self.smart = False

    def remove_actions(self, direction):        
        try:
            self.legal_actions.remove(direction)
        except ValueError:
            print ("directions not in current legal actions")


    def move(self,global_map):
        direction = self.random_move(self.legal_actions)
        print("Monster moving ...")

        x = self.location[0]
        y = self.location[1]

        if ( direction == "still" ):
            global_map.update(self.location, self.location, self.my_symbol)
            return

        if ( direction == "left" ):
            new_x = x - 1
            new_location = [new_x, y]

            global_map.update(self.location, new_location, self.my_symbol)
            self.update(new_location)
            
            return

        if ( direction == "right" ):
            new_x = x + 1  
            new_location = [new_x, y]

            global_map.update(self.location, new_location, self.my_symbol)
            self.update(new_location)
            return 

        if ( direction == "up" ):
            new_y = y - 1  
            new_location = [x, new_y]

            global_map.update(self.location, new_location, self.my_symbol)
            self.update(new_location)
            return

        if ( direction == "down" ):
            new_y = y + 1  
            new_location = [x, new_y]

            global_map.update(self.location, new_location, self.my_symbol)
            self.update(new_location)
            return
        
     
    def random_move(self, move):
        #if there is just one possible move
        if (len(move) == 1):
            return move[0]

        #forcing pacman to move instead of standing still while it's possible
        try:
            self.remove_actions("still")
        except:
            pass
        value = randint(0,len(move)-1)
        return move[value]

    def update(self, new_location):
        self.location = copy.deepcopy(new_location)

    def make_monster_smart (self):
        self.smart = True