from collections import defaultdict


def main():
    connections = open('day12.txt', 'r').read().splitlines()

    adjList = defaultdict(list)
    total = set()

    for connection in connections:
        root, children = connection.split(' <-> ')
        adjList[root].extend(children.split(', '))
        total.add(root)
        total = total.union(set(adjList[root]))

    def dfs(node, seen):
        seen.add(node)
        seenTarget = []
        for child in adjList[node]:
            if child in seen:
                continue
            seenTarget.append(dfs(child, seen))

        if node == '0' or any(seenTarget):
            return True

    numGroups = 0
    for root in adjList.keys():
        seen = set()
        dfs(root, seen)
        beforeDiff = len(total)
        total = total - seen
        if len(total) != beforeDiff:
            numGroups += 1
    print(numGroups)


if __name__ == "__main__":
    main()
