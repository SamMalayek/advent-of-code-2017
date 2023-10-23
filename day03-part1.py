import math


def main():
    myInput = int(open('day03.txt', 'r').read().rstrip())

    botRightCornerPos = math.ceil(math.sqrt(myInput))
    botRightCornerVal = botRightCornerPos**2

    botMidVal = botRightCornerVal - (botRightCornerPos // 2)

    if myInput > botMidVal:
        distToCenter = (botRightCornerPos // 2)*2 - (botRightCornerVal - myInput)
        print(distToCenter)
    else:
        distToCenter = (botRightCornerPos // 2) + (botMidVal - myInput)
        print(distToCenter)


if __name__ == "__main__":
    main()
