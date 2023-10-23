
def main():
    lines = [int(step) for step in open('day05.txt', 'r').read().splitlines()]

    numSteps = 0
    curStep = 0
    while curStep < len(lines):
        prevCurStep = curStep
        curStep += lines[prevCurStep]
        numSteps += 1
        lines[prevCurStep] += 1
    print(numSteps)


if __name__ == "__main__":
    main()
