import itertools

from src.const import (
    X, Y,
    E, N, W, S,
    LOOP
)


def check_index_error(x, y):
    if 0 <= x < X and 0 <= y < Y:
        return True

    return False


def n_search(x, y, board, flag, color):
    cnt = 1
    for yy in range(y - 1, 0, -1):
        if check_index_error(x, yy):
            if board[yy][x] == color:
                cnt += 1
                continue
        break

    return cnt >= flag


def ne_search(x, y, board, flag, color):
    cnt = 1
    for i in range(1, X):
        yy, xx = y - i, x + i
        if check_index_error(xx, yy):
            if board[yy][xx] == color:
                cnt += 1
                continue
        break

    return cnt >= flag


def e_search(x, y, board, flag, color):
    cnt = 1
    for xx in range(x + 1, X):
        if check_index_error(xx, y):
            if board[y][xx] == color:
                cnt += 1
                continue
        break

    return cnt >= flag


def se_search(x, y, board, flag, color):
    cnt = 1
    for i in range(1, X):
        yy, xx = y + i, x + i
        if check_index_error(xx, yy):
            if board[yy][xx] == color:
                cnt += 1
                continue
        break

    return cnt >= flag


def s_search(x, y, board, flag, color):
    cnt = 1
    for yy in range(y + 1, Y):
        if check_index_error(x, yy):
            if board[yy][x] == color:
                cnt += 1
                continue
        break

    return cnt >= flag


def sw_search(x, y, board, flag, color):
    cnt = 1
    for i in range(1, X):
        yy, xx = y + i, x - i
        if check_index_error(xx, yy):
            if board[yy][xx] == color:
                cnt += 1
                continue
        break

    return cnt >= flag


def w_search(x, y, board, flag, color):
    cnt = 1
    for xx in range(x - 1, 0, -1):
        if check_index_error(xx, y):
            if board[y][xx] == color:
                cnt += 1
                continue
        break

    return cnt >= flag


def nw_search(x, y, board, flag, color):
    cnt = 1
    for i in range(1, X):
        yy, xx = y - i, x - i
        if check_index_error(xx, yy):
            if board[yy][xx] == color:
                cnt += 1
                continue
        break

    return cnt >= flag


def run(json):
    # 優先度, 5つおけるところから順番に
    for flag in range(5, 0, -1):
        # 相手が0, cpuが1
        for color in range(2):
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
                if json[y][x] is None:
                    # 上方向
                    if n_search(x, y, json, flag, color):
                        return x, y
                    # 右上方向
                    if ne_search(x, y, json, flag, color):
                        return x, y
                    # 右方向
                    if e_search(x, y, json, flag, color):
                        return x, y
                    # 右下方向
                    if se_search(x, y, json, flag, color):
                        return x, y
                    # 下方向
                    if s_search(x, y, json, flag, color):
                        return x, y
                    # 左下方向
                    if sw_search(x, y, json, flag, color):
                        return x, y
                    # 左方向
                    if w_search(x, y, json, flag, color):
                        return x, y
                    # 左上方向
                    if nw_search(x, y, json, flag, color):
                        return x, y

                # 次の設定
                step += 1
                x += dx
                y += dy
