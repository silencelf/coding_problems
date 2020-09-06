class Solution:
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        low, high, dir1, dir2 = 1, len(nums) - 1, 0, 0
        while low < high:
            mid = low + (high - low ) // 2
            if nums[mid -1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                low = mid + 1
                dir2 = 1
                if not dir1:
                    dir1 = 1
                if dir1 != dir2:    
                    return mid
            else:
                high = mid - 1    
                dir2 = 1
                if not dir1:
                    dir1 = -1
                if dir1 != dir2:    
                    return mid
        if low == 0 and nums[mid] > nums[mid+1]:       
            return low
        if low == len(nums) -1 and nums[mid] > nums[mid + 1]:
            return low

    def findPeak(self, nums):
        if not nums:
            return -1
        low, high= 0, len(nums) - 1
        while low < high:
            mid1 = (high + low) // 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                low = mid2
            else:
                high = mid1
        return low

sol = Solution()
nums = [1,2,1,3,5,6,4]
#result  = sol.findPeakElement(nums)
result  = sol.findPeak(nums)
print(f'Peak of {nums} : {nums[result]}')
