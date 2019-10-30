import random

ROCK = 1        #石头
PAPER = 2       #剪刀
SCISSORS = 3    #布

WIN = 1         #胜
LOSS = 2        #负
DRAW = 3        #平


def rock_paper_scissors(a, b):
    if a == b:
        return DRAW
    if a == b - 1 or (a == 3 and b == 1):
        return WIN
    else:
        return LOSS



if __name__ == "__main__":
    for i in range(100):
        a = random.randint(1,3)
        b = random.randint(1,3)
        result = rock_paper_scissors(a, b)
        if result == WIN:
            print("A is Winner")
        elif result == LOSS:
            print("B is Winner")
        else:
            print("Draw")
    