#!/usr/local/bin/python3
import copy
from misc import *
class Map:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.symbol = Symbol()

        #GENERATE AN OPEN EMPTY MAP
        #this should be the map loading stage
        self.data = [[self.symbol.empty for y in range(height)] for x in range(width)] # generate the map data[y-coordinate][x-coordinate]
        
        # this is for pacman to check if it's scan the whole map yet
        self.checked = [[0 for y in range(height)] for x in range(width)]

    # update all the agents new location
    def update(self, agents_new_coordinate):
        #make a deep-copy version of the agents coordinate for easy reference
        self.agents_coordinate = copy.deepcopy(agents_new_coordinate)

        # agents_coordinat = {'pacman':[2,2], 'monster1':[3,3]}
        for a in agents_new_coordinate:
            new_x = agents_new_coordinate[a][0]
            new_y = agents_new_coordinate[a][1]
            #[new_y][new_x]

            self.data[new_y][new_x] = a

    def map_print(self):
        print (self.data)
        print ("\n")

    def view_a_possition(self,possition):
        x = possition[0]
        y = possition[1]
        out = self.data[y][x]
        return out