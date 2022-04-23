def fibonacci(index: int, memo) -> int:
    if index == 1:
        return 1
    if index == 0:
        return 0
    if index in memo:
        return memo.get(index)
    memo[index] = fibonacci(index - 1, memo) + fibonacci(index - 2, memo)
    return memo.get(index)


if __name__ == '__main__':
    d = {}
    print(fibonacci(998, d))
