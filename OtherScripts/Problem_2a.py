import math


def coin_change(dollars: float) -> tuple:
    quarters = dimes = nickles = 0
    while dollars >= .25:
        dollars -= .25
        quarters += 1
    while dollars >= .10:
        dollars -= .10
        dimes += 1
    while dollars >= .05:
        dollars -= .05
        nickles += 1
    pennies = int(math.ceil(dollars * 100))
    return quarters, dimes, nickles, pennies


def fewest_coins(dollars: float) -> int:
    coin = 0
    for i in coin_change(dollars):
        coin += i
    return coin


if __name__ == '__main__':
    print(coin_change(.98))
    print(fewest_coins(.98))
