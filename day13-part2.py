
def main():
    connections = [c.split(': ') for c in open('day13.txt', 'r').read().splitlines()]
    maxStackNum = int(connections[-1][0]) + 1
    connections = {int(k): int(v) for k, v in connections}

    stackPos = [0 for _ in range(maxStackNum)]
    stackDirUp = [True for _ in range(maxStackNum)]

    def iterate():
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

    def flipDir():
        for i in range(len(stackDirUp)):
            stackDirUp[i] = not stackDirUp[i]

    wait = 0
    cur = -1

    foundPath = False

    while not foundPath:
        while cur < maxStackNum-1:
            cur += 1  # According to problem, you begin outside the firewall, and step in as first operation

            if cur >= 0 and cur in connections and stackPos[cur] == 0:
                wait += 1
                flipDir()
                while cur > 0:
                    iterate()
                    cur -= 1
                flipDir()
                cur = -2
                break

            iterate()

        if cur == maxStackNum - 1:
            foundPath = True

    print(wait)


if __name__ == "__main__":
    main()
