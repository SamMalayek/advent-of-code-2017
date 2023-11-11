
def main():
    lines = open('day15.txt', 'r').read().splitlines()
    count = 0
    divisor = 2147483647

    def genA():
        curA = int(lines[0].split()[-1])
        while True:
            curA = (curA * 16807) % divisor
            if curA % 4 == 0:
                yield curA

    def genB():
        curB = int(lines[1].split()[-1])
        while True:
            curB = (curB * 48271) % divisor
            if curB % 8 == 0:
                yield curB

    yieldA = genA()
    yieldB = genB()
    for _ in range(5000000):
        a = next(yieldA)
        b = next(yieldB)

        if bin(a)[-16:] == bin(b)[-16:]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
