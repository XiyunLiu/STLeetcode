__author__ = 'liuxiyun'

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        board = [string.split() for string in board]
        self.hasWord = []
        trie = self.buildTrie(words)
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.helper(i,j,trie,board)
        return self.hasWord

    def buildTrie(self, words):
        trie = {}
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['word'] = word
        return trie

    def helper(self,i,j,trieNode,board):
        c = board[i][j]
        if c == '#' or c not in trieNode:
            return
        trieNode = trieNode[c]
        if 'word' in trieNode:
            self.hasWord.append(trieNode['word'])
            trieNode.pop('word')

        board[i][j] = '#'
        if i > 0 :
            self.helper(i-1,j,trieNode,board)
        if i < len(board)-1:
            self.helper(i+1,j,trieNode,board)
        if j > 0:
            self.helper(i,j-1,trieNode,board)
        if j < len(board[i])-1:
            self.helper(i,j+1,trieNode,board)
        board[i][j] = c

c = Solution()
# print c.findWords(["oaan","etae","ihkr","iflv"],["oath","pea","eat","rain"])
# print c.findWords(["aa"],["aaa"])
# print c.findWords(["ab","aa"],["bab","aaaa","aaba"])
print c.findWords(["b","a","b","b","a"],["baa","abba","baab","aba","a"])