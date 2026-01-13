# Best: O(n^2) [1, 2, 3, 4, 5]
# Worst: O(n^2) [5, 4, 3, 2, 1]
# Average: O(n^2)
# Stable: false [2, 3, 2, 1]


def selection_sort(nums):
    nums_count = len(nums)
    for i in range(nums_count - 1):
        min_index = i
        for j in range(i + 1, nums_count):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == "__main__":
    case_1 = [7, 6, 5, 4, 3, 2]
    case_2 = [8, 2, 1, 3, 4]
    case_3 = [1, 2, 3]

    selection_sort(case_1)
    selection_sort(case_2)
    selection_sort(case_3)

    print(case_1)
    print(case_2)
    print(case_3)
