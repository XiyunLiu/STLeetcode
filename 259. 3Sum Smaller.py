__author__ = 'liuxiyun'
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 2:
            return 0
        count = 0
        nums.sort()
        for i in range(0,len(nums)-2):
            j = i+1
            k = len(nums)-1
            tar = target - nums[i]
            while j<k:
                if nums[j] + nums[k] < tar:
                    count += (k-j)
                    j += 1
                else:
                    k -= 1
        return count