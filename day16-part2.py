
def main():
    cmds = open('day16.txt').read().rstrip().split(',')
    baseOrd = 97
    letters = [chr(o) for o in range(baseOrd, baseOrd+16)]
    seen = set()
    maxSeenLen = 0
    iterations = 1000000000

    def swap(i, j):
        letters[i], letters[j] = letters[j], letters[i]

    cur = 0
    while cur < iterations:
        for cmd in cmds:
            operation, rest = cmd[0], cmd[1:]
            if operation == 's':
                i = int(rest)
                letters = letters[-i:] + letters[:-i]
            elif operation == 'x':
                i, j = list(map(int, rest.split('/')))
                swap(i, j)
            elif operation == 'p':
                i, j = list(map(letters.index, rest.split('/')))
                swap(i, j)

        seen.add(tuple(letters))
        curSeenLen = len(seen)
        if curSeenLen == maxSeenLen:
            multi = (iterations - cur) // cur
            cur += (multi * cur)

        maxSeenLen = max(maxSeenLen, curSeenLen)
        cur += 1

    print(''.join(letters))


if __name__ == "__main__":
    main()
