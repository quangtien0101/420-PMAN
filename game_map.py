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
        empty_list = []
        self.data = [[ empty_list for y in range(height)] for x in range(width)]#initialize the map data[y-coordinate][x-coordinate]
        
        # this is for pacman to check if it's scan the whole map yet
        self.checked = [[0 for y in range(height)] for x in range(width)]

    # update all the agents new location
    def update(self, agents_location, agents_new_coordinate, agent_symbol):

        x = agents_location[0]
        y = agents_location[1]

        new_x = agents_new_coordinate[0]
        new_y = agents_new_coordinate[1]

            #[new_y][new_x]

        # removing the agent from the old location
        try:
            self.data[y][x].remove(agent_symbol)
            if len(self.data[y][x]) == 0:
                self.data[y][x] = [self.symbol.empty]

        except ValueError:
            pass
        #update agent's new location
        l = copy.deepcopy(self.data[new_y][new_x])
        l.append(agent_symbol)
        self.data[new_y][new_x] = copy.deepcopy(l)

    def map_print(self):
        #print (self.data)
        for y in range(self.height):
            print(self.data[y])
            

        print ("\n")

    def view_a_possition(self,possition):
        x = possition[0]
        y = possition[1]
        out = self.data[y][x]
        return out

    def map_dimension(self):
        return [self.width, self.height]

    def load_food(self, foods):
        for i in foods:
            self.update(i,i,self.symbol.food)

    def load_agents(self, agents):
        for a in agents:
            self.update(a.location, a.location, a.my_symbol)

    def remove_food(self, food_location):
        x = food_location[0]
        y = food_location[1]

        try:
            self.data[y][x].remove(self.symbol.food)
        except:
            pass