class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        matched = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        matched[0][0] = True
        for i in range(0,len(p)):
            matched[0][i+1] = matched[0][i-1] and p[i] == '*'
        for i in range(0,len(s)):
            for j in range(0,len(p)):
                if p[j] == '.' or p[j] == s[i]:
                    matched[i+1][j+1] = matched[i][j]
                elif p[j] == '*':
                    if p[j-1] != '.' and p[j-1] != s[i]:
                        matched[i+1][j+1] = matched[i+1][j-1]
                    else:
                        matched[i+1][j+1] = matched[i+1][j-1] or matched[i+1][j] or matched[i][j+1]
        return matched[len(s)][len(p)]

