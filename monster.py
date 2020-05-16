#!/usr/local/bin/python3.7

class Monster:
    def __init__ (self, location, view, map_dimension):
        self.location = location # a list [x,y]
        self.view = view # an interger 5
        self.map = map_dimension # a list [lenght,height]
    
    def move(self):
        print("Monster randomly moving")

     