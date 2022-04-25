if __name__ == '__main__':
    repeat = False
    while not repeat:
        try:
            num = int(input("Enter an integer number: "))
            repeat = True
            if num % 15 == 0:
                print('FizzBuzz')
            elif num % 3 == 0:
                print('Fizz')
            elif num % 5 == 0:
                print('Buzz')
            else:
                print(num)
        except ValueError:
            pass
