class MoveError(Exception):
    def __init__(self, tile: int, direction: str) -> None:
        super().__init__(f"Failed to move tile {tile} {direction}")
