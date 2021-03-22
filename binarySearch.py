def binarySearch(nums, target):
    low = 0; high = len(nums)

    while low < high:
        mid = (low + high) >> 1
        print(mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1

if __name__ == '__main__':
    # nums = [2, 3, 4, 5, 6, 8, 10]
    nums = [8]
    ret = binarySearch(nums, 8)
    print(ret)