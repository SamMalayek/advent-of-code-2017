
def main():
    nums = [list(map(int, l.split())) for l in open('day02.txt', 'r').read().splitlines()]

    resp = 0
    for l in nums:
        added = False
        for first in l:
            if added:
                break
            for second in l:
                if first == second:
                    continue
                cur = sorted([first, second])
                if cur[1] % cur[0] == 0:
                    resp += cur[1] // cur[0]
                    added = True
                    break

    print(resp)


if __name__ == "__main__":
    main()
