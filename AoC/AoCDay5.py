from collections import defaultdict


def count_sum(include: bool) -> int:  # Find the total number of lines, include boolean True = diagonals, False = none
    d = defaultdict(int)  # Dict will contain all points
    for start, end in points:  # start is x, y for start, end is x, y for end
        if (start.split(",")[0] == end.split(",")[0]) or (start.split(",")[1] == end.split(",")[1].strip("\n")):
            starts = [int(start.split(",")[0]), int(start.split(",")[1])]  # Create a list of ints for easier parsing
            ends = [int(end.split(",")[0]), int(end.split(",")[1])]  # Create a list of ints for easier parsing
            while starts[0] != ends[0]:  # While X start is not X end
                d[starts[0], starts[1]] += 1  # Add point to the dictionary
                if starts[0] < ends[0]:  # Draw line to the right
                    starts[0] += 1
                else:
                    starts[0] -= 1  # Draw line to the left
            while starts[1] != ends[1]:  # While Y start is not Y end
                d[starts[0], starts[1]] += 1  # Add point to dictionary
                if starts[1] < ends[1]:  # Draw line downwards
                    starts[1] += 1
                else:
                    starts[1] -= 1  # Draw line upwards
            d[starts[0], starts[1]] += 1  # Account for last iteration of while not happening -> Do While loop
        elif include is True:  # If include diagonal and neither x nor y have the same start and end coordinate
            starts = [int(start.split(",")[0]), int(start.split(",")[1])]  # Create a list of ints for easier parsing
            ends = [int(end.split(",")[0]), int(end.split(",")[1])]  # Create a list of ints for easier parsing
            while starts[0] != ends[0]:  # Only need to check X coordinate, as x and y for diagonal only change by one
                d[starts[0], starts[1]] += 1  # Add point to dictionary
                if starts[0] < ends[0]:  # Checking X coordinate
                    starts[0] += 1
                else:
                    starts[0] -= 1
                if starts[1] < ends[1]:  # Checking Y coordinate
                    starts[1] += 1
                else:
                    starts[1] -= 1
            d[starts[0], starts[1]] += 1  # Accounting for last iteration of while not happening -> Do While loop
    count = sum(  # Count total number of dictionary entries above 1, i.e. the overlap points
        d[i] > 1
        for i in d
    )
    return count


if __name__ == '__main__':
    file = open("/Users/dylan/Library/CloudStorage/Box-Box/My Box Notes/Python/InputFiles/Day5.txt", "r")
    points = [line.split(" -> ") for line in file]  # Split each line into a list of two points
    print(count_sum(False))  # Boolean includes diagonals
