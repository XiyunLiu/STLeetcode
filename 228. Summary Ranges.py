__author__ = 'liuxiyun'
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        answer=[]
        if len(nums)==0:
            return []
        i=0
        while i<len(nums):
            start = nums[i]
            while i+1 < len(nums) and nums[i+1] - nums[i] == 1:
                i += 1
            if start != nums[i]:
                answer.append(str(start) + "->" + str(nums[i]))
            else:
                answer.append(str(start))
            i+=1
        return answer
