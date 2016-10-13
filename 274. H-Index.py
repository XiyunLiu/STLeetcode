__author__ = 'liuxiyun'
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations == []:
            return 0
        n = len(citations)
        numPaper = [0 for i in range(0,n+1)]
        for citation in citations:
            if citation >= n:
                numPaper[n] += 1
            else:
                numPaper[citation] += 1
        curTotalPaper = 0
        for i in range(n,-1,-1):
            curTotalPaper += numPaper[i]
            if curTotalPaper >= i:
                return i
        return 0