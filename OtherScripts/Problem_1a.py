import sys


def greeting(arg: str) -> str:
    return "Welcome, " + arg + "!"


if __name__ == '__main__':
    print(greeting(sys.argv[1]))
