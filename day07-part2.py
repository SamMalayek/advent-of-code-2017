from collections import defaultdict, namedtuple
import re

GroupSum = namedtuple('GroupSum', ['node', 'weight'])


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

    root = next(iter(heads))

    # Recurse to the bottom and work your way up, checking the weights of groups (sub-trees).
    def dfs(node):
        groupSums = []

        for child in adjList[node]:
            groupSums.append(GroupSum(child, dfs(child)))

        groupSums.sort(key=lambda x: x.weight)

        # We found the problem group
        if groupSums and groupSums[0].weight != groupSums[-1].weight:
            # First child in adjList is issue (head of its problem group)
            if groupSums[0].weight != groupSums[1].weight:
                diff = abs(groupSums[0].weight - groupSums[1].weight)
                print(nodeWeights[groupSums[0].node] - diff)
            # Last child in adjList is issue (head of its problem group)
            else:
                diff = abs(groupSums[-2].weight - groupSums[-1].weight)
                print(nodeWeights[groupSums[-1].node] - diff)
            quit()

        return sum([gs.weight for gs in groupSums]) + nodeWeights[node]

    dfs(root)


if __name__ == "__main__":
    main()
