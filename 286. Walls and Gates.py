__author__ = 'liuxiyun'
from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms == [[]] or rooms == []:
            return
        queue = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append([i,j])
        while queue:
            i,j = queue.popleft()
            if i > 0 and rooms[i-1][j] == 2147483647:
                rooms[i-1][j] = rooms[i][j]+1
                queue.append([i-1,j])
            if j > 0 and rooms[i][j-1] == 2147483647:
                rooms[i][j-1] = rooms[i][j]+1
                queue.append([i,j-1])
            if j < len(rooms[0])-1 and rooms[i][j+1] == 2147483647:
                rooms[i][j+1] = rooms[i][j]+1
                queue.append([i,j+1])
            if i < len(rooms)-1 and rooms[i+1][j] == 2147483647:
                rooms[i+1][j] = rooms[i][j]+1
                queue.append([i+1,j])

            