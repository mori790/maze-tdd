import argparse
from .core import Maze
from .gen import RecursiveBacktracker
from .solve import BFSSolver
from .render import render_ascii, render_with_path
from .pgview import run as view_run

def main():
    parser = argparse.ArgumentParser(prog="maze")
    sub = parser.add_subparsers(dest="cmd", required=True)

    pgen = sub.add_parser("gen")
    pgen.add_argument("--w", type=int, required=True)
    pgen.add_argument("--h", type=int, required=True)
    pgen.add_argument("--seed", type=int, default=0)

    psolve = sub.add_parser("solve")
    psolve.add_argument("--w", type=int, required=True)
    psolve.add_argument("--h", type=int, required=True)
    psolve.add_argument("--seed", type=int, default=0)
    psolve.add_argument("--sx", type=int, default=0)
    psolve.add_argument("--sy", type=int, default=0)
    psolve.add_argument("--gx", type=int, default=None)
    psolve.add_argument("--gy", type=int, default=None)
    
    pview = sub.add_parser("view")
    pview.add_argument("--w", type=int, required=True)
    pview.add_argument("--h", type=int, required=True)
    pview.add_argument("--seed", type=int, default=0)
    pview.add_argument("--cell", type=int, default=32)
    
    args = parser.parse_args()
    if args.cmd == "gen":
        m = Maze(args.w, args.h)
        RecursiveBacktracker(seed=args.seed).generate(m)
        print(render_ascii(m))
    elif args.cmd == "solve":
        m = Maze(args.w, args.h)
        RecursiveBacktracker(seed=args.seed).generate(m)
        gx = args.gx if args.gx is not None else args.w - 1
        gy = args.gy if args.gy is not None else args.h - 1
        path = BFSSolver().solve(m, (args.sx, args.sy), (gx, gy))
        print(render_with_path(m, path))
        print(f"Path length: {len(path)}")
    elif args.cmd == "view":
        view_run(width=args.w, height=args.h, seed=args.seed, cell=args.cell)


if __name__ == "__main__":
    main()
