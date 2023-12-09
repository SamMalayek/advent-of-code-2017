from collections import deque


def main():
    grid = [a for a in open('day19.txt').read().splitlines() if a]

    def baseShouldSkip(row, col):
        if row < 0 or row >= len(grid):
            return True
        if col < 0 or col >= len(grid[row]):
            return True
        if grid[row][col] == ' ':
            return True
        return False

    dirs = [
        (1, 0),   # Down
        (0, 1),   # Right
        (-1, 0),  # Up
        (0, -1)   # Left
    ]
    dirsToIndex = {
        (1, 0): 0,
        (0, 1): 1,
        (-1, 0): 2,
        (0, -1): 3
    }
    curDir = 0

    startRow = 0
    startCol = 0

    for i, col in enumerate(grid[0]):
        if col == '|':
            startCol = i
            break

    queue = deque([(startRow, startCol)])
    numSteps = 1  # This isn't a typical BFS where we need to store the count in the queue's tuple.

    while queue:
        curRow, curCol = queue.popleft()

        rowOffset, colOffset = dirs[curDir][0], dirs[curDir][1]

        nextRow, nextCol = rowOffset+curRow, colOffset+curCol

        if baseShouldSkip(nextRow, nextCol):
            continue

        elif grid[nextRow][nextCol] == '+':
            # This strictly sets direction using a 'lookahead' and nothing else.
            for rowOffset, colOffset in dirs:
                afterNextRow, afterNextCol = rowOffset+nextRow, colOffset+nextCol
                if afterNextRow == curRow and afterNextCol == curCol:
                    continue
                if baseShouldSkip(afterNextRow, afterNextCol):
                    continue
                curDir = dirsToIndex[(rowOffset, colOffset)]

        numSteps += 1
        queue.append((nextRow, nextCol))

    print(numSteps)


if __name__ == "__main__":
    main()
