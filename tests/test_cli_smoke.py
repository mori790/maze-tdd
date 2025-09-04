import subprocess, sys, os

def test_cli_generates_maze_and_solve_smoke():
    # 生成
    r = subprocess.run([sys.executable, "-m", "maze.cli", "gen", "--w", "5", "--h", "4", "--seed", "1"], capture_output=True, text=True)
    assert r.returncode == 0
    # 解く
    r2 = subprocess.run([sys.executable, "-m", "maze.cli", "solve", "--w", "5", "--h", "4", "--seed", "1"], capture_output=True, text=True)
    assert r2.returncode == 0
    assert "path length:" in r2.stdout.lower()
