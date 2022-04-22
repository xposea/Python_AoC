if __name__ == '__main__':
    depth, pos = 0, 0
    for line in open("InputFiles/Day2.txt", "r"):
        if line.split(" ")[0] == "forward":
            pos += int(line.split(" ")[1])
        elif line.split(" ")[0] == "up":
            depth -= int(line.split(" ")[1])
        elif line.split(" ")[0] == "down":
            depth += int(line.split(" ")[1])
    print(depth * pos)
