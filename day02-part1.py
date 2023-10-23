
def main():
    nums = [list(map(int, l.split())) for l in open('day02.txt', 'r').read().splitlines()]

    resp = 0
    for l in nums:
        resp += abs(min(l) - max(l))
    print(resp)


if __name__ == "__main__":
    main()
