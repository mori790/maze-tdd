import types
import argparse
import re
import builtins
import io
import pytest

from maze.cli import build_parser, GenCommand, SolveCommand

def test_parser_dispatches_to_correct_command_class():
    parser = build_parser()
    args_gen = parser.parse_args(["gen", "--w", "3", "--h", "2", "--seed", "1"])
    assert getattr(args_gen, "_cmd_class") is GenCommand
    
    args_solve = parser.parse_args(["solve", "--w", "3", "--h", "2", "--seed", "1"])
    assert getattr(args_solve, "_cmd_class") is SolveCommand
    
def test_gen_command_prints_ascii(capsys):
    parser = build_parser()
    args = parser.parse_args(["gen", "--w", "3", "--h", "2", "--seed", "1"])
    
    # 実行
    cmd = args._cmd_class()
    cmd.run(args)
    
    out = capsys.readouterr().out
    # 簡易チェック：ASCIIに境界線っぽい文字が含まれる
    assert re.search(f"[+\-|]", out)
    
def test_solve_command_prints_path_and_lenght(capsys):
    parser = build_parser()
    args = parser.parse_args(["solve", "--w", "4", "--h", "3", "--seed", "1"])
    
    cmd = args._cmd_class()
    cmd.run(args)
    
    out = capsys.readouterr().out.lower()
    # パスのオーバレイと長さが出る想定
    assert "path length:" in out

def test_gen_same_seed_produces_same_outputI(capsys):
    # Arrange
    parser = build_parser()
    args1 = parser.parse_args(["gen", "--w", "3", "--h", "2", "--seed", "1"])
    args2 = parser.parse_args(["gen", "--w", "3", "--h", "2", "--seed", "1"])
    
    # Act
    cmd1 = args1._cmd_class()
    cmd1.run(args1)
    out1 = capsys.readouterr().out
    cmd2 = args2._cmd_class()
    cmd2.run(args2)
    out2 = capsys.readouterr().out
    
    # Assert
    assert out1 == out2