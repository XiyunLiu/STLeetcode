__author__ = 'liuxiyun'
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3:
            return 0
        res = 0
        left_max_height = [0 for i in range(len(height))]
        right_max_height = [0 for j in range(len(height))]
        left_max = height[0]
        right_max = height[-1]
        for i in range(1,len(height)):
            j = len(height)-1-i
            left_max_height[i] = left_max
            right_max_height[j] = right_max
            left_max = max(left_max,height[i])
            right_max = max(right_max,height[j])
        print left_max_height
        print right_max_height
        for i in range(1,len(height)-1):
            h = min(left_max_height[i],right_max_height[i])
            if h>height[i]:
                res+=h
                print i,h
        return res
c = Solution()
print c.trap([0,1,0,2,1,0,1,3,2,1,2,1])