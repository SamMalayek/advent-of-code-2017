
def main():
    connections = [list(map(int, c.split(': '))) for c in open('day13.txt', 'r').read().splitlines()]
    maxStackNum = connections[-1][0] + 1

    stackLens = [0 for _ in range(maxStackNum)]
    stackPos = [0 for _ in range(maxStackNum)]
    stackDirUp = [True for _ in range(maxStackNum)]
    for connection in connections:
        stackNum, length = connection
        stackLens[stackNum] = length

    cur = -1
    caughtLocs = []

    while cur < maxStackNum-1:
        cur += 1

        if stackLens[cur] > 0 and stackPos[cur] == 0:
            caughtLocs.append((cur, stackLens[cur]))

        for i in range(len(stackLens)):
            if stackDirUp[i] and stackPos[i] < stackLens[i] - 1:
                stackPos[i] = (stackPos[i] + 1) % stackLens[i] if stackLens[i] > 0 else 0
            elif stackPos[i] == stackLens[i] - 1:
                stackPos[i] = (stackPos[i] - 1) % stackLens[i] if stackLens[i] > 0 else 0
                stackDirUp[i] = False
            elif stackPos[i] == 0:
                stackPos[i] = (stackPos[i] + 1) % stackLens[i] if stackLens[i] > 0 else 0
                stackDirUp[i] = True
            else:
                stackPos[i] = (stackPos[i] - 1) % stackLens[i] if stackLens[i] > 0 else 0

    resp = 0
    for m1, m2 in caughtLocs:
        resp += (m1*m2)
    print(resp)


if __name__ == "__main__":
    main()
