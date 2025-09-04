from maze.core import Maze

def render_ascii(m: Maze) -> str:
    # 上枠
    s = " " + "_" * (m.width*2 - 1) + "\n"
    for y in range(m.height):
        row = ["|"]
        for x in range(m.width):
            c = m.cell(x, y)
            floor = "_" if "S" in c.walls else " "
            wallE = "|" if "E" in c.walls else " "
            row.append(floor + wallE)
        s += "".join(row) + "\n"
    return s

def render_with_path(m: Maze, path: list[tuple[int,int]]) -> str:
    marks = {p: "*" for p in path}  # 経路セルをマーキング
    s = " " + "_" * (m.width*2 - 1) + "\n"
    for y in range(m.height):
        row = ["|"]
        for x in range(m.width):
            c = m.cell(x, y)
            mark = marks.get((x, y))
            floor_char = "_" if "S" in c.walls else " "
            cell_char = mark if mark else floor_char
            wallE = "|" if "E" in c.walls else " "
            row.append(cell_char + wallE)
        s += "".join(row) + "\n"
    return s
