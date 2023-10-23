
def main():
    nums = list(map(int, open('day01.txt', 'r').read().rstrip()))

    resp = 0
    i = 0
    while i < len(nums):
        if nums[i-1] == nums[i]:
            resp += nums[i]
        i += 1

    print(resp)


if __name__ == "__main__":
    main()
