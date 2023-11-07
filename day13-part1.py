
def main():
    connections = [list(map(int, c.split(': '))) for c in open('day13.txt', 'r').read().splitlines()]
    maxStackNum = connections[-1][0] + 1

    stackLens = [0 for _ in range(maxStackNum)]
    stackPos = [0 for _ in range(maxStackNum)]
    stackDirUp = [True for _ in range(maxStackNum)]
    for stackNum, length in connections:
        stackLens[stackNum] = length

    cur = -1
    caughtLocs = []

    while cur < maxStackNum-1:
        cur += 1

        if stackLens[cur] > 0 and stackPos[cur] == 0:
            caughtLocs.append((cur, stackLens[cur]))

        for stackNum, length in connections:
            if stackDirUp[stackNum] and stackPos[stackNum] < length - 1:
                stackPos[stackNum] = (stackPos[stackNum] + 1) % length
            elif stackPos[stackNum] == length - 1:
                stackPos[stackNum] = (stackPos[stackNum] - 1) % length
                stackDirUp[stackNum] = False
            elif stackPos[stackNum] == 0:
                stackPos[stackNum] = (stackPos[stackNum] + 1) % length
                stackDirUp[stackNum] = True
            else:
                stackPos[stackNum] = (stackPos[stackNum] - 1) % length

    resp = 0
    for m1, m2 in caughtLocs:
        resp += (m1*m2)
    print(resp)


if __name__ == "__main__":
    main()
