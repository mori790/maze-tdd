import argparse
from abc import ABC, abstractmethod
from typing import Dict, Type

from .core import Maze
from .gen import RecursiveBacktracker
from .solve import BFSSolver
from .render import render_ascii, render_with_path
from .pgview import run as view_run

def add_common_size_seed(p: argparse.ArgumentParser) -> None:
    p.add_argument("--w", type=int, required=True)
    p.add_argument("--h", type=int, required=True)
    p.add_argument("--seed", type=int, default=0)
    
class Command(ABC):
    name: str
    help: str
    
    @classmethod
    @abstractmethod
    def add_arguments(cls, subparser: argparse.ArgumentParser) -> None:
        ...
        
    @abstractmethod
    def run(self, args: argparse.Namespace) -> None:
        ...
    
class GenCommand(Command):
    name = "gen"
    help = "Generate a maze print as ASCII"
    
    @classmethod
    def add_arguments(cls, p: argparse.ArgumentParser) -> None:
        add_common_size_seed(p)

    def run(self, args: argparse.Namespace) -> None:
        m = Maze(args.w, args.h)
        RecursiveBacktracker(seed=args.seed).generate(m)
        print(render_ascii(m))

class SolveCommand(Command):
    name = "solve"
    help = "Generate & solve a maze, then print path overlay and length"
    
    @classmethod
    def add_arguments(cls, p: argparse.ArgumentParser) -> None:
        add_common_size_seed(p)
        p.add_argument("--sx", type=int, default=0)
        p.add_argument("--sy", type=int, default=0)
        p.add_argument("--gx", type=int, default=None)
        p.add_argument("--gy", type=int, default=None)
    
    def run(self, args: argparse.Namespace) -> None:
        m = Maze(args.w, args.h)
        RecursiveBacktracker(seed=args.seed).generate(m)
        gx = args.gx if args.gx is not None else args.w-1
        gy = args.gy if args.gy is not None else args.h-1
        path = BFSSolver().solve(m, (args.sx, args.sy), (gx, gy))
        print(render_with_path(m, path))
        print(f"Path length: {len(path)}")

class ViewCommand(Command):
    name = "view"
    help = "Open interactive viewer (pygame/pg)."

    @classmethod
    def add_arguments(cls, p: argparse.ArgumentParser) -> None:
        add_common_size_seed(p)
        p.add_argument("--cell", type=int, default=32)

    def run(self, args: argparse.Namespace) -> None:
        view_run(width=args.w, height=args.h, seed=args.seed, cell=args.cell)

COMMANDS: Dict[str, Type[Command]] = {
    GenCommand.name: GenCommand,
    SolveCommand.name: SolveCommand,
    ViewCommand.name: ViewCommand,
}

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="maze")
    sub = parser.add_subparsers(dest="cmd", required=True)
    
    # コマンドに自分の引数登録
    for name, Cmd in COMMANDS.items():
        sp = sub.add_parser(name, help=Cmd.help)
        Cmd.add_arguments(sp)
        # 実行時に使うクラス参照を紐づけておく
        sp.set_defaults(_cmd_class=Cmd)
    
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    # クラスを取り出してインスタンス化 からの実行
    cmd_class: Type[Command] = getattr(args, "_cmd_class")
    cmd_class().run(args)


if __name__ == "__main__":
    main()
