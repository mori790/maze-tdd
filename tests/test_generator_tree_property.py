from maze.core import Maze
from maze.gen import RecursiveBacktracker

def count_removed_walls(m: Maze) -> int:
    # 壁の消失を通路本数に換算
    total_missing = 0
    for y in range(m.height):
        for x in range(m.width):
            c = m.cell(x,y)
            total_missing += 4 - len(c.walls)
    # 双方向だから2で割る
    return total_missing // 2

def test_generated_maze_is_a_tree():
    W, H = 12, 7
    m = Maze(W, H)
    RecursiveBacktracker(seed=123).generate(m)
    edges = count_removed_walls(m)
    assert edges == W*H - 1