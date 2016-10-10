__author__ = 'liuxiyun'
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == [] or k <= 0:
            return []
        n = len(nums)
        values = []
        queue = deque()
        for i in range(len(nums)):
            print 'i=',i,'num=',nums[i],
            while queue and queue[0] < i-k+1:
                print ' remove left',queue[0],
                queue.popleft()
            while queue and nums[queue[-1]]<nums[i]:
                print ' remove smaller',queue[-1],
                queue.pop()
            print ' push i',i,
            queue.append(i)
            if i>=k-1:
                print '[add max value',queue[-1],']',
                values.append(nums[queue[0]])
            print ' queue',queue
        return values
c = Solution()
print c.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)