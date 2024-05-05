# import the problem along with the 3 algorithms
from problem import Problem
from uniform_cost import uniform_cost
from astar_misplaced import astar_misplaced
from astar_euclidean import astar_euclidean

# prompt user for the initial state of problem
def custom_puzzle() -> Problem:
    print("Enter your puzzle, use a zero to represent the blank")
    row1 = input("Enter the first row, use a space between numbers    ")
    row2 = input("Enter the second row, use a space between numbers   ")
    row3 = input("Enter the third row, use a space between numbers    ")

    tiles = [list(map(int, row.split(" "))) for row in (row1, row2, row3)]
    return Problem(tiles)

# intro
print("Welcome to group 27's 8 puzzle solver.")

puzzle_type = 0
prompt = "Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n"
while puzzle_type not in {1, 2}:
    try:
        puzzle_type = int(input(prompt))
    except ValueError:
        ...

problem = Problem.default() if puzzle_type == 1 else custom_puzzle()

# list of algorithms
algo_functions = {
    1: uniform_cost,
    2: astar_misplaced,
    3: astar_euclidean
}

# prompt user for which algorithm to run on the problem
algo_choice = 0
prompt = """\nEnter your choice of algorithm
Uniform Cost Search
A* with the Misplaced Tile heuristic.
A* with the Euclidean distance heuristic.\n"""
while algo_choice not in algo_functions:
    print(prompt)
    try:
        algo_choice = int(input())
    except ValueError:
        ...

# run the algorithm and output if there is solution or not
solution = algo_functions[algo_choice](problem)
if solution:
    print("Goal!!!\n\n"
          "To solve this problem the search algorithm expanded a total of " + str(solution[0]) + " nodes.\n"
          "The maximum number of nodes in the queue at any one time: " + str(solution[1]) + ".\n"
          "The depth of the goal node was " + str(solution[2]) + ".\n")
else:
    print("No solution.")