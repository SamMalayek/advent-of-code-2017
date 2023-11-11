
def main():
    lines = open('day15.txt', 'r').read().splitlines()
    count = 0
    divisor = 2147483647
    curA = int(lines[0].split()[-1])
    curB = int(lines[1].split()[-1])

    for _ in range(40000000):
        curA = (curA * 16807) % divisor
        curB = (curB * 48271) % divisor

        if bin(curA)[-16:] == bin(curB)[-16:]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
