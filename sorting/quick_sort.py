# Best: O(nlog(n)) [3, 1, 4, 2, 5]
# Worst: O(n^2) [5, 4, 3, 2, 1]
# Average: O(nlog(n))
# Stable: false [2, 2, 1]


def quick_sort(nums):
    def _quick_sort(left, right):
        if left < right:
            i = left
            j = right
            pivot = nums[left]
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[left] = nums[left], nums[i]
            _quick_sort(left, i - 1)
            _quick_sort(i + 1, right)

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
