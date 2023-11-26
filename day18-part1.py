from collections import defaultdict


def main():
    cmds = open('day18.txt').read().splitlines()
    register = defaultdict(int)
    playedSounds = []
    recoveredSounds = []

    def isNum(val):
        try:
            int(val)
            return True
        except ValueError:
            return False

    def getNum(elem):
        return int(elem) if isNum(elem) else register[elem]

    cur = 0

    while cur < len(cmds):
        op, *rest = cmds[cur].split()

        if op == 'snd':
            num = getNum(rest[0])
            playedSounds.append(num)
        elif op == 'set':
            num = getNum(rest[1])
            register[rest[0]] = num
        elif op == 'add':
            num = getNum(rest[1])
            register[rest[0]] += num
        elif op == 'mul':
            num = getNum(rest[1])
            register[rest[0]] *= num
        elif op == 'mod':
            num = getNum(rest[1])
            if num != 0:
                register[rest[0]] %= num
        elif op == 'rcv':
            if len(playedSounds) != 0 and getNum(rest[0]) != 0:
                recoveredSounds.append(playedSounds.pop())
                print(recoveredSounds[-1])
                quit()
        elif op == 'jgz':
            if getNum(rest[0]) > 0:
                cur += getNum(rest[1])
                continue

        cur += 1


if __name__ == "__main__":
    main()
