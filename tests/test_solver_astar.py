from maze.core import Maze
from maze.gen import RecursiveBacktracker
from maze.solve import AStarSolver, BFSSolver

def test_astar_finds_path_and_is_not_longer_than_bfs():
    m = Maze(20, 12)
    RecursiveBacktracker(seed=99).generate(m)
    start, goal = (0,0), (19,11)
    
    bfs_path = BFSSolver().solve(m, start, goal)
    astar_path = AStarSolver().solve(m, start, goal)
    
    assert astar_path[0] == start and astar_path[-1] == goal
    
    assert len(bfs_path) == len(astar_path)