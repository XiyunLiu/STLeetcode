__author__ = 'liuxiyun'
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = 1
        sequenceMap = {}
        for num in nums:
            if num in sequenceMap:
                continue
            if num-1 in sequenceMap:
                left = sequenceMap[num-1]
            else:
                left = 0
            if num+1 in sequenceMap:
                right = sequenceMap[num+1]
            else:
                right = 0
            newTotalLength = left+right+1
            sequenceMap[num-left] = newTotalLength
            sequenceMap[num+right] = newTotalLength
            sequenceMap[num] = newTotalLength
            maxLength = max(maxLength,newTotalLength)
            print sequenceMap
        return maxLength
c = Solution()
print c.longestConsecutive([1,3,2,4])