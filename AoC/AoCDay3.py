def part_one() -> int:
    gamma, epsilon = "", ""
    for i in range(len(numbers[0])):
        count = sum(
            s[i] == '1'
            for s in numbers
        )
        if count > len(numbers) / 2:
            gamma += str(1)
            epsilon += str(0)
        else:
            gamma += str(0)
            epsilon += str(1)
    return int(gamma, 2) * int(epsilon, 2)


def part_two() -> int:
    oxygen, carbon = "", ""
    for i in range(len(numbers[0])):
        oxy, car, oxy_count, car_count = 0, 0, 0, 0
        for s in numbers:
            if s.startswith(oxygen):
                oxy_count += 1
                if s.replace(oxygen, '', 1).startswith("1"):
                    oxy += 1
            if s.startswith(carbon):
                car_count += 1
                if s.replace(carbon, '', 1).startswith("1"):
                    car += 1
        if oxy >= oxy_count/2:
            oxygen += "1"
        else:
            oxygen += "0"
        if car_count == 1:
            for s in numbers:
                if s.startswith(carbon):
                    carbon = s
        elif car >= car_count/2:
            carbon += "0"
        else:
            carbon += "1"
    print(oxygen, carbon)
    return int(oxygen, 2) * int(carbon, 2)


if __name__ == '__main__':
    file = open("/Users/dylan/Library/CloudStorage/Box-Box/My Box Notes/Python/InputFiles/Day3.txt", "r")
    numbers = [line.strip() for line in file]
    print(part_one())
    print(part_two())
