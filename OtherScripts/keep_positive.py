def keep_positive(inputs: list) -> list:
    return [abs(i) for i in inputs]


if __name__ == '__main__':
    repeat = True
    while repeat:
        print(keep_positive([int(i) for i in input("Enter whole numbers: ").split()]))
        repeat = False
        try:
            print(keep_positive([int(i) for i in input("Enter whole numbers: ").split()]))
            repeat = False
        except ValueError:
            pass
