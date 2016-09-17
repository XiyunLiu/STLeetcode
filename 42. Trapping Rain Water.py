class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
        leftMaxHeight = [height[0] for i in range(len(height))]
        rightMaxHeight = [height[-1] for j in range(len(height))]
        
        for i in range(1,len(height)):
            j = len(height)-i-1
            leftMaxHeight[i] = max(leftMaxHeight[i-1],height[i-1])
            rightMaxHeight[j] = max(rightMaxHeight[j+1],height[j+1])

        total = 0
        for i in range(1,len(height)-1):
            wall = min(leftMaxHeight[i],rightMaxHeight[i])
            total += max(wall-height[i],0)
            
        return total