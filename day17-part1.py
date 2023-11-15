
def main():
    numSteps = int(open('day17.txt').read().rstrip())

    cur = 0
    nextVal = 1
    arr = [0]

    while nextVal < 2018:
        cur = (cur + numSteps) % len(arr)
        cur += 1
        arr.insert(cur, nextVal)

        nextVal += 1

    print(arr[cur+1])


if __name__ == "__main__":
    main()
