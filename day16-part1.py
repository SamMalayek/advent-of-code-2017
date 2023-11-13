
def main():
    cmds = open('day16.txt').read().rstrip().split(',')
    baseOrd = 97
    letters = [chr(o) for o in range(baseOrd, baseOrd+16)]

    def swap(a, b):
        letters[a], letters[b] = letters[b], letters[a]

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

    print(''.join(letters))


if __name__ == "__main__":
    main()
