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

    def move_tile_up(self, pos_x: int, pos_y: int) -> bool:
        tile = self.current_state[pos_x][pos_y]

        # We need to make sure that you can move the tile
        # in the given direction so we check if its >= 0
        # and if the new pos is empty
        new_x = pos_x - 1
        if new_x < 0:
            raise MoveError(tile, "up")

        if self.current_state[new_x][pos_y] != 0:
            raise MoveError(tile, "up")

        # Change the position of the tile
        self.current_state[new_x][pos_y] = self.current_state[pos_x][pos_y]
        self.current_state[pos_x][pos_y] = 0

        return self.current_state == self.goal_state

    def move_tile_down(self, pos_x: int, pos_y: int) -> bool:
        tile = self.current_state[pos_x][pos_y]

        # We need to make sure that you can move the tile
        # in the given direction so we check if its <= 2
        # and if the new pos is empty
        new_x = pos_x + 1
        if new_x > 2:
            raise MoveError(tile, "down")

        if self.current_state[new_x][pos_y] != 0:
            raise MoveError(tile, "down")

        # Change the position of the tile
        self.current_state[new_x][pos_y] = tile
        self.current_state[pos_x][pos_y] = 0

        return self.current_state == self.goal_state

    def move_tile_left(self, pos_x: int, pos_y: int) -> bool:
        tile = self.current_state[pos_x][pos_y]

        # We need to make sure that you can move the tile
        # in the given direction so we check if its >= 0
        # and if the new pos is empty
        new_y = pos_y - 1
        if new_y < 0:
            raise MoveError(tile, "left")

        if self.current_state[pos_x][new_y] != 0:
            raise MoveError(tile, "left")

        # Change the position of the tile
        self.current_state[pos_x][new_y] = tile
        self.current_state[pos_x][pos_y] = 0

        return self.current_state == self.goal_state

    def move_tile_right(self, pos_x: int, pos_y: int) -> bool:
        tile = self.current_state[pos_x][pos_y]

        # We need to make sure that you can move the tile
        # in the given direction so we check if its <= 2
        # and if the new pos is empty
        new_y = pos_y + 1
        if new_y > 2:
            raise MoveError(tile, "down")

        if self.current_state[pos_x][new_y] != 0:
            raise MoveError(tile, "down")

        # Change the position of the tile
        self.current_state[pos_x][new_y] = tile
        self.current_state[pos_x][pos_y] = 0

        return self.current_state == self.goal_state


if __name__ == "__main__":
    problem = Problem([[3 * i + y for y in range(1, 4)] for i in range(3)])
    print(problem.initial_state, problem.is_done)
