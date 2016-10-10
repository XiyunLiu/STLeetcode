__author__ = 'liuxiyun'
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        maxKill = 0
        m = len(grid)
        n = len(grid[0])
        left = [[0 for _ in range(0,n)] for x in range(0,m)]
        right = [[0 for _ in range(0,n)] for x in range(0,m)]
        up = [[0 for _ in range(0,n)] for x in range(0,m)]
        down = [[0 for _ in range(0,n)] for x in range(0,m)]
        maxKill = 0
        for i in range(1,m):
            for j in range(0,n):
                up[i][j] = 0 if grid[i-1][j] == 'W' else (up[i-1][j] + 1 if grid[i-1][j] == 'E' else up[i-1][j])
                down[m-1-i][j] = 0 if grid[m-i][j] == 'W' else (down[m-i][j] + 1 if grid[m-i][j] == 'E' else down[m-i][j])
                # print grid[m-i][j],down
        for i in range(0,m):
            for j in range(1,n):
                left[i][j] = 0 if grid[i][j-1] == 'W' else (left[i][j-1] + 1 if grid[i][j-1] == 'E' else left[i][j-1])
                right[i][n-1-j] = 0 if grid[i][n-j] == 'W' else (right[i][n-j] + 1 if grid[i][n-j] == 'E' else right[i][n-j])
                # print i,j-1,grid[i][j-1],left
        print up
        print down
        print left
        print right
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == '0':
                    maxKill = max(maxKill, up[i][j] + down[i][j] + left[i][j] + right[i][j])
        return maxKill
c = Solution()
print c.maxKilledEnemies(["0E00","E0WE","0E00"])
print c.maxKilledEnemies(["W","E","W","0","E"])