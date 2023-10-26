from collections import defaultdict
import re


def main():
    lines = open('day07.txt', 'r').read().splitlines()
    adjList = defaultdict(list)
    heads = set()
    nodeWeights = {}

    for l in lines:
        parts = [part for part in re.split(' |,|->|\)|\(', l) if part]
        node = parts[0]
        weight = int(parts[1])
        nodeWeights[node] = weight
        if len(parts) > 2:
            head = parts[0]
            heads.add(head)
            adjList[head].extend(parts[2:])

    for children in adjList.values():
        heads = heads - set(children)

    print(next(iter(heads)))


if __name__ == "__main__":
    main()
