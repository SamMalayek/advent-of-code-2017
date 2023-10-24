
def main():
    myInput = int(open('day03.txt', 'r').read().rstrip())

    maxLen = 11

    grid = [[0 for _ in range(maxLen)] for _ in range(maxLen)]

    centerRow, centerCol = maxLen//2, maxLen//2
    curRow, curCol = maxLen//2, maxLen//2
    curVal = 1
    nextCornerRow, nextCornerCol = curRow, curCol+1
    dirs = [
        (0, 1),  # Right
        (-1, 0),  # Up
        (0, -1),  # Left
        (1, 0),  # Down
    ]
    dirCorners = [
        (1, 1),  # Bot-Right
        (-1, 1),  # Top-Right
        (-1, -1),  # Top-Left
        (1, -1),  # Bot-Left
    ]
    curDir = 0
    lenFromCenter = 1

    while curVal < myInput:
        grid[curRow][curCol] = curVal
        curRow, curCol = curRow+dirs[curDir][0], curCol+dirs[curDir][1]

        curVal = sum([sum(grid[curRow + i][curCol-1:curCol+2]) for i in range(-1, 2)])
        if (curRow, curCol) == (nextCornerRow, nextCornerCol):
            curDir = (curDir+1) % 4
            if curDir == 0:
                lenFromCenter += 1
                nextCornerRow = centerRow+(dirCorners[curDir][0]*lenFromCenter)-1
                nextCornerCol = centerCol+(dirCorners[curDir][1]*lenFromCenter)
            else:
                nextCornerRow = centerRow+(dirCorners[curDir][0]*lenFromCenter)
                nextCornerCol = centerCol+(dirCorners[curDir][1]*lenFromCenter)

    print(curVal)


if __name__ == "__main__":
    main()
