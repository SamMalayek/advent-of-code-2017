from collections import defaultdict, deque
from concurrent.futures import ThreadPoolExecutor
import threading


def main():
    cmds = open('day18.txt').read().splitlines()
    registerA = defaultdict(int)
    registerB = defaultdict(int)
    registerB['p'] = 1
    conditionA = threading.Condition()
    conditionB = threading.Condition()

    AtoB = deque([])
    BtoA = deque([])

    def isNum(val):
        try:
            int(val)
            return True
        except ValueError:
            return False

    def getNum(elem, reg):
        return int(elem) if isNum(elem) else reg[elem]

    def isTimeoutOnChannel(channel, condition):
        with condition:
            while not channel:
                notifiedBeforeTimeout = condition.wait(timeout=1/100)
                if not notifiedBeforeTimeout:
                    return True
                return False

    def runProgram(receiveChannel, sendChannel, receiveCondition, sendCondition, register):
        cur = 0
        counter = 0

        while cur < len(cmds):
            op, *rest = cmds[cur].split()
            if op == 'snd':
                num = getNum(rest[0], register)
                sendChannel.appendleft(num)
                with sendCondition:
                    sendCondition.notify()

                counter += 1
            elif op == 'set':
                num = getNum(rest[1], register)
                register[rest[0]] = num
            elif op == 'add':
                num = getNum(rest[1], register)
                register[rest[0]] += num
            elif op == 'mul':
                num = getNum(rest[1], register)
                register[rest[0]] *= num
            elif op == 'mod':
                num = getNum(rest[1], register)
                if num != 0:
                    register[rest[0]] %= num
            elif op == 'rcv':
                if isTimeoutOnChannel(receiveChannel, receiveCondition):
                    return counter

                register[rest[0]] = receiveChannel.pop()

                if isTimeoutOnChannel(receiveChannel, receiveCondition):
                    return counter
            elif op == 'jgz':
                if getNum(rest[0], register) > 0:
                    cur += getNum(rest[1], register)
                    continue
            cur += 1
        return counter

    with ThreadPoolExecutor(max_workers=2) as executor:
        futureA = executor.submit(runProgram, BtoA, AtoB, conditionA, conditionB, registerA)
        futureB = executor.submit(runProgram, AtoB, BtoA, conditionB, conditionA, registerB)
        futureA.result()
        print(futureB.result())


if __name__ == "__main__":
    main()
