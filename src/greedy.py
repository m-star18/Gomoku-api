import itertools

from const import (
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
