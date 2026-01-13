import random

# Best: O(n + k) 【0.12, 0.24, 0.37, 0.51, 0.63, 0.88]
# Worst: O(n + k) [0.91, 0.92, 0.93, 0.94, 0.95]
# Average: O(n + k)
# Stable: false


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
                elif nums[mid] == pivot:
                    mid += 1
                else:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1
            _quick_sort(left, low - 1)
            _quick_sort(high + 1, right)

    _quick_sort(0, len(nums) - 1)


def bucket_sort(nums):
    nums_count = len(nums)
    buckets = [[] for _ in range(nums_count)]
    for num in nums:
        index = int(nums_count * num)
        if index == nums_count:
            index = nums_count - 1
        buckets[index].append(num)

    for bucket in buckets:
        quick_sort(bucket)

    index = 0
    for bucket in buckets:
        for num in bucket:
            nums[index] = num
            index += 1


if __name__ == "__main__":
    nums = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
    bucket_sort(nums)
    print(nums)
