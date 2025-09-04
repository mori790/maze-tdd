from collections import deque
from typing import List, Tuple
from maze.core import Maze

def neighbors(m: Maze, x: int, y:int):
    # 壁が無い方向だけ
    if "N" not in m.cell(x,y).walls and y > 0: yield (x, y-1)
    if "S" not in m.cell(x,y).walls and y < m.height-1: yield (x, y+1)
    if "W" not in m.cell(x,y).walls and x > 0: yield (x-1, y)
    if "E" not in m.cell(x,y).walls and x < m.width-1: yield (x+1, y)
    
class BFSSolver:
    def solve(self, m: Maze, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        sx, sy = start; gx, gy = goal
        q = deque([(sx, sy)])
        prev = { (sx, sy): None }
        while q:
            x, y = q.popleft()
            if (x,y) == (gx, gy):
                # 経路復元
                path = []
                cur = (x, y)
                while cur is not None:
                    path.append(cur)
                    cur = prev[cur]
                return list(reversed(path))
            for nx, ny in neighbors(m, x, y):
                if(nx, ny) not in prev:
                    prev[(nx, ny)] = (x, y)
                    q.append((nx, ny))
        raise ValueError("No path")