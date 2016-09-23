class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == [] or board[0] == []:
            return
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        for i in range(self.m):
            for j in range(self.n):
                neighbor = self.countNeighbor(i,j)
                if self.board[i][j] == 1:
                    if neighbor != 3 and neighbor != 2: # 1 to 0
                        self.board[i][j] = 3
                else:
                    if neighbor == 3: # 0 to 1
                        self.board[i][j] = 2
        for i in range(0,self.m):
            for j in range(0,self.n):
                if self.board[i][j] == 3:
                    self.board[i][j] = 0
                elif self.board[i][j] == 2:
                    self.board[i][j] = 1

    def countNeighbor(self,i,j):
        numOfLiveNeighbor = 0
        if j>0:
            numOfLiveNeighbor += self.board[i][j-1]%2
        if j<self.n-1:
            numOfLiveNeighbor += self.board[i][j+1]%2
        if i>0:
            numOfLiveNeighbor += self.board[i-1][j]%2
            if j>0:
                numOfLiveNeighbor += self.board[i-1][j-1]%2
            if j<self.n-1:
                numOfLiveNeighbor += self.board[i-1][j+1]%2
        if i<self.m-1:
            numOfLiveNeighbor += self.board[i+1][j]%2
            if j>0:
                numOfLiveNeighbor += self.board[i+1][j-1]%2
            if j<self.n-1:
                numOfLiveNeighbor += self.board[i+1][j+1]%2
        return numOfLiveNeighbor

