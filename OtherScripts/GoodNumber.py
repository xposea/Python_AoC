def rotated_digits(n) -> int:
    count = 0
    for i in range(n + 1):
        for j in str(i):
            if int(j) not in {2, 5, 6, 8}:
                break
        else:
            count += 1
    return count


def rotate_digits(n) -> int:
    return sum(
        int(j) in {2, 5, 6, 8}
        for i in range(n + 1)
        for j in str(i)
    )


if __name__ == '__main__':
    print(rotated_digits(857))
