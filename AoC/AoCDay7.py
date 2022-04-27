from statistics import median, mean


def count_fuel(number_of_spaces) -> int:
    return sum(
        num
        for num in range(number_of_spaces + 1)
    )


if __name__ == '__main__':
    inputs = open("/Users/dylan/Library/CloudStorage/Box-Box/My Box Notes/Python/InputFiles/Day7.txt", "r").readline()
    inputs = [int(inputs_s) for inputs_s in inputs.split(",")]
    print(sum(
        abs(number - median(inputs))
        for number in inputs
    ))
    print(sum(
        count_fuel(abs(number - int(mean(inputs))))
        for number in inputs
    ))  # Works for my input but doesn't work for the example? Just barely off by 2. Seems like range of answers.
