#!/usr/local/bin/python3.7

from pacman import *
from monster import *
from game_map import*
from misc import *

import sys


symbol = Symbol()


def get_legal_actions(agent, Map):
    #Don't let the agent move out side the map or to go through wall
    x = agent.location[0]
    y = agent.location[1]

    #reset the legal actions before striping the illegal
    agent.legal_actions = ["up","left","down","right","still"]
    if (x > 0):
        if (Map.data[y][x-1] == Map.symbol.wall):
            agent.remove_actions("left")
    else:
        agent.remove_actions("left")

    if (x < Map.width -1):
        if (Map.data[y][x+1] == Map.symbol.wall):
            agent.remove_actions("right")

    else:
        agent.remove_actions("right")

    if (y > 0):
        if (Map.data[y-1][x] == Map.symbol.wall):
            agent.remove_actions("up")
            
    else:
        agent.remove_actions("up")

    if (y < Map.height - 1):
        if (Map.data[y+1][x] == Map.symbol.wall):
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

def main():
    #generate maps
    #generate agents location


    # define a 8 X 8 map
    global_map = Map(8, 8)

    food_pos = [[7,4],[3,3]]
    food_number = len(food_pos)

    map_dimension = global_map.map_dimension()

# initialize pacman and monster locations
    pman = Pacman([4,4],5,map_dimension,food_number)
    monster1 = Monster([1,1],5,map_dimension)

    agents = [pman, monster1]

    
    # add agents into the map
    global_map.load_agents(agents)
    # add food into the map
    global_map.load_food(food_pos)
    
    global_map.map_print()

    state_check(pman, global_map)

    i = 100 # a variable just to make the loop stop, removing later

    finish = False

    while (True):
        
        
        for a in agents:
            get_legal_actions(a,global_map)
            # agent moves and global map update it's location
            a.move(global_map)
            
    
        finish = state_check(pman, global_map)
        global_map.map_print()

        if finish:
            break

        i = i - 1
        if (i <= 0):
            print("Preemptive to end the game")
            break


    print ("The game finish")
if __name__ == "__main__":
    main()