
def main():
    lines = open('day15.txt', 'r').read().splitlines()
    count = 0
    aMulti = 16807
    bMulti = 48271
    divisor = 2147483647
    curA = int(lines[0].split()[-1])
    curB = int(lines[1].split()[-1])
    lastA = -1
    lastB = -1

    for _ in range(5000000):
        while curA % 4 != 0 or curA == lastA:
            curA = (curA * aMulti) % divisor
        while curB % 8 != 0 or curB == lastB:
            curB = (curB * bMulti) % divisor
        lastA = curA
        lastB = curB

        curABin = bin(curA)[2:].rjust(32, '0')[-16:]
        curBBin = bin(curB)[2:].rjust(32, '0')[-16:]
        if curABin == curBBin:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
