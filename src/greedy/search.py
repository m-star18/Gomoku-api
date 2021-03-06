from src.greedy.const import (
    X, Y,
)


class GomokuGreedySearch:
    """
    五目並べの探索クラス.

    Attributes
    ----------
    x: int
        探索を行うスタート地点のx座標.
    y: int
        探索を行うスタート地点のy座標.
    board: list[list[int]]
        現在の盤面.
    cfg: list[any]
        探索のconfig情報.
    """
    def __init__(self, x, y, board, cfg):
        self.x = x
        self.y = y
        self.board = board
        self.cfg = cfg

    """
    探索が盤面からはみ出してないか判定する.
    
    Parameters
    ----------
    x: int
        対象の盤面のx座標.
    y: int
        対象の盤面のy座標.
    
    Return
    ------
    flag: bool
        探索が盤面からはみ出していないか.
    """
    def check_index_error(self, x, y):
        if 0 <= x < X and 0 <= y < Y:
            return True

        return False

    """
    両面かどうかを判定する.
    
    Parameters
    ----------
    cnt: int
        連結数.
    x: int
        対象の盤面のx座標.
    y: int
        対象の盤面のy座標.
    
    Return
    ------
    flag: bool
        両面かどうか.
    """
    def check_both_size(self, cnt, x, y):
        if cnt >= self.cfg[0]:
            if self.cfg[2]:
                if self.check_index_error(x, y):
                    return self.board[y][x] is None
                return False
            return True

        return False

    """
    上方向に探索する.
    
    Returns
    -------
    flag_x: int or None
        穴あきの部分に置くときのx座標.
    flag_y: int or None
        穴あきの部分に置くときのy座標.
    flag: bool
        両面かどうか.
    """
    def n_search(self):
        cnt = 1
        flag = True
        flag_y, flag_x = None, None
        for yy in range(self.y - 1, -2, -1):
            if self.check_index_error(self.x, yy):
                if self.board[yy][self.x] == self.cfg[1]:
                    cnt += 1
                    continue
                # 2-1, 3-1, 2-2の場合を考慮する
                elif self.board[yy][self.x] is None and flag and self.cfg[3]:
                    flag = False
                    flag_y, flag_x = yy, self.x
                    continue
            break

        return flag_x, flag_y, self.check_both_size(cnt, self.x, yy)

    """
    右上方向に探索する.

    Returns
    -------
    flag_x: int or None
        穴あきの部分に置くときのx座標.
    flag_y: int or None
        穴あきの部分に置くときのy座標.
    flag: bool
        両面かどうか.
    """
    def ne_search(self):
        cnt = 1
        flag = True
        flag_y, flag_x = None, None
        for i in range(1, X):
            yy, xx = self.y - i, self.x + i
            if self.check_index_error(xx, yy):
                if self.board[yy][xx] == self.cfg[1]:
                    cnt += 1
                    continue
                # 2-1, 3-1, 2-2の場合を考慮する
                elif self.board[yy][xx] is None and flag and self.cfg[3]:
                    flag = False
                    flag_y, flag_x = yy, xx
                    continue
            break

        return flag_x, flag_y, self.check_both_size(cnt, xx, yy)

    """
    右方向に探索する.

    Returns
    -------
    flag_x: int or None
        穴あきの部分に置くときのx座標.
    flag_y: int or None
        穴あきの部分に置くときのy座標.
    flag: bool
        両面かどうか.
    """
    def e_search(self):
        cnt = 1
        flag = True
        flag_y, flag_x = None, None
        for xx in range(self.x + 1, X + 2):
            if self.check_index_error(xx, self.y):
                if self.board[self.y][xx] == self.cfg[1]:
                    cnt += 1
                    continue
                # 2-1, 3-1, 2-2の場合を考慮する
                elif self.board[self.y][xx] is None and flag and self.cfg[3]:
                    flag = False
                    flag_y, flag_x = self.y, xx
                    continue
            break

        return flag_x, flag_y, self.check_both_size(cnt, xx, self.y)

    """
    右下方向に探索する.

    Returns
    -------
    flag_x: int or None
        穴あきの部分に置くときのx座標.
    flag_y: int or None
        穴あきの部分に置くときのy座標.
    flag: bool
        両面かどうか.
    """
    def se_search(self):
        cnt = 1
        flag = True
        flag_y, flag_x = None, None
        for i in range(1, X):
            yy, xx = self.y + i, self.x + i
            if self.check_index_error(xx, yy):
                if self.board[yy][xx] == self.cfg[1]:
                    cnt += 1
                    continue
                # 2-1, 3-1, 2-2の場合を考慮する
                elif self.board[yy][xx] is None and flag and self.cfg[3]:
                    flag = False
                    flag_y, flag_x = yy, xx
                    continue
            break

        return flag_x, flag_y, self.check_both_size(cnt, xx, yy)

    """
    下方向に探索する.

    Returns
    -------
    flag_x: int or None
        穴あきの部分に置くときのx座標.
    flag_y: int or None
        穴あきの部分に置くときのy座標.
    flag: bool
        両面かどうか.
    """
    def s_search(self):
        cnt = 1
        flag = True
        flag_y, flag_x = None, None
        for yy in range(self.y + 1, Y + 2):
            if self.check_index_error(self.x, yy):
                if self.board[yy][self.x] == self.cfg[1]:
                    cnt += 1
                    continue
                # 2-1, 3-1, 2-2の場合を考慮する
                elif self.board[yy][self.x] is None and flag and self.cfg[3]:
                    flag = False
                    flag_y, flag_x = yy, self.x
                    continue
            break

        return flag_x, flag_y, self.check_both_size(cnt, self.x, yy)

    """
    左下方向に探索する.

    Returns
    -------
    flag_x: int or None
        穴あきの部分に置くときのx座標.
    flag_y: int or None
        穴あきの部分に置くときのy座標.
    flag: bool
        両面かどうか.
    """
    def sw_search(self):
        cnt = 1
        flag = True
        flag_y, flag_x = None, None
        for i in range(1, X):
            yy, xx = self.y + i, self.x - i
            if self.check_index_error(xx, yy):
                if self.board[yy][xx] == self.cfg[1]:
                    cnt += 1
                    continue
                # 2-1, 3-1, 2-2の場合を考慮する
                elif self.board[yy][xx] is None and flag and self.cfg[3]:
                    flag = False
                    flag_y, flag_x = yy, xx
                    continue
            break

        return flag_x, flag_y, self.check_both_size(cnt, xx, yy)

    """
    左方向に探索する.

    Returns
    -------
    flag_x: int or None
        穴あきの部分に置くときのx座標.
    flag_y: int or None
        穴あきの部分に置くときのy座標.
    flag: bool
        両面かどうか.
    """
    def w_search(self):
        cnt = 1
        flag = True
        flag_y, flag_x = None, None
        for xx in range(self.x - 1, -2, -1):
            if self.check_index_error(xx, self.y):
                if self.board[self.y][xx] == self.cfg[1]:
                    cnt += 1
                    continue
                # 2-1, 3-1, 2-2の場合を考慮する
                elif self.board[self.y][xx] is None and flag and self.cfg[3]:
                    flag = False
                    flag_y, flag_x = self.y, xx
                    continue
            break

        return flag_x, flag_y, self.check_both_size(cnt, xx, self.y)

    """
    左上方向に探索する.

    Returns
    -------
    flag_x: int or None
        穴あきの部分に置くときのx座標.
    flag_y: int or None
        穴あきの部分に置くときのy座標.
    flag: bool
        両面かどうか.
    """
    def nw_search(self):
        cnt = 1
        flag = True
        flag_y, flag_x = None, None
        for i in range(1, X):
            yy, xx = self.y - i, self.x - i
            if self.check_index_error(xx, yy):
                if self.board[yy][xx] == self.cfg[1]:
                    cnt += 1
                    continue
                # 2-1, 3-1, 2-2の場合を考慮する
                elif self.board[yy][xx] is None and flag and self.cfg[3]:
                    flag = False
                    flag_y, flag_x = yy, xx
                    continue
            break

        return flag_x, flag_y, self.check_both_size(cnt, xx, yy)

    """
    全探索.
    
    Returns
    -------
    x: int or None
        次の一手のx座標.
    y: int or None
        次の一手のy座標.
    """
    def all_check(self):
        # 上方向
        xx, yy, flag = self.n_search()
        if flag:
            if xx is not None:
                return xx, yy
            else:
                return self.x, self.y
        # 右上方向
        xx, yy, flag = self.ne_search()
        if flag:
            if xx is not None:
                return xx, yy
            else:
                return self.x, self.y
        # 右方向
        xx, yy, flag = self.e_search()
        if flag:
            if xx is not None:
                return xx, yy
            else:
                return self.x, self.y
        # 右下方向
        xx, yy, flag = self.se_search()
        if flag:
            if xx is not None:
                return xx, yy
            else:
                return self.x, self.y
        # 下方向
        xx, yy, flag = self.s_search()
        if flag:
            if xx is not None:
                return xx, yy
            else:
                return self.x, self.y
        # 左下方向
        xx, yy, flag = self.sw_search()
        if flag:
            if xx is not None:
                return xx, yy
            else:
                return self.x, self.y
        # 左方向
        xx, yy, flag = self.w_search()
        if flag:
            if xx is not None:
                return xx, yy
            else:
                return self.x, self.y
        # 左上方向
        xx, yy, flag = self.nw_search()
        if flag:
            if xx is not None:
                return xx, yy
            else:
                return self.x, self.y
        return None, None
