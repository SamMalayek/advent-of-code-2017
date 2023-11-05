
def main():
    dirs = open('day11.txt', 'r').read().rstrip().split(',')

    def getNeighbor(x, y, z, direction):
        if direction == 'n':
            return x+1, y-1, z
        if direction == 's':
            return x-1, y+1, z
        if direction == 'ne':
            return x+1, y, z-1
        if direction == 'se':
            return x, y+1, z-1
        if direction == 'sw':
            return x-1, y, z+1
        return x, y-1, z+1  # nw

    x, y, z = 0, 0, 0

    for d in dirs:
        x, y, z = getNeighbor(x, y, z, d)

    print(max(abs(x), abs(y), abs(z)))


if __name__ == "__main__":
    main()
