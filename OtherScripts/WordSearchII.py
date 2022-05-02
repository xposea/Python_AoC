from __future__ import annotations

from collections import defaultdict
from typing import List


def find_words(board: List[List[str]], words: List[str]):
    ans = []  # Misread the problem slightly, but this does act as a regular word search finder
    horiz = []
    vert = [""] * len(board)
    for row in board:
        word = ""
        for index, letter in enumerate(row):
            word += letter
            vert[index] += letter
        horiz.append(word)
    for line in set(horiz + vert):
        for single in words:
            if single in line or single[::-1] in line:
                ans.append(single)
    return ans


def create_adjacency_dict(d: dict, board: List[List[str]]) -> dict:
    for row_num, row in enumerate(board):
        for col_num, col in enumerate(row):
            d[row_num, col_num] = surrounding_index(row_num, col_num)
    return d


def surrounding_index(row_num: int, col_num: int) -> list:
    ans = []
    if row_num - 1 >= 0:
        ans.append([row_num - 1, col_num])
    if row_num + 1 < len(board):
        ans.append([row_num + 1, col_num])
    if col_num - 1 >= 0:
        ans.append([row_num, col_num - 1])
    if col_num + 1 < len(board[0]):
        ans.append([row_num, col_num + 1])
    return ans


def recursive_check(word: str, index: int, d: dict, path: set, row_num, col_num) -> bool:
    if index == len(word):
        return True
    for point in d[row_num, col_num]:
        if board[point[0]][point[1]] == word[index]:
            spot = list(d.keys()).index((point[0], point[1]))
            if spot not in path:
                path.add(spot)
                if recursive_check(word, index + 1, d, set(path), point[0], point[1]):
                    return True
                else:
                    path.discard(spot)


if __name__ == '__main__':
    ans = []
    board = [["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]]
    words = ["eaafgdcba", "eaabcdgfa"]
    d = create_adjacency_dict(defaultdict(str), board)
    nd = defaultdict(list)
    for index, point in enumerate(d):
        nd[board[point[0]][point[1]]].append(point)

    for word in words:
        for index, point in enumerate(nd[word[0]]):
            print(point)
            if recursive_check(word, 1, d, {list(d.keys()).index((point[0], point[1]))}, point[0], point[1]):
                if word not in ans:
                    ans.append(word)
    print(ans)
