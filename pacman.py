#!/usr/local/bin/python3 
from misc import *
from game_map import *
class Pacman:
    def __init__ (self, location, view, map_dimension, food):
        self.location = location # a list [x,y], pacman current location
        self.food = food # an int, the total number of food
        self.view = view # an interger 5
        #Pac man has it's own map to calculate and stores the manhattan distance
        self.manhattan_distance = Map(map_dimension[0], map_dimension[1])

        self.map = Map(map_dimension[0], map_dimension[1])
        self.legal_actions = ["up","down","left","right","still"]        
        
        self.symbol = Symbol()

        # this will be the goals that pacman will try to reach in order to scan the map
        goals_pos = self.generate_goal_possitions_for_map_scanning()
        self.map_scaned = False # this indicate wether if pacman has learn about the whole map

    def generate_successor(self):
        
        #calculate the manhattan distance of all the tiles in i's view

        pass


    # sense if there is any monster near pacman (manhattan distance <= 2)
    def monster_sense(self, global_map):
        danger_zone = self.calculate_manhattan_distance()

        monster_location = []
        # now we check if there is any monster in the danger zone
        for i in danger_zone:
            x = i[0]
            y = i[1]

            content = global_map.view_a_possition(i)

            if (content == self.symbol.monster):
                monster_location.append(i)

        return monster_location


    # removing actions that may lead pacman to the monster 
    def escaping_monster(self, monster_list):
        for i in monster_list:
            if (i[0] < self.location[0]): # don't go left
                try:                    
                    self.legal_actions.remove("left")
                except ValueError:
                    pass

            if (i[1] > self.locationp[1]): #don't go up
                try:                    
                    self.legal_actions.remove("up")
                except ValueError:
                    pass

            if (i[1] < self.location[1]): #don't go down
                try:                    
                    self.legal_actions.remove("down")
                except ValueError:
                    pass

            if (i[0] > self.location[0]): # don't go right
                try:                    
                    self.legal_actions.remove("right")
                except ValueError:
                    pass
        
        

    # if there's any monster near, prioritize to escape the monster reach first
    def move(self, global_map):
        # always keep the manhattan distance from the monster at least 2 or more
        monster_in_danger_zone = self.monster_sense(global_map)
        # there is some monster near by
        # escaping first
        if len(monster_in_danger_zone) != 0:
            self.escaping_monster(monster_in_danger_zone)
            # after limiting the legal actions, we can move in the most reasonable direction or standing still if there is no options left
            
            move = self.search_for_best_move()
            return move

        else:
            # continue to scan the map 
            if (self.map_scaned == False):
            
                pass
            #get to the nearest goal
            
            else :
                # move normaly to try to get the food
                pass


    # with the current view, calculate the manhattan distance of tiles that packman can currently see
    def calculate_manhattan_distance(self):
        radius = int (view/2)
        total = view * view  # the maximum number of tiles that pacman can see
        #this contains the coordinate of all the titles that has manhattan distance <=2
        danger_zone = []

        for y in range(self.location[1] - radius, self.location[1] + radius +1 ,1):
            if (y<0 or y >= self.map.height):
                continue
            
            for x in range(self.location[0]-radius, self.location[0] +radius + 1, 1):
                if (x<0 or x >= self.map.width) :
                    continue
                self.manhattan_distance.data[y][x] = manhattandistance(self.location, [x,y])
                if (manhattandistance(self.location, [x,y]) <= 2):
                    danger_zone.append([x,y])

        return danger_zone
    
    def generate_goal_possitions_for_map_scanning(self):
        goals_pos = []
        radius = int(view/2)
        x = 0
        y = 0
        while (x < self.map.width):
            x = x + radius
            if (x >= self.map.width):
                break
            y = 0
            while (y < self.map.height):
                y = y + radius
                if ( y >= self.map.height):
                    break
                goals_pos.append([x,y])


        return goals_pos
        

    # Pacman will try to scan the whole map to know where all the food is
    def map_scanning(self):
        # check if the map of pacman is complete
        x = 1
        for i in self.map.checked:
            if 0 in i:
                x = 0
                break
        if (x == 1):
            return 1 
    

        #start to scan the map
        #pacman will remember everyfood that it's see and store it into it's own map
        #but it has to avoid monster while doing so
        
        
        return 0



    # the search function to find all the best move from the given successor
    def search_for_best_move(self):
        pass

    # the current location has food
    def eat_food(self):
        self.food = self.food - 1                  
        pass

    # when pacman has gather all the foods
    def win_game(self):
        dub = "win"
        return dub

    # when the current location has a monster
    def lose_game(self):
        l = "lose"
        return l



