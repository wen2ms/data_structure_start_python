# Best: O(nlog(n))
# Worst: O(nlog(n))
# Average: O(nlog(n))
# Stable: false [[3, 2, 3, 1]


def heapify(index, nums_count, nums):
    maximum_pos = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < nums_count and nums[left] > nums[maximum_pos]:
        maximum_pos = left
    if right < nums_count and nums[right] > nums[maximum_pos]:
        maximum_pos = right
    if maximum_pos != index:
        nums[index], nums[maximum_pos] = nums[maximum_pos], nums[index]
        heapify(maximum_pos, nums_count, nums)


def heap_sort(nums):
    nums_count = len(nums)
    for i in range(nums_count // 2 - 1, -1, -1):
        heapify(i, nums_count, nums)
    for i in range(nums_count - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(0, i, nums)


if __name__ == "__main__":
    case_1 = [7, 6, 5, 4, 3, 2]
    case_2 = [8, 2, 1, 3, 4]
    case_3 = [1, 2, 3]

    heap_sort(case_1)
    heap_sort(case_2)
    heap_sort(case_3)

    print(case_1)
    print(case_2)
    print(case_3)
