__author__ = 'liuxiyun'
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix == []:
            return []
        m, n = len(matrix), len(matrix[0])
        minLength = min(m,n)
        for edge in range((minLength+1)/2):
            print "edge",edge
            for j in range(edge, n-edge):
                print "1.",matrix[edge][j]
                res.append(matrix[edge][j])
            for i in range(edge+1, m-edge):
                print "2.",matrix[i][n-1-edge]
                res.append(matrix[i][n-1-edge])
            if minLength%2 == 1 and edge == (minLength+1)/2-1:
                break
            for j in range(n-2-edge,edge-1,-1):
                print '3.',matrix[m-1-edge][j]
                res.append(matrix[m-1-edge][j])
            for i in range(m-2-edge,edge,-1):
                print "4.", matrix[i][edge]
                res.append(matrix[i][edge])
        return res
c = Solution()
print c.spiralOrder([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]])
print c.spiralOrder([[ 1, 2, 3, 4], [ 5,6,7,8],[9,10,11,12]])
print c.spiralOrder([[6,9,7]])
print c.spiralOrder([[3],[2]])
print c.spiralOrder([[7],[9],[6]])