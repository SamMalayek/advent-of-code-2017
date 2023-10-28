
def main():
    s = open('day09.txt', 'r').read().rstrip()

    curDepth = 0
    score = 0
    inGarbage = False
    exclamation = -1

    i = 0
    while i < len(s):
        c = s[i]
        if exclamation == i:
            exclamation = -1
            i += 1
            continue
        elif c == '!':
            exclamation = i+1
        elif c == '>':
            inGarbage = False
        elif inGarbage:
            i += 1
            continue
        elif c == '{':
            curDepth += 1
        elif c == '}':
            score += curDepth
            curDepth -= 1
        elif c == '<':
            inGarbage = True

        i += 1

    print(score)


main()
