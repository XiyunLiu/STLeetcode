__author__ = 'liuxiyun'
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {"}" : "{", "]" : "[", ")" : "("}
        stack = []
        for char in s:
            if char not in dic:
                stack.append(char)
            else:
                if stack == []:
                    return False
                last = stack.pop()
                if dic[char] != last:
                    return False
        return stack == []