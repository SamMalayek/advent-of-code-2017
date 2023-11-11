
def main():
    lines = open('day15.txt', 'r').read().splitlines()
    count = 0
    divisor = 2147483647

    def gen(multi, factor, cur):
        while True:
            cur = (cur * multi) % divisor
            if cur % factor == 0:
                yield cur

    yieldA = gen(16807, 4, int(lines[0].split()[-1]))
    yieldB = gen(48271, 8, int(lines[1].split()[-1]))
    for _ in range(5000000):
        a = next(yieldA)
        b = next(yieldB)

        if bin(a)[-16:] == bin(b)[-16:]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
