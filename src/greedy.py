import itertools

from src.const import (
    X, Y,
    E, N, W, S,
    LOOP, CONFIG,
)


def check_index_error(x, y):
    if 0 <= x < X and 0 <= y < Y:
        return True

    return False


def check_both_size(x, y, board, cfg, cnt):
    if cnt >= cfg[0]:
        if cfg[2]:
            if check_index_error(x, y):
                return board[y][x] is None
            return False
        return True

    return False


def n_search(x, y, board, cfg):
    cnt = 1
    flag = True
    flag_y, flag_x = None, None
    for yy in range(y - 1, -2, -1):
        if check_index_error(x, yy):
            if board[yy][x] == cfg[1]:
                cnt += 1
                continue
            # 2-1, 3-1, 2-2の場合を考慮する
            elif board[yy][x] is None and flag and cfg[3]:
                flag = False
                flag_y, flag_x = yy, x
                continue
        break

    return flag_x, flag_y, check_both_size(x, yy, board, cfg, cnt)


def ne_search(x, y, board, cfg):
    cnt = 1
    flag = True
    flag_y, flag_x = None, None
    for i in range(1, X):
        yy, xx = y - i, x + i
        if check_index_error(xx, yy):
            if board[yy][xx] == cfg[1]:
                cnt += 1
                continue
            # 2-1, 3-1, 2-2の場合を考慮する
            elif board[yy][xx] is None and flag and cfg[3]:
                flag = False
                flag_y, flag_x = yy, xx
                continue
        break

    return flag_x, flag_y, check_both_size(xx, yy, board, cfg, cnt)


def e_search(x, y, board, cfg):
    cnt = 1
    flag = True
    flag_y, flag_x = None, None
    for xx in range(x + 1, X + 2):
        if check_index_error(xx, y):
            if board[y][xx] == cfg[1]:
                cnt += 1
                continue
            # 2-1, 3-1, 2-2の場合を考慮する
            elif board[y][xx] is None and flag and cfg[3]:
                flag = False
                flag_y, flag_x = y, xx
                continue
        break

    return flag_x, flag_y, check_both_size(xx, y, board, cfg, cnt)


def se_search(x, y, board, cfg):
    cnt = 1
    flag = True
    flag_y, flag_x = None, None
    for i in range(1, X):
        yy, xx = y + i, x + i
        if check_index_error(xx, yy):
            if board[yy][xx] == cfg[1]:
                cnt += 1
                continue
            # 2-1, 3-1, 2-2の場合を考慮する
            elif board[yy][xx] is None and flag and cfg[3]:
                flag = False
                flag_y, flag_x = yy, xx
                continue
        break

    return flag_x, flag_y, check_both_size(xx, yy, board, cfg, cnt)


def s_search(x, y, board, cfg):
    cnt = 1
    flag = True
    flag_y, flag_x = None, None
    for yy in range(y + 1, Y + 2):
        if check_index_error(x, yy):
            if board[yy][x] == cfg[1]:
                cnt += 1
                continue
                # 2-1, 3-1, 2-2の場合を考慮する
            elif board[yy][x] is None and flag and cfg[3]:
                flag = False
                flag_y, flag_x = yy, x
                continue
        break

    return flag_x, flag_y, check_both_size(x, yy, board, cfg, cnt)


def sw_search(x, y, board, cfg):
    cnt = 1
    flag = True
    flag_y, flag_x = None, None
    for i in range(1, X):
        yy, xx = y + i, x - i
        if check_index_error(xx, yy):
            if board[yy][xx] == cfg[1]:
                cnt += 1
                continue
            # 2-1, 3-1, 2-2の場合を考慮する
            elif board[yy][xx] is None and flag and cfg[3]:
                flag = False
                flag_y, flag_x = yy, xx
                continue
        break

    return flag_x, flag_y, check_both_size(xx, yy, board, cfg, cnt)


def w_search(x, y, board, cfg):
    cnt = 1
    flag = True
    flag_y, flag_x = None, None
    for xx in range(x - 1, -2, -1):
        if check_index_error(xx, y):
            if board[y][xx] == cfg[1]:
                cnt += 1
                continue
            # 2-1, 3-1, 2-2の場合を考慮する
            elif board[y][xx] is None and flag and cfg[3]:
                flag = False
                flag_y, flag_x = y, xx
                continue
        break

    return flag_x, flag_y, check_both_size(xx, y, board, cfg, cnt)


def nw_search(x, y, board, cfg):
    cnt = 1
    flag = True
    flag_y, flag_x = None, None
    for i in range(1, X):
        yy, xx = y - i, x - i
        if check_index_error(xx, yy):
            if board[yy][xx] == cfg[1]:
                cnt += 1
                continue
            # 2-1, 3-1, 2-2の場合を考慮する
            elif board[yy][xx] is None and flag and cfg[3]:
                flag = False
                flag_y, flag_x = yy, xx
                continue
        break

    return flag_x, flag_y, check_both_size(xx, yy, board, cfg, cnt)


def all_check(x, y, board, cfg):
    # 上方向
    xx, yy, flag = n_search(x, y, board, cfg)
    if flag:
        if xx is not None:
            return xx, yy
        else:
            return x, y
    # 右上方向
    xx, yy, flag = ne_search(x, y, board, cfg)
    if flag:
        if xx is not None:
            return xx, yy
        else:
            return x, y
    # 右方向
    xx, yy, flag = e_search(x, y, board, cfg)
    if flag:
        if xx is not None:
            return xx, yy
        else:
            return x, y
    # 右下方向
    xx, yy, flag = se_search(x, y, board, cfg)
    if flag:
        if xx is not None:
            return xx, yy
        else:
            return x, y
    # 下方向
    xx, yy, flag = s_search(x, y, board, cfg)
    if flag:
        if xx is not None:
            return xx, yy
        else:
            return x, y
    # 左下方向
    xx, yy, flag = sw_search(x, y, board, cfg)
    if flag:
        if xx is not None:
            return xx, yy
        else:
            return x, y
    # 左方向
    xx, yy, flag = w_search(x, y, board, cfg)
    if flag:
        if xx is not None:
            return xx, yy
        else:
            return x, y
    # 左上方向
    xx, yy, flag = nw_search(x, y, board, cfg)
    if flag:
        if xx is not None:
            return xx, yy
        else:
            return x, y
    return None, None


def run(json):
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
            if json[y][x] is None:
                xx, yy = all_check(x, y, json, cfg)
                if xx is not None:
                    return xx, yy
            # 次の設定
            step += 1
            x += dx
            y += dy
