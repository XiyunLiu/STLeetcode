__author__ = 'liuxiyun'
import math
class Solution(object):
    ans = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        for num in range(len(self.ans),n+1):
            if num==int(math.sqrt(num)):
                self.ans.append(1)
                continue
            thisans=min(self.ans[num-j*j]+1 for j in range(1,int(math.sqrt(num))+1)) # For each i, it must be the sum of some number (i - j*j) and a perfect square number (j*j).
            self.ans.append(thisans)
        return self.ans[n]