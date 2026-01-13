# Best: O(n) [1, 2, 3, 4, 5]
# Worst: O(n^2) [5, 4, 3, 2, 1]
# Average: O(n^2)
# Stable: true [2, 1, 2]


def bubble_sort(nums):
    nums_count = len(nums)
    swapped = False
    for i in range(nums_count - 1):
        for j in range(nums_count - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            return


if __name__ == "__main__":
    case_1 = [6, 5, 4, 3, 2, 1]
    case_2 = [8, 2, 1, 3, 4]
    case_3 = [1, 2, 3]
    bubble_sort(case_1)
    bubble_sort(case_2)
    bubble_sort(case_3)
    print(case_1)
    print(case_2)
    print(case_3)
