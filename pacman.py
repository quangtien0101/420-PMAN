#!/usr/local/bin/python3 
from misc import *
from game_map import *

from random import seed
from random import randint

class Pacman:
    def __init__ (self, location, view, map_dimension, food):
        self.location = location # a list [x,y], pacman current location
        self.food = food # an int, the total number of food, map provided
        self.view = view # an interger 5
        #Pac man has it's own map to calculate and stores the manhattan distance
        self.manhattan_distance = Map(map_dimension[0], map_dimension[1])

        #Pacman personal map since it can't see the whole world
        self.map = Map(map_dimension[0], map_dimension[1])
        self.legal_actions = ["up","down","left","right","still"]        
        
        self.symbol = Symbol()

        # this will be the goals that pacman will try to reach in order to scan the map
        self.goals_pos = self.generate_goal_possitions_for_map_scanning()
        self.map_scaned = False # this indicate wether if pacman has learn about the whole map

        self.food_pos = [] #this contains the list of food locations that pacman need to reach

    def update(self, new_location):
        self.location = copy.deepcopy(new_location)

    def remove_actions(self, direction):        
        try:
            self.legal_actions.remove(direction)
        except ValueError:
            print ("directions not in current legal actions")


    # sense if there is any monster near pacman (manhattan distance <= 2)
    def monster_sense(self, global_map):
        danger_zone = self.calculate_manhattan_distance(global_map)

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
                self.remove_actions("left")

            if (i[1] > self.locationp[1]): #don't go up
                try:                    
                    self.remove_actions("up")
                except ValueError:
                    pass

            if (i[1] < self.location[1]): #don't go down
                try:                    
                    self.remove_actions("down")
                except ValueError:
                    pass

            if (i[0] > self.location[0]): # don't go right
                try:                    
                    self.remove_actions("right")
                except ValueError:
                    pass
        
        

    # if there's any monster near, prioritize to escape the monster's reach first
    def move(self, global_map):

        optimal_moves = self.search_for_best_move()
        move = []
        # always keep the manhattan distance from the monster at least 2 or more
        monster_in_danger_zone = self.monster_sense(global_map)
        # there is some monster near by
        # escaping first while trying to reach the goal
        if len(monster_in_danger_zone) != 0:
            self.escaping_monster(monster_in_danger_zone)
            # after limiting the legal actions, we can move in the most reasonable direction or standing still if there is no options left
            
        #checking if optimal moves is in legal actions
        for i in optimal_moves:
            if i in self.legal_actions:
                    move.append(i)
            
            # if all optiomal moves is ilegal
        if (len(move) == 0):
            move = copy.deepcopy(self.legal_actions)

            # if there is more than one possible move, random the moves
        
        direction = self.random_move(move)
        x = self.location[0]
        y = self.location[1]
        if ( direction == "left" ):
            new_x = x - 1
            new_location = [new_x, y]

            global_map.update(self.location, new_location, self.symbol.pacman)
            
            return

        if ( direction == "right" ):
            new_x = x + 1  
            new_location = [new_x, y]

            global_map.update(self.location, new_location, self.symbol.pacman)

            return 

        if ( direction == "up" ):
            new_y = y - 1  
            new_location = [x, new_y]

            global_map.update(self.location, new_location, self.symbol.pacman)

            return

        if ( direction == "down" ):
            new_y = y + 1  
            new_location = [x, new_y]

            global_map.update(self.location, new_location, self.symbol.pacman)

            return
        

    # with the current view, calculate the manhattan distance of tiles that packman can currently see
    # also return the danger zone
    # this is tell pacman what's there in it's vicinity
    # including foods, wall, monsters
  
    def calculate_manhattan_distance(self,global_map):
        radius = int (view/2)
        
        #this contains the coordinate of all the titles that has manhattan distance <=2
        danger_zone = []

        for y in range(self.location[1] - radius, self.location[1] + radius +1 ,1):
            if (y<0 or y >= self.map.height):
                continue
            
            for x in range(self.location[0]-radius, self.location[0] +radius + 1, 1):
                if (x<0 or x >= self.map.width) :
                    continue
                self.manhattan_distance.data[y][x] = manhattandistance(self.location, [x,y])
                self.map.data[y][x] = global_map.data[y][x]

                if (manhattandistance(self.location, [x,y]) <= 2):
                    danger_zone.append([x,y])

        return danger_zone
    
    # this is tell pacman what's there in it's vicinity
    # including foods, wall, monsters
  
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
        # moving to the nearest food or the nearest goal possition
        if (not self.map_scaned): # Map is not fully scanned, continue to scanning
            nearest, distance = self.closet_goal(self.goals_pos)
        
        else: #Map is fully scanned, now it's collecting the foods
            nearest, distance = self.closet_goal(self.food_pos)

        # now looking for possible move to get to the goal
        optimal_moves = []
        if (self.location[0] > nearest[0]): #pacman is currently on the right of it's goal
            optimal_moves.append("left")

        if (self.location[0] < nearest[0]):
            optimal_moves.append["right"]

        if (self.location[1] > nearest[1]):
            optimal_moves.append["down"]

        if (self.location[1] < nearest[1]):
            optimal_moves.append["up"]
        
        return optimal_moves


    # the current location has food
    def eat_food(self):
        self.food = self.food - 1
        if self.food <=0 :
            return self.win_game()                  

        return "NomNom"

    # when pacman has gather all the foods
    def win_game(self):
        dub = "win"
        return dub

    # when the current location has a monster
    def lose_game(self):
        l = "lose"
        return l


    def closet_goal(self, goals): 
        # goals is the list of goals that pacman is trying to reach, either goals_pos or food_pos
        x = self.location[0]
        y = self.location[1]

        minimum = 99999999
        nearest = []
        for l in goals:
            goal_x = l[0]
            goal_y = l[1]
            tmp = manhattandistance([x,y],[goal_x,goal_y])
            if tmp < minimum:
                minimum = tmp
                nearest = copy.deepcopy(l)

        return nearest, minimum

    def random_move(self, move):
        #if there is just one possible move
        if (len(move) == 1):
            return move[0]

        #forcing pacman to move instead of standing still while it's possible
        self.remove_actions("still")

        seed(1)
        value = randint(0,len(move)-1)
        return move[value]