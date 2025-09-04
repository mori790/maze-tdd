from maze.core import Maze

def test_maze_initializes_with_all_walls():
    m = Maze(3,2) # 横3, 縦2
    assert m.width == 3 and m.height == 2
    for y in range(m.height):
        for x in range(m.width):
            cell = m.cell(x, y)
            # 各セルは４方向全て壁
            assert cell.walls == {"N", "E", "S", "W"}