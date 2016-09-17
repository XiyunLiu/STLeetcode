from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = 0
        j = 0
        maxWindow = 0
        dic = defaultdict(int)
        while i < len(s):
            while i<len(s):
                dic[s[i]] += 1
                if len(dic) <= k:
                    print i
                    i += 1
                else:
                    break
            print s[j:i]
            maxWindow = max(maxWindow, i-j)
            while j<i:
                dic[s[j]] -= 1
                if dic[s[j]] == 0:
                    dic.pop(s[j])
                    print dic
                if len(dic) > k:
                    j += 1
                else:
                    break
            i += 1
            j += 1
        return maxWindow
c = Solution()
c.lengthOfLongestSubstringKDistinct("bacc",2)