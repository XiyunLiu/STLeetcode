__author__ = 'liuxiyun'
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        addOne = 1
        for i in range(len(digits)-1, -1,-1):
            digits[i] += addOne
            if digits[i] == 10:
                digits[i] = 0
                addOne = 1
            else:
                addOne = 0
        if addOne == 1:
            digits.insert(0,1)
        return digits