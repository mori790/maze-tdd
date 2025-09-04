from maze.core import Maze
from maze.gen import RecursiveBacktracker
from collections import deque

def reachable(m: Maze, start=(0,0), goal=None) -> bool:
    if goal is None:
        goal = (m.width-1, m.height-1)
    sx, sy = start
    gx, gy = goal
    q = deque([(sx, sy)])
    seen = {(sx, sy)}
    while q:
        x, y = q.popleft()
        if (x,y) == (gx, gy):
            return True
        cell = m.cell(x, y)
        # 壁がない方向に進む
        if "N" not in cell.walls and y > 0 and (x, y-1) not in seen:
            seen.add((x, y-1)); q.append((x, y-1))
        if "S" not in cell.walls and y < m.height-1 and (x, y+1) not in seen:
            seen.add((x, y+1)); q.append((x, y+1))
        if "W" not in cell.walls and x > 0 and (x-1, y) not in seen:
            seen.add((x-1, y)); q.append((x-1, y))
        if "E" not in cell.walls and x < m.width-1 and (x+1, y) not in seen:
            seen.add((x+1, y)); q.append((x+1, y))
    return False

def test_recursive_backtracker_makes_path_from_start_to_goal():
    m = Maze(10, 6)
    gen = RecursiveBacktracker(seed=42)
    gen.generate(m, start=(0,0))
    assert reachable(m, start=(0,0), goal=(9,5))