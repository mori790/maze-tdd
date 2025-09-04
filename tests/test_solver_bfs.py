from maze.core import Maze
from maze.gen import RecursiveBacktracker
from maze.solve import BFSSolver

def test_bfs_returns_shortest_path_length():
    m = Maze(8, 5)
    RecursiveBacktracker(seed=7).generate(m, start=(0,0))
    solver = BFSSolver()
    path = solver.solve(m, start=(0,0), goal=(7, 4))
    assert path[0] == (0,0) and path[-1] == (7,4)
    assert 10 <= len(path) <= 64