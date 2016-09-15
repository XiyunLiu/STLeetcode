__author__ = 'liuxiyun'
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums.append(upper+1)
        pre = lower-1
        res = []
        for num in nums:
            if (num-pre) <= 1:
                pass
            elif (num-pre) == 2:
                res.append(str(num-1))
            else:
                res.append(str(pre+1) + "->" + str(num-1))
            pre = num
        return res