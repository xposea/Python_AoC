def convert_input(inputs: list) -> list:
    return [float(i) for i in inputs]


if __name__ == '__main__':
    repeat = True
    while repeat:
        try:
            print(convert_input(input("Input a list: ").split()))
            repeat = False
        except ValueError:
            pass
