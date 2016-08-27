class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.listOfPoss = []
        self.end = len(num)
        self.num = num
        self.helper([],0)
        # print self.listOfPoss
        self.res = []
        for poss in self.listOfPoss:
            if self.calculation(poss)==target:
                self.res.append(''.join(poss))
        return self.res
        
    def helper(self,temp,start):
        if start == self.end:
            if len(temp)>2:
                self.listOfPoss.append(temp[:])
            return
        for i in range(start,self.end):
            if i == self.end-1:
                self.helper(temp+[self.num[start:i+1]],i+1)
                continue
            self.helper(temp+[self.num[start:i+1]]+['+'],i+1)
            self.helper(temp+[self.num[start:i+1]]+['-'],i+1)
            self.helper(temp+[self.num[start:i+1]]+['*'],i+1)
            if i==start and self.num[i]=='0':
                break
    
    def calculation(self,listOfStr):
        # print listOfStr
        res = 0
        i = 0
        fuhao = '+'
        while i<len(listOfStr):
            temp = int(listOfStr[i])
            j = i+1
            while j<len(listOfStr) and listOfStr[j] == '*':
                temp *= int(listOfStr[j+1])
                j += 2
            if fuhao == '+':
                res += temp
            else:
                res -= temp
            i = j+1
            if j<len(listOfStr):
                fuhao = listOfStr[j]
        # print listOfStr,res
        return res

c = Solution()
print c.addOperators('3456237490',9191)
# print c.calculation(['1','+','2'])