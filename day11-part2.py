
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

    def getDistance(toX, toY, toZ):
        return (abs(toX) + abs(toY) + abs(toZ)) / 2

    furthestDist = 0

    x, y, z = 0, 0, 0
    goalX, goalY, goalZ = 0, 0, 0

    for d in dirs:
        x, y, z = getNeighbor(x, y, z, d)
        curDist = getDistance(x, y, z)
        if curDist > furthestDist:
            goalX, goalY, goalZ = x, y, z
            furthestDist = curDist

    print(max([abs(goalX), abs(goalY), abs(goalZ)]))


if __name__ == "__main__":
    main()
