def part_one(inputs) -> int:
    count = sum(
        inputs[i] > inputs[i - 1]
        for i in range(1, len(inputs))
    )
    return count


def part_two(inputs) -> int:
    count = sum(
        inputs[i] > inputs[i - 3]
        for i in range(3, len(inputs))
    )
    return count


if __name__ == '__main__':
    numbers = [int(line) for line in open("InputFiles/Day1.txt", "r")]
    print(part_one(numbers))
    print(part_two(numbers))

