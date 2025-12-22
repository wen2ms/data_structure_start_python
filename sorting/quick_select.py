# Best: O(n) [3, 1, 4, 2, 5]
# Worst: O(n^2) [5, 4, 3, 2, 1]
# Average: O(n)


def quick_select(nums, left, right, kth):
    if left == right:
        return nums[left]

    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    if i == kth:
        return nums[i]
    if i > kth:
        return quick_select(nums, left, i - 1, kth)
    return quick_select(nums, i + 1, right, kth)


if __name__ == "__main__":
    nums = [4, 3, 2, 1, 5]
    print(quick_select(nums, 0, len(nums) - 1, 2))
