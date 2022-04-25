from typing import List


def sort3(a: int, b: int, c: int) -> List[int]:
    return sorted((a, b, c))


if __name__ == '__main__':
    print(sort3(5, 6, 2))
