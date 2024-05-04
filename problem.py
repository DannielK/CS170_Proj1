from exceptions import MoveError
import copy


class Problem:
    def __init__(self, initial_state: list[list[int]]) -> None:
        self.initial_state = initial_state
        self.current_state = copy.deepcopy(initial_state)
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    @property
    def is_done(self) -> None:
        return self.current_state == self.goal_state

    @classmethod
    def default(cls) -> None:
        return cls([[1, 2, 3], [4, 8, 0], [7, 6, 5]])

    def __str__(self) -> str:
        return (
            f"<Problem state={self.current_state[0]}\n"
            f"               {self.current_state[1]}\n"
            f"               {self.current_state[2]}>"
        )

    def move_tile_up(self, row: int, col: int) -> bool:
        # Get the tile to move and check if its empty
        tile = self.current_state[row][col]
        if tile == 0:
            raise MoveError(tile, "")

        # We need to make sure that you can move the tile
        # in the given direction so we check if its >= 0
        # and if the new pos is empty
        new_row = row - 1
        if new_row < 0 or self.current_state[new_row][col] != 0:
            raise MoveError(tile, "up")

        # Change the position of the tile
        self.current_state[new_row][col] = self.current_state[row][col]
        self.current_state[row][col] = 0

        return self.current_state == self.goal_state

    def move_tile_down(self, row: int, col: int) -> bool:
        # Get the tile to move and check if its empty
        tile = self.current_state[row][col]

        # We need to make sure that you can move the tile
        # in the given direction so we check if its <= 2
        # and if the new pos is empty
        new_row = row + 1
        if new_row > 2 or self.current_state[new_row][col] != 0:
            raise MoveError(tile, "down")

        # Change the position of the tile
        self.current_state[new_row][col] = tile
        self.current_state[row][col] = 0

        return self.current_state == self.goal_state

    def move_tile_left(self, row: int, col: int) -> bool:
        # Get the tile to move and check if its empty
        tile = self.current_state[row][col]
        if tile == 0:
            raise MoveError(tile, "")

        # We need to make sure that you can move the tile
        # in the given direction so we check if its >= 0
        # and if the new pos is empty
        new_col = col - 1
        if new_col < 0 or self.current_state[row][new_col] != 0:
            raise MoveError(tile, "left")

        # Change the position of the tile
        self.current_state[row][new_col] = tile
        self.current_state[row][col] = 0

        return self.current_state == self.goal_state

    def move_tile_right(self, row: int, col: int) -> bool:
        # Get the tile to move and check if its empty
        tile = self.current_state[row][col]
        if tile == 0:
            raise MoveError(tile, "")

        # We need to make sure that you can move the tile
        # in the given direction so we check if its <= 2
        # and if the new pos is empty
        new_col = col + 1
        if new_col > 2 or self.current_state[row][new_col] != 0:
            raise MoveError(tile, "right")

        # Change the position of the tile
        self.current_state[row][new_col] = tile
        self.current_state[row][col] = 0

        return self.current_state == self.goal_state


if __name__ == "__main__":
    # Test to see if the problem is already complete
    # Should be true
    lst = [[3 * i + y for y in range(1, 4)] for i in range(3)]
    lst[2][2] = 0

    problem = Problem(lst)
    assert problem.is_done == True

    # Test to see if the problem is already complete
    # Should be false
    lst = [[3 * i + y for y in range(1, 4)] for i in range(3)]
    lst[1][2] = 0
    lst[2][2] = 6

    problem = Problem(lst)
    assert problem.is_done == False

    # Test to see if the tile was moved to the correct position and if its done
    assert problem.move_tile_up(2, 2) == True

    assert problem.move_tile_right(2, 1) == False
    assert problem.current_state == [[1, 2, 3], [4, 5, 6], [7, 0, 8]]

    assert problem.move_tile_down(1, 1) == False
    assert problem.current_state == [[1, 2, 3], [4, 0, 6], [7, 5, 8]]

    assert problem.move_tile_left(1, 2) == False
    assert problem.current_state == [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
