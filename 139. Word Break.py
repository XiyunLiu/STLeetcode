__author__ = 'liuxiyun'
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        isWord = [False for i in range(len(s)+1)]
        isWord[0] = True
        for i in range(0,len(s)):
            for j in range(i,-1,-1):
                if s[j:i+1] in wordDict and isWord[j]:
                    isWord[i+1] = True
                    break
        return isWord[-1]