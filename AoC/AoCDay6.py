def count_fish(days: int) -> int:
    fish = [0] * 9
    for number in open("/Users/dylan/Library/CloudStorage/Box-Box/My Box Notes/Python/InputFiles/Day6.txt",
                       "r").readline().split(","):
        fish[int(number)] += 1
    for days in range(days):
        fish.append(0)
        fish[9] = fish[0]
        del fish[0]
        fish[6] += fish[8]
    return sum(fish)


if __name__ == '__main__':
    print(count_fish(80))
    print(count_fish(256))
