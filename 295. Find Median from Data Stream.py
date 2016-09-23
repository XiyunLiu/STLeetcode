__author__ = 'liuxiyun'
import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        if len(self.large) < len(self.small):
            tmp = -heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        print self.small
        print self.large

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.large == []:
            return -self.small[0]
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2.0
        return self.large[0]

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.addNum(3)
print mf.findMedian()