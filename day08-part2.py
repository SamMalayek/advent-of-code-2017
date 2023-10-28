from collections import defaultdict


def main():
    lines = open('day08.txt', 'r').read().splitlines()
    register = defaultdict(int)
    values = []

    for l in lines:
        toExec = l.replace(' inc ', ' += ').replace(' dec ', ' -= ') + ' else 0'

        exec(toExec, {}, register)

        values.append(max(register.values()))

    print(max(values))


if __name__ == "__main__":
    main()
