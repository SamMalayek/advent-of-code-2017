
def main():
    s = open('day09.txt', 'r').read().rstrip()

    curDepth = 0
    score = 0
    inGarbage = False
    exclamation = -1
    garbageCount = 0

    i = 0
    while i < len(s):
        c = s[i]
        if exclamation == i:
            exclamation = -1
        elif c == '!':
            exclamation = i+1
        elif c == '>':
            inGarbage = False
        elif inGarbage:
            garbageCount += 1
        elif c == '{':
            curDepth += 1
        elif c == '}':
            score += curDepth
            curDepth -= 1
        elif c == '<':
            inGarbage = True

        i += 1

    print(garbageCount)


if __name__ == "__main__":
    main()
