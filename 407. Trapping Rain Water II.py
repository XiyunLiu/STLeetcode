__author__ = 'liuxiyun'
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        up = [[0 for y in range(len(heightMap[0]))] for x in range(len(heightMap))]
        down = [[0 for y in range(len(heightMap[0]))] for x in range(len(heightMap))]
        left = [[0 for y in range(len(heightMap[0]))] for x in range(len(heightMap))]
        right = [[0 for y in range(len(heightMap[0]))] for x in range(len(heightMap))]
        m,n = len(heightMap),len(heightMap[0])
        for i in range(0,m):
            for j in range(1,n):
                left[i][j] = max(left[i][j-1],heightMap[i][j-1])
                right[i][n-j-1] = max(right[i][n-j],heightMap[i][n-j])
        print left
        print right
        for j in range(0,n):
            for i in range(1,m):
                up[i][j] = max(up[i-1][j],heightMap[i-1][j])
                down[m-i-1][j] = max(down[m-i][j],heightMap[m-i][j])
        water = 0
        print up
        print down
        for i in range(0,m):
            for j in range(0,n):
                water += max(0,min(left[i][j],right[i][j],up[i][j],down[i][j])-heightMap[i][j])
        return water
c = Solution()
# print c.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
# print c.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]])

s = [[1,2],[1,5],[1,3],[0,2]]
s.sort(key = lambda x: x[0])