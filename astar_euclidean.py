from problem import Problem
import math
import heapq
import copy

# calculate the euclidean distance between two points
def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# find the goal position of a tile with a given value
def find_tile_goal_position(node: Problem, value):
    for i, row in enumerate(node.initial_state):
        for j in range(len(row)):
            if node.goal_state[i][j] == value:
                return i, j

# calculate the euclidean heuristic of a current state
def heuristic(node: Problem):
    h_n = 0
    g_n = node.g_n
    for i, row in enumerate(node.initial_state):
        for j, element in enumerate(row):
            if element == 0:
                continue
            goal_row, goal_col = find_tile_goal_position(node, element)
            h_n += euclidean_distance((i,j), (goal_row, goal_col))
    f_n = g_n + h_n
    return g_n, h_n, f_n

def find_blank_tile(node: Problem):
    for i, row in enumerate(node.initial_state):
        for j, element in enumerate(row):
            if element == 0:
                return i, j

def astar_euclidean(initial: Problem):
    # initialize the problem by adding root node to frontier
    initial.g_n, initial.h_n, initial.f_n = heuristic(initial)
    frontier = [initial] 
    # set of all expanded nodes
    expanded_set = {}
    dupe_state = ""
    for i, row in enumerate(initial.initial_state):
        for j, element in enumerate(row):
            dupe_state += str(element)
    dupe_frontier_states = {dupe_state: 0}
    # max length of queue at any time
    max_queue = 0
    # depth of goal node
    sol_depth = 0

    while(True):
        # if frontier is empty then return failure
        if not frontier:
            return False

        # choose a leaf node and remove it from frontier
        node = copy.deepcopy(heapq.heappop(frontier))
        dupe_state = ""
        for i, row in enumerate(node.initial_state):
            for j, element in enumerate(row):
                dupe_state += str(element)
        del dupe_frontier_states[dupe_state]

        # if node contains goal state then return corresponding solution
        if node.is_done:
            # update solution depth
            sol_depth = node.g_n
            return len(expanded_set), max_queue, sol_depth

        # add node to explored set
        expanded_set[dupe_state] = 0

        # expand chosen node, adding resulting node to frontier
        print("The best state to expand with g(n) = " + str(node.g_n) + " and h(n) = " + str(node.h_n) + " is...\n" + str(node))

        x_blank, y_blank = find_blank_tile(node)
        try:
            move_up = node.move_tile_up(x_blank + 1, y_blank)
            move_up.g_n, move_up.h_n, move_up.f_n = heuristic(move_up)
            dupe_state = ""
            for i, row in enumerate(move_up.initial_state):
                for j, element in enumerate(row):
                    dupe_state += str(element)
            if (dupe_state not in dupe_frontier_states) and (dupe_state not in expanded_set):
                heapq.heappush(frontier, move_up)
                dupe_frontier_states[dupe_state] = 0
        except:
            pass
        try:
            move_down = node.move_tile_down(x_blank - 1, y_blank)
            move_down.g_n, move_down.h_n, move_down.f_n = heuristic(move_down)
            dupe_state = ""
            for i, row in enumerate(move_down.initial_state):
                for j, element in enumerate(row):
                    dupe_state += str(element)
            if (dupe_state not in dupe_frontier_states) and (dupe_state not in expanded_set):
                heapq.heappush(frontier, move_down)
                dupe_frontier_states[dupe_state] = 0            
        except:
            pass
        try:
            move_left = node.move_tile_left(x_blank, y_blank + 1)
            move_left.g_n, move_left.h_n, move_left.f_n = heuristic(move_left)
            dupe_state = ""
            for i, row in enumerate(move_left.initial_state):
                for j, element in enumerate(row):
                    dupe_state += str(element)
            if (dupe_state not in dupe_frontier_states) and (dupe_state not in expanded_set):
                heapq.heappush(frontier, move_left)
                dupe_frontier_states[dupe_state] = 0
        except:
            pass
        try:
            move_right = node.move_tile_right(x_blank, y_blank - 1)
            move_right.g_n, move_right.h_n, move_right.f_n = heuristic(move_right)
            dupe_state = ""
            for i, row in enumerate(move_right.initial_state):
                for j, element in enumerate(row):
                    dupe_state += str(element)
            if (dupe_state not in dupe_frontier_states) and (dupe_state not in expanded_set):
                heapq.heappush(frontier, move_right)
                dupe_frontier_states[dupe_state] = 0
        except:
            pass

        # check for queue max length
        max_queue = max(max_queue, len(frontier))
