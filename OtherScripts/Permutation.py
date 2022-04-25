def permute(index1: int, index2: int, set1, set2) -> None:
    if index1 == -1:
        return
    if index2 == -1:
        return
    print(set1[index1], set2[index2])
    print(set2[index2], set1[index1])
    permute(index1 - 1, index2, set1, set2)
    permute(index1, index2 - 1, set1, set2)


if __name__ == '__main__':
    set1 = input("Enter a set of inputs: ").split()
    set2 = input("Enter a second set of inputs: ").split()
    permute(len(set1) - 1, len(set2) - 1, set1, set2)

