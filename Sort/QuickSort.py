def quick_sort(nums):
    if len(nums) < 2:
        return nums
    privot = nums[0]
    left = [x for x in nums[1:] if x < privot]
    right = [x for x in nums[1:] if x >= privot]
    return quick_sort(left) + [privot] + quick_sort(right)


def quick_Sort(nums, start, end):
    if start < end:
        i, j = start, end
        privot = nums[start]
        while i < j:
            while nums[j] >= privot and i < j:
                j -= 1
            nums[i] = nums[j]
            while nums[i] <= privot and i < j:
                i += 1
            nums[j] = nums[i]
        nums[i] = privot

        quick_Sort(nums, start, i - 1)
        quick_Sort(nums, j + 1, end)
    return nums


nums = [2, 3, 1, 6, 3, 4, 8, 3, 5]
print(quick_Sort(nums, 0, len(nums) - 1))