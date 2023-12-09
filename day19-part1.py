from collections import deque


def main():
    grid = open('day19.txt').read().splitlines()

    def baseShouldSkip(row, col):
        if row < 0 or row >= len(grid):  # Only needed for the example
            return True
        if col < 0 or col >= len(grid[row]):  # Only needed for the example
            return True
        if grid[row][col] == ' ':
            return True
        return False

    dirs = [  # Supports Python <3.7 where order of dict keys is not guaranteed to equal insertion order
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

    lettersSeen = []

    startRow = 0
    startCol = 0

    for i, col in enumerate(grid[0]):
        if col == '|':
            startCol = i
            break

    queue = deque([(startRow, startCol)])

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

        elif grid[nextRow][nextCol].isalpha():
            lettersSeen.append(grid[nextRow][nextCol])

        queue.append((nextRow, nextCol))

    print(''.join(lettersSeen))


if __name__ == "__main__":
    main()
