__author__ = 'liuxiyun'
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        numIsland = 0
        self.grid = grid
        self.visited = [[False for i in xrange(0, len(grid[0]))] for j in xrange(0, len(grid))]
        for i in xrange(0, len(grid)):
            for j in xrange(0, len(grid[i])):
                if self.visited[i][j] or self.grid[i][j] == '0':
                    continue
                numIsland += 1
                self.explore(i,j)
        return numIsland

    def explore(self,i,j):
        if self.visited[i][j] or self.grid[i][j] == '0':
            return
        self.visited[i][j] = True
        if i > 0: # explore up
            self.explore(i-1,j)
        if i < len(self.grid)-1: # explore down
            self.explore(i+1,j)
        if j > 0: # explore left
            self.explore(i,j-1)
        if j < len(self.grid[i])-1: # explore right
            self.explore(i,j+1)

