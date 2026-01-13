def kadane(nums: list):
    maximum_sum = nums[0]
    curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = num if curr_sum < 0 else curr_sum + num
        maximum_sum = max(maximum_sum, curr_sum)
    return maximum_sum


if __name__ == "__main__":
    print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
