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
