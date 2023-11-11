
def main():
    connections = [c.split(': ') for c in open('day13.txt', 'r').read().splitlines()]
    maxStackNum = int(connections[-1][0]) + 1
    connections = {int(k): int(v) for k, v in connections}

    stackPos = [0 for _ in range(maxStackNum)]
    stackDirUp = [True for _ in range(maxStackNum)]

    cur = -1
    caughtLocs = []

    while cur < maxStackNum - 1:
        cur += 1  # According to problem, you begin outside the firewall, and step in as first operation

        if cur in connections and stackPos[cur] == 0:
            caughtLocs.append((cur, connections[cur]))

        for stackNum, length in connections.items():
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
        resp += (m1 * m2)
    print(resp)


if __name__ == "__main__":
    main()
