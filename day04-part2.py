
def main():
    lines = open('day04.txt', 'r').read().splitlines()
    resp = 0
    for l in lines:
        parts = [''.join(sorted(word)) for word in l.split()]
        if len(parts) == len(set(parts)):
            resp += 1

    print(resp)


if __name__ == "__main__":
    main()
