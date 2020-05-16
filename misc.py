#!/usr/local/bin/python3.7

class Symbol:
    def __init__(self):
        self.pacman = "p"
        self.monster = "m"
        self.food = "."
        self.wall = "%"
        self.empty = " "

def manhattandistance(possition, destination):
    return abs(possition[0] - destination[0] ) + abs( possition[1] - destination[1] )

