#!/usr/local/bin/python3.7

from pacman import *
from monster import *
from game_map import*
from misc import *

import sys


symbol = Symbol()

def get_legal_actions(agent, Map, game_level):
    #Don't let the agent move out side the map or to go through wall
    x = agent.location[0]
    y = agent.location[1]

    #reset the legal actions before striping the illegal
    agent.legal_actions = ["up","left","down","right","still"]
    if (x > 0):
        if (symbol.wall in Map.data[y][x-1]):
            agent.remove_actions("left")

        if (game_level < 3):
            if (symbol.monster in Map.data[y][x-1]):
                agent.remove_actions("left")
    else:
        agent.remove_actions("left")

    if (x < Map.width -1):
        if (symbol.wall in Map.data[y][x+1]):
            agent.remove_actions("right")

        if (game_level < 3):
            if (symbol.monster in Map.data[y][x+1]):
                agent.remove_actions("right")

    else:
        agent.remove_actions("right")

    if (y > 0):
        if (symbol.wall in Map.data[y-1][x]):
            agent.remove_actions("up")

        if (game_level < 3):
            if (symbol.monster in Map.data[y-1][x]):
                agent.remove_actions("up")

    else:
        agent.remove_actions("up")

    if (y < Map.height - 1):
        if (symbol.wall in Map.data[y+1][x]):
            agent.remove_actions("down")

        if (game_level < 3):
            if (symbol.monster in Map.data[y+1][x]):
                agent.remove_actions("down")

    else:
            agent.remove_actions("down")

# tell pacman to eat the food
# this also check if pacman has already ate all the food, therefore the game can end
def state_check(pacman, global_map):
    x = pacman.location[0]
    y = pacman.location[1]

    # there is food at pacman's current location
    if symbol.food in global_map.data[y][x]:
        result = pacman.eat_food()
        global_map.remove_food([x,y])
        if result == "win":
            print ("Pacman win the game!")
            return True
    
    # there is a monster at pacman's current location
    if (symbol.monster in global_map.data[y][x]):
        print("Pacman die")
        return True

    return False

def set_level(level):
    game_level = level
    

def main():
    #generate maps
    #generate agents location

    # set map level
    game_level = 3

    # define a 8 X 8 map
    global_map = Map(8, 8)

    food_pos = [[4,1], [1,1],[2,6]]
    food_number = len(food_pos)

    wall_pos = [[7,5],[4,2],[3,2],[5,2],[3,1],[3,0],[5,1]]

    map_dimension = global_map.map_dimension()

    # initialize pacman and monster locations
    
    pman = Pacman([4,4],5,map_dimension,food_number,game_level)
    

    monster1 = Monster([0,0],5,map_dimension,game_level)
    monster2 = Monster([4,3],5,map_dimension,game_level)
    monster3 = Monster([6,7],5,map_dimension,game_level)

    agents = [pman,monster2,monster1,monster3]

    
    # add agents into the map
    global_map.load_agents(agents)
    # add food into the map
    global_map.load_food(food_pos)
    
    # add wall into the map
    global_map.load_wall(wall_pos)
    global_map.map_print()

    state_check(pman, global_map)

    i = 100000 # a variable just to make the loop stop, removing later

    finish = False

    while (True):
        
        
        for a in agents:
            get_legal_actions(a,global_map,game_level)
            # agent moves and global map update it's location
            a.move(global_map)
            
    
        finish = state_check(pman, global_map)
        global_map.map_print()

        if finish:
            print ("The game finish in {} steps".format(100000 - i))
            break

        i = i - 1
        if (i <= 0):
            print("Preemptive to end the game")
            break


    print ("The game finish at level {}".format(game_level))
if __name__ == "__main__":
    main() 