import itertools

from src.greedy.const import (
    X, Y,
    E, N, W, S,
    LOOP, CONFIG,
)
from src.greedy.search import GomokuGreedySearch


def spiral_search(json):
    for cfg in CONFIG:
        # 初期設定
        cycle = itertools.cycle((E, N, W, S))

        x = LOOP
        y = LOOP
        step = 1  # 進んだ距離
        corner = 1  # まがり角の位置
        # 螺旋状に探索する
        for i in range(X * Y):
            # まがり角に到達したら方向転換
            if step >= corner:
                step = 1
                direction = next(cycle)
                dx, dy = direction

                # X方向に進むとき、まがり角が遠くなる
                if direction == E or direction == W:
                    corner += 1

            # 全方向に探索
            # その座標に置けないとき
            gomoku_search = GomokuGreedySearch(x, y, json, cfg)
            if json[y][x] is None:
                xx, yy = gomoku_search.all_check()
                if xx is not None:
                    return xx, yy
            # 次の設定
            step += 1
            x += dx
            y += dy


def run(json):
    # 螺旋状に探索
    spiral_search(json)
