from dataclasses import dataclass

@dataclass
class Cell:
    x: int
    y: int
    walls: set

class Maze:
    def __init__(self, width: int, height: int):
        assert width > 0 and height > 0
        self.width = width
        self.height = height
        self._grid = [
            [Cell(x, y, {"N","E","S","W"}) for x in range(width)]
            for y in range(height)
        ]
        
    def cell(self, x: int, y: int) -> Cell:
        return self._grid[y][x]