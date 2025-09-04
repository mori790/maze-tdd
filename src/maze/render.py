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
