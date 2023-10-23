
def main():
	nums = list(map(int, open('day01.txt', 'r').read().rstrip()))

	resp = 0
	i = 0
	while i < len(nums):
		offset = len(nums)//2 + i if len(nums)//2 + i < len(nums) else i - len(nums)//2
		if nums[i] == nums[offset]:
			resp += nums[i]
		i += 1

	print(resp)


if __name__ == "__main__":
	main()
