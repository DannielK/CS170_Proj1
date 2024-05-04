from problem import Problem


def custom_puzzle() -> Problem:
    print("Enter your puzzle, use a zero to represent the blank")
    row1 = input("Enter the first row, use a space between numbers    ")
    row2 = input("Enter the second row, use a space between numbers   ")
    row3 = input("Enter the third row, use a space between numbers    ")

    tiles = [list(map(int, row.split(" "))) for row in (row1, row2, row3)]
    return Problem(tiles)


print("Welcome to XXX (change this to your student ID) 8 puzzle solver.")

puzzle_type = 0
prompt = "Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n"
while puzzle_type not in {1, 2}:
    try:
        puzzle_type = int(input(prompt))
    except ValueError:
        ...

problem = Problem.default() if puzzle_type == 1 else custom_puzzle()

algo_choice = 0
prompt = """\nEnter your choice of algorithm
Uniform Cost Search
A* with the Misplaced Tile heuristic.
A* with the Euclidean distance heuristic.\n"""
while algo_choice not in {1, 2, 3}:
    print(prompt)
    try:
        algo_choice = int(input())
    except ValueError:
        ...
