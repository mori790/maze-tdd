import random
from typing import Tuple

from maze.core import Maze

OPPOSITE = {"N":"S", "S":"N", "E":"W", "W":"E"}
DIRS = {
    "N": (0, -1),
    "S": (0, 1),
    "W": (-1, 0),
    "E": (1, 0)
}

# 範囲内か確認
def in_bounds(m: Maze, x: int, y: int) -> bool:
    return 0 <= x < m.width and 0 <= y < m.height

class RecursiveBacktracker:
    def __init__(self, seed: int | None = None):
        self.rng = random.Random(seed)
    
    def generate(self, m: Maze, start: Tuple[int, int] = (0,0)):
        stack = [start]
        visited = {start}
        while stack:
            # 末尾取り出し
            x, y = stack[-1]
            # 未訪問の隣接セル候補
            candidates = []
            for d, (dx, dy) in DIRS.items():
                nx, ny = x+dx, y+dy
                if in_bounds(m, nx, ny) and (nx, ny) not in visited:
                    candidates.append((d, nx, ny))
            if not candidates:
                stack.pop()
                continue
            d, nx, ny = self.rng.choice(candidates)
            # 壁を壊す
            m.cell(x, y).walls.discard(d)
            m.cell(nx, ny).walls.discard(OPPOSITE[d])
            visited.add((nx, ny))
            stack.append((nx, ny))
                