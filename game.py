#!/usr/local/bin/python3.7

from pacman import *
from monster import *
from game_map import*

def get_legal_actions(agent, Map):
    #Don't let the agent move out side the map or to go through wall
    x = agent.location[0]
    y = agent.location[1]

    #reset the legal actions before striping the illegal
    agent.legal_actions = ["up","left","down","right","still"]
    if (x > 0):
        if (Map.data[y][x-1] == Map.symbol.wall):
            agent.legal_actions.remove("left")
    else:
        agent.legal_actions.remove("left")

    if (x < Map.width -1):
        if (Map.data[y][x+1] == Map.symbol.wall):
            agent.legal_actions.remove("right")

    else:
        agent.legal_actions.remove("right")

    if (y > 0):
        if (Map.data[y-1][x] == Map.symbol.wall):
            agent.legal_actions.remove("up")
            
    else:
        agent.legal_actions.remove("up")

    if (y < Map.height - 1):
        if (Map.data[y+1][x] == Map.symbol.wall):
            agent.legal_actions.remove("down")
    else:
            agent.legal_actions.remove("down")

def main():
    #generate maps
    #generate agents location


    isWin = False
    score = 0

    global_map = Map(8, 8)

# initialize pacman and monster locations
    pman = Pacman([4,4],5,[5,5],0)
    monster1 = Monster([4,4],5,[5,5])

    agents = [pman, monster1]

    global_map.map_print()

    i = 100 # a variable just to make the loop stop, removing later
    while (not isWin):
        for a in agents:
            get_legal_actions(a,global_map)
            a.move(global_map)
        i = i - 1
        print(i)
        if (i <= 0):
            break
        #Map.update
        #Score.update


    print ("The game finish")
if __name__ == "__main__":
    main()