__author__ = 'liuxiyun'
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0,len(nums)-1
        if len(nums) >= 2 and nums[0] > nums[1]:
            return 0
        elif len(nums) >= 2 and nums[-2] < nums[-1]:
            return len(nums)-1
        while low < high:
            mid = (low+high)/2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
                return mid
            elif (mid == 0 or nums[mid-1] < nums[mid]) and (mid  == len(nums)-1 or nums[mid] < nums[mid+1]):
                low = mid
            else:
                high = mid
        return low
