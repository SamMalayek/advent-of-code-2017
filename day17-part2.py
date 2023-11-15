
def main():
    numSteps = int(open('day17.txt').read().rstrip())

    cur = 0
    nextVal = 1
    oneVal = -1

    while nextVal < 50000001:
        cur = (cur + numSteps) % nextVal
        cur += 1
        if cur == 1:
            oneVal = nextVal

        nextVal += 1

    print(oneVal)


if __name__ == "__main__":
    main()
