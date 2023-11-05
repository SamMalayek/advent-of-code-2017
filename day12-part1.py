from collections import defaultdict


def main():
    connections = open('day12.txt', 'r').read().splitlines()

    adjList = defaultdict(list)

    for connection in connections:
        root, children = connection.split(' <-> ')
        adjList[root].extend(children.split(', '))

    def dfs(node, seen):
        seen.add(node)
        seenTarget = []
        for child in adjList[node]:
            if child not in seen:
                seenTarget.append(dfs(child, seen))

        if node == '0' or any(seenTarget):
            return True
        return False

    for root in adjList.keys():
        seen = set()
        if dfs(root, seen):
            print(len(seen))
            quit()


if __name__ == "__main__":
    main()
