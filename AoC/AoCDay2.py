def part_one() -> int:
    depth, pos = 0, 0
    for line in open("/Users/dylan/Library/CloudStorage/Box-Box/My Box Notes/Python/InputFiles/Day2.txt", "r"):
        text, num = line.split()
        if text == "forward":
            pos += int(num)
        elif text == "up":
            depth -= int(num)
        elif text == "down":
            depth += int(num)
    return depth * pos


def part_two() -> int:
    depth, pos, aim = 0, 0, 0
    for line in open("/Users/dylan/Library/CloudStorage/Box-Box/My Box Notes/Python/InputFiles/Day2.txt", "r"):
        text, num = line.split()
        if text == "forward":
            pos += int(num)
            depth += aim * int(num)
        elif text == "up":
            aim -= int(num)
        elif text == "down":
            aim += int(num)
    return depth * pos


if __name__ == '__main__':
    print(part_one())
    print(part_two())