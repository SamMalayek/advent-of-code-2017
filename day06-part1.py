import math

def main():
    cur = tuple(map(int, open('day06.txt', 'r').read().rstrip().split()))
    lenCur = len(cur)
    seen = set()
    count = 0

    while cur not in seen:
        seen.add(cur)
        maxI = 0
        maxIVal = 0
        for i in range(lenCur):
            if cur[i] > maxIVal:
                maxI = i
                maxIVal = cur[i]
        curMutate = list(cur)
        curMutate[maxI] = 0
        curI = maxI
        for i in range(lenCur):
            curI = (curI + 1) % lenCur
            distributionCount = math.ceil(maxIVal / (lenCur - i))
            maxIVal -= distributionCount
            curMutate[curI] += distributionCount

        cur = tuple(curMutate)

        count += 1

    print(count)

if __name__ == "__main__":
    main()
