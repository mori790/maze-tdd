from maze.core import Maze
from maze.gen import RecursiveBacktracker
from maze.solve import BFSSolver
from maze.render import render_with_path

def test_render_marks_path_cells():
    m = Maze(6, 4)
    RecursiveBacktracker(seed=7).generate(m)
    path = BFSSolver().solve(m, (0,0), (5,3))
    art = render_with_path(m, path)
    # 経路を示す '*' などが含まれること
    assert "*" in art
