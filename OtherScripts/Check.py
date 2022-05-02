from collections import defaultdict
from typing import List


def create_adjacency_dict(d: dict, board: List[List[str]]) -> dict:
    for row_num, row in enumerate(board):
        for col_num, col in enumerate(row):
            d[row_num, col_num] = surrounding_index(row_num, col_num)
    return d


def surrounding_index(row_num: int, col_num: int, board) -> list:
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


def recursive_check(word: str, index: int, d: dict, path: set, row_num, col_num, board) -> bool:
    if index == len(word):
        return True
    for point in d[row_num, col_num]:
        if board[point[0]][point[1]] == word[index]:
            spot = list(d.keys()).index((point[0], point[1]))
            if spot not in path:
                path.add(spot)
                return recursive_check(word, index + 1, d, path, point[0], point[1], board)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        d = create_adjacency_dict(defaultdict(str), board)
        for index, point in enumerate(d):
            for word in words:
                if board[point[0]][point[1]] == word[0]:
                    if recursive_check(word, 1, d, {index}, point[0], point[1], board):
                        if word not in ans:
                            ans.append(word)
        return ans
