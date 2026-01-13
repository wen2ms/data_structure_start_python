# Best: O(nlog(n)) [1, 2, 3, 4, 5]
# Worst: O(nlog(n)) [5, 4, 3, 2, 1]
# Average: O(nlog(n))
# Stable: true [1, 2, 3, 2, 4]


def merge(low, mid, high, nums):
    left_count = mid - low + 1
    right_count = high - mid
    left = [0] * left_count
    right = [0] * right_count
    for i in range(left_count):
        left[i] = nums[low + i]
    for i in range(right_count):
        right[i] = nums[mid + i + 1]
    i = 0
    j = 0
    k = low
    while i < left_count and j < right_count:
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while i < left_count:
        nums[k] = left[i]
        i += 1
        k += 1
    while j < right_count:
        nums[k] = right[j]
        j += 1
        k += 1


def merge_sort(nums):
    def _merge_sort(low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        _merge_sort(low, mid)
        _merge_sort(mid + 1, high)
        merge(low, mid, high, nums)

    _merge_sort(0, len(nums) - 1)


if __name__ == "__main__":
    case_1 = [7, 6, 5, 4, 3, 2]
    case_2 = [8, 2, 1, 3, 4]
    case_3 = [1, 2, 3]

    merge_sort(case_1)
    merge_sort(case_2)
    merge_sort(case_3)

    print(case_1)
    print(case_2)
    print(case_3)
