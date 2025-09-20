# Maze TDD

OOP および TDD の学習目的で作成したプロジェクトです。アイデアやコードは chatGPT を使っています。
大学院入試で勉強してきたアルゴリズムの知識を一部使っています。
テスト駆動開発（TDD）で作成された迷路生成・解法プログラム。Python で実装され、CLI と Pygame を使った GUI 両方で迷路を楽しめます。

動画 URL: https://youtu.be/kXq3WwUxIQE

## 特徴

- **迷路生成**: Recursive Backtracker アルゴリズムによる迷路生成
- **経路探索**: BFS（幅優先探索）と A\*アルゴリズムによる経路探索
- **表示形式**: ASCII 文字による表示と Pygame による視覚的表示
- **CLI 対応**: コマンドラインから簡単操作
- **完全テスト**: TDD による包括的なテストカバレッジ

## インストール

```bash
# リポジトリをクローン
git clone <repository-url>
cd maze-tdd

# 仮想環境を作成・有効化
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# または
.venv\Scripts\activate     # Windows

# 依存関係をインストール
pip install -e .
```

## 使い方

### CLI コマンド

#### 迷路生成

```bash
python -m maze.cli gen --w 10 --h 8 --seed 42
```

#### 迷路解法

```bash
python -m maze.cli solve --w 10 --h 8 --seed 42 --sx 0 --sy 0 --gx 9 --gy 7
```

#### GUI ビューア

```bash
python -m maze.cli view --w 20 --h 12 --seed 42 --cell 32
```

### パラメータ説明

- `--w`: 迷路の幅
- `--h`: 迷路の高さ
- `--seed`: ランダムシード値
- `--sx, --sy`: 開始位置（デフォルト: 0, 0）
- `--gx, --gy`: ゴール位置（デフォルト: 右下）
- `--cell`: セルサイズ（GUI 用、デフォルト: 32）

### GUI 操作

- `R`: 同じシードで迷路を再生成
- `+/-`: シード値を増減
- `P`: 経路表示の ON/OFF
- `Esc`: 終了

## プロジェクト構造

```
src/maze/
├── core.py      # 迷路の基本クラス（Maze, Cell）
├── gen.py       # 迷路生成アルゴリズム
├── solve.py     # 経路探索アルゴリズム（BFS, A*）
├── render.py    # ASCII描画機能
├── pgview.py    # Pygame GUI
└── cli.py       # コマンドライン インターフェース

tests/           # テストファイル
```

## アルゴリズム

### 迷路生成: Recursive Backtracker

- スタックベースの深度優先探索
- 完全な迷路（全ての地点が到達可能）を生成
- シード値による再現可能な生成

### 経路探索

- **BFS**: 最短経路を保証する幅優先探索
- **A\***: マンハッタン距離ヒューリスティック付き最適探索

## テスト実行

```bash
pytest
```

## 開発

このプロジェクトは TDD（テスト駆動開発）で開発されています：

1. 要求を満たすテストケースを最初に作成
2. テストを通すための最小限の実装
3. リファクタリングによる品質向上

テストは以下をカバーしています：

- 迷路生成の正当性
- 経路探索アルゴリズムの正確性
- CLI インターフェースの動作確認
- 描画機能の整合性
