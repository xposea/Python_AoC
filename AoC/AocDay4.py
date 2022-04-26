from __future__ import annotations
from typing import NamedTuple


class Board(NamedTuple):
    remaining: set[int]
    ints: list[int]

    @classmethod
    def read_input(cls, board: str) -> Board:
        ints = [int(s) for s in board.split()]
        remaining = set(ints)
        return cls(remaining, ints)

    @property
    def board_won(self) -> bool:
        for i in range(5):
            for j in range(5):
                if self.ints[i * 5 + j] in self.remaining:
                    break
            else:
                return True
            for j in range(5):
                if self.ints[i + 5 * j] in self.remaining:
                    break
            else:
                return True
        return False


def play_ball() -> int:
    for i in bingo_balls:
        for board in boards:
            board.remaining.discard(i)
            if board.board_won:
                return sum(board.remaining) * i
    else:
        raise AssertionError('Failed to win')


def play_until_last() -> int:
    non_winner = set([int(i) for i in range(len(boards))])
    for ball in bingo_balls:
        for index, board in enumerate(boards):
            board.remaining.discard(ball)
            if board.board_won:
                non_winner.discard(index)
                if len(non_winner) == 0:
                    return sum(board.remaining) * ball
    else:
        raise AssertionError('Failed to win')


if __name__ == '__main__':
    file = open("/Users/dylan/Library/CloudStorage/Box-Box/My Box Notes/Python/InputFiles/Day4.txt", "r")
    bingo_balls, *rest = file.read().split("\n\n")
    boards = [Board.read_input(board) for board in rest]
    bingo_balls = [int(num) for num in bingo_balls.split(',')]
    print(play_ball())
    print(play_until_last())
