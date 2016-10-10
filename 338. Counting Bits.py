__author__ = 'liuxiyun'
import math
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        count = 0
        for i in range(0,int(math.log(num,2))+1):
            res += map(lambda x: x+1,res)
        return res[:num+1]


c = Solution()
print c.countBits(5)