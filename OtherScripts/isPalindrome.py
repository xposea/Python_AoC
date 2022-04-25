if __name__ == '__main__':
    string = input("Input a palindrome: ")
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
        