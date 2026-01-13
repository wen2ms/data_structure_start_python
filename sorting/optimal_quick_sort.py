import random

# Best: O(n) [2, 2, 2, 3]
# Worst: O(n^2) [5, 4, 3, 2, 1]
# Average: O(nlog(n))
# Stable: False [2, 2, 1]


def quick_sort(nums):
    def _quick_sort(left, right):
        if left < right:
            low = left
            mid = left
            high = right
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]
            while mid <= high:
                if nums[mid] < pivot:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low += 1
                    mid += 1
                elif nums[mid] > pivot:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1
                else:
                    mid += 1
            _quick_sort(left, low - 1)
            _quick_sort(high + 1, right)

    _quick_sort(0, len(nums) - 1)


if __name__ == "__main__":
    case_1 = [7, 6, 5, 4, 3, 2]
    case_2 = [8, 2, 1, 3, 4]
    case_3 = [1, 2, 3]

    quick_sort(case_1)
    quick_sort(case_2)
    quick_sort(case_3)

    print(case_1)
    print(case_2)
    print(case_3)
