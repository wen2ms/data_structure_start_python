# Best: O(n) [1, 2, 3, 4, 5]
# Worst: O(n^2) [5, 4, 3, 2, 1]
# Average: O(n^2)
# Stable: true [1, 2, 3, 2, 4]


def insertion_sort(nums):
    nums_count = len(nums)
    for i in range(1, nums_count):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key


if __name__ == "__main__":
    case_1 = [7, 6, 5, 4, 3, 2]
    case_2 = [8, 2, 1, 3, 4]
    case_3 = [1, 2, 3]

    insertion_sort(case_1)
    insertion_sort(case_2)
    insertion_sort(case_3)

    print(case_1)
    print(case_2)
    print(case_3)
