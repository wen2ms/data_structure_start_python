def bisect_left(nums: list, key):
    nums_count = len(nums)
    low = 0
    high = nums_count
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < key:
            low = mid + 1
        else:
            high = mid
    return low


def bisect_right(nums: list, key):
    nums_count = len(nums)
    low = 0
    high = nums_count
    while low < high:
        mid = (low + high) // 2
        if nums[mid] <= key:
            low = mid + 1
        else:
            high = mid
    return low


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(bisect_left(nums, 3), bisect_right(nums, 3))
