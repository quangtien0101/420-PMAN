#!/usr/local/bin/python3.7

from pacman import *
from monster import *
from game_map import*
from misc import *

symbol = Symbol()
isWin = False
game_over = False
food_number = 1

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
        if result == "win":
            isWin = True

    # there is a monster at pacman's current location
    if (symbol.monster in global_map.data[y][x]):
        game_over = True

def main():
    #generate maps
    #generate agents location


    score = 0

    global_map = Map(8, 8)

# initialize pacman and monster locations
    pman = Pacman([4,4],5,[5,5],food_number)
    monster1 = Monster([4,4],5,[5,5])

    agents = [pman, monster1]

    global_map.map_print()

    state_check(pman, global_map)

    i = 100 # a variable just to make the loop stop, removing later

    while (not isWin or not game_over):
        

        for a in agents:
            get_legal_actions(a,global_map)
            # agent moves and global map update it's location
            a.move(global_map)
        
        state_check(pman, global_map)

        global_map.map_print()
        
        i = i - 1
        print(i)
        if (i <= 0):
            break
        #Map.update
        #Score.update


    print ("The game finish")
if __name__ == "__main__":
    main()