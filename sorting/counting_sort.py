# Best: O(n + k) [1, 2, 3, 4, 5]
# Worst: O(n + k) [5, 4, 3, 2, 1]
# Average: O(n + k)
# Stable: false [1, 2, 3, 2, 4]


def counting_sort(nums):
    maximum = max(nums)
    counts = [0] * (maximum + 1)
    for num in nums:
        counts[num] += 1
    index = 0
    for i in range(maximum + 1):
        while counts[i] > 0:
            nums[index] = i
            index += 1
            counts[i] -= 1


if __name__ == "__main__":
    case_1 = [7, 6, 5, 4, 3, 2]
    case_2 = [8, 2, 1, 3, 4]
    case_3 = [1, 2, 3]

    counting_sort(case_1)
    counting_sort(case_2)
    counting_sort(case_3)

    print(case_1)
    print(case_2)
    print(case_3)
