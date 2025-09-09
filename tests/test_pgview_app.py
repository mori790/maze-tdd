import os
import pygame
import pytest

from maze.pgview import MazeViewerApp, MazeGenerator, MazePathSolver

# ---- フェイクのStrategy ----
class FakeGen(MazeGenerator):
    def __init__(self):
        self.generate_calls = 0
        self.last_set_seed = None

    def set_seed(self, seed):
        self.last_set_seed = seed

    def generate(self, maze):
        # 実際には何もしない（呼ばれた回数を数えるだけ）
        self.generate_calls += 1

class FakeSolver(MazePathSolver):
    def __init__(self):
        self.solve_calls = 0
        self.last_args = None

    def solve(self, maze, start, goal):
        self.solve_calls += 1
        self.last_args = (start, goal)
        # 小さな固定パス（2x1 でも成立するように）
        return [(0, 0), (1, 0)]


@pytest.fixture(autouse=True)
def _headless_pygame(monkeypatch):
    # ヘッドレス環境で動かすための設定
    monkeypatch.setenv("SDL_VIDEODRIVER", "dummy")
    monkeypatch.setenv("SDL_AUDIODRIVER", "dummy")
    yield
    # 念のため終了
    try:
        pygame.quit()
    except Exception:
        pass


def test_app_initial_generation_and_path_computation():
    gen = FakeGen()
    solver = FakeSolver()

    app = MazeViewerApp(width=2, height=1, seed=3, cell=8,
                        generator=gen, solver=solver, show_path=True)

    # 初期生成が1回行われ、seedが伝播している
    assert gen.generate_calls == 1
    assert gen.last_set_seed == 3

    # パス計算も行われている
    assert solver.solve_calls == 1
    assert app.path  # 非空


def test_toggle_path_with_key_p():
    gen = FakeGen()
    solver = FakeSolver()
    app = MazeViewerApp(width=2, height=1, seed=0, cell=8,
                        generator=gen, solver=solver, show_path=True)

    # 初期状態: show_path True
    assert app.show_path is True
    initial_solve_calls = solver.solve_calls

    # Pキーでトグル → False になり、再計算不要
    app._handle_keydown(pygame.K_p)
    assert app.show_path is False
    assert solver.solve_calls == initial_solve_calls  # 呼ばれていない（パス消すだけ）

    # 再度P → Trueに戻り、パス再計算
    app._handle_keydown(pygame.K_p)
    assert app.show_path is True
    assert solver.solve_calls == initial_solve_calls + 1


def test_seed_increment_and_regen_on_plus_and_r():
    gen = FakeGen()
    solver = FakeSolver()
    app = MazeViewerApp(width=2, height=1, seed=10, cell=8,
                        generator=gen, solver=solver, show_path=False)

    # 初期生成1回
    assert gen.generate_calls == 1
    assert gen.last_set_seed == 10

    # '+'（または '='）でseed++ & 再生成
    app._handle_keydown(pygame.K_PLUS)
    assert app.seed == 11
    assert gen.last_set_seed == 11
    assert gen.generate_calls == 2  # 再生成された

    # Rで再生成（seedはそのまま）
    app._handle_keydown(pygame.K_r)
    assert app.seed == 11
    assert gen.last_set_seed == 11
    assert gen.generate_calls == 3  # さらに1回
