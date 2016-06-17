__author__ = 'liuxiyun'
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ans = []
        fuhao = '+-*'
        if input == '':
            return []
        for i in range(len(input)):
            if input[i] not in fuhao:
                continue
            left,right = input[:i],input[i+1:]
            left_res = self.diffWaysToCompute(left)
            right_res = self.diffWaysToCompute(right)
            for l in left_res:
                for r in right_res:
                    if input[i] == '+':
                        tmp = int(l)+int(r)
                    elif input[i] == '-':
                        tmp = int(l)-int(r)
                    else:
                        tmp = int(l)*int(r)
                    ans.append(tmp)
        if ans == []:
            ans.append(int(input))
        return ans