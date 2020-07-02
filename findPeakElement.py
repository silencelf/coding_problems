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

sol = Solution()
nums = [1,2,1,3,5,6,4]
result  = sol.findPeakElement(nums)
print(f'{nums} : {result}')