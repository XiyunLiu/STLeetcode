__author__ = 'liuxiyun'
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
        intervals.sort(key = lambda x: x.start)
        res = [intervals[0]]
        for interval in intervals:
            if interval.start > res[-1].end:
                res.append(interval)
            else:
                res[-1].end = max(res[-1].end, interval.end)
        return res
