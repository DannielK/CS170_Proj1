from problem import Problem
import copy

def A_star_tile(root: Problem) -> bool:

    frontier = [root] #frontier set to store nodes to be explored
    explored_set = [] #explored set to store explored nodes/states

    while(True):
        #if frontier is empty then there is no solution, return false
        if not frontier: 
            return False
        
        #pick node with lowest cost to move to
        lowest_cost_index = 0
        lowest_cost = total_cost(frontier[0])
        lowest_cost_node = frontier[0]
        for idx, node in enumerate(frontier):
            if total_cost(node) < lowest_cost:
                lowest_cost = total_cost(node)
                lowest_cost_node = node
                lowest_cost_index = idx
        
        explored_node = Problem(lowest_cost_node.initial_state)
        #remove lowest cost node from frontier
        del frontier[lowest_cost_index]

        #add lowest cost node to explored set
        explored_set.append(explored_node)

        print("Best state to expand with the cost of " + str(lowest_cost) + " and a node cost of " + str(lowest_cost_node.cost) +  " is: \n")
        print(lowest_cost_node.__str__())
        print("\n")

        #check if the node's current state is goal state
        if lowest_cost_node.initial_state == lowest_cost_node.goal_state:
            return True

        num_children_created = 0
        #expands node with the different operators
        for x in range(4):
            #expands node by moving tile and returns true if it is a goal state after moving
            new_tiles = lowest_cost_node.initial_state
            chosen_node = Problem(new_tiles)
            chosen_node.cost = lowest_cost_node.cost

            curr_x = 0
            curr_y = 0

            #get current position of blank tile
            for idx1, row in enumerate(chosen_node.initial_state):
                for idx2, element in enumerate(row):
                    if element==0:
                        curr_x = idx1
                        curr_y = idx2

            #checks which operation should be made and if it is a legal move
            legal_move = True
            if x==0:
                try:
                    temp = chosen_node.move_tile_up(curr_x+1, curr_y)
                    num_children_created += 1
                except:
                    legal_move = False
            elif x==1:
                try: 
                    temp = chosen_node.move_tile_down(curr_x-1, curr_y)
                    num_children_created += 1
                except:
                    legal_move = False
            elif x==2:
                try: 
                    temp = chosen_node.move_tile_left(curr_x, curr_y+1)
                    num_children_created += 1
                except:
                    legal_move = False
            elif x==3:
                try:
                    temp = chosen_node.move_tile_right(curr_x, curr_y-1)
                    num_children_created += 1
                except:
                    legal_move = False

            #checks whether the new child node's state already was seen before 
            exists = False
            for to_be_explored in frontier:
                if temp.initial_state == to_be_explored.initial_state:
                    exists = True
            print(str(len(explored_set)))
            for expanded in explored_set:
                if temp.initial_state == expanded.initial_state:
                    exists = True

            #if child node was NOT seen before AND was created from a legal move, add to frontier
            if (not exists) and legal_move:
                if x==0:
                    frontier.append(chosen_node.move_tile_up(curr_x+1, curr_y))
                elif x==1:
                    frontier.append(chosen_node.move_tile_down(curr_x-1, curr_y))
                elif x==2: 
                    frontier.append(chosen_node.move_tile_left(curr_x, curr_y+1))
                elif x==3:
                    frontier.append(chosen_node.move_tile_right(curr_x, curr_y-1))
        print(str(num_children_created) + "\n")  

def total_cost(node: Problem) -> int:

    sum = node.cost

    for idx1, row in enumerate(node.initial_state):
        for idx2, element in enumerate(row):
            if element!=node.goal_state[idx1][idx2]:
                sum = sum + 1
    
    return sum