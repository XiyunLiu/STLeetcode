__author__ = 'liuxiyun'
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        longestPath = 0
        curPath = 0
        inputPath = input.split("\n")
        stack = []
        print inputPath
        for path in inputPath:
            level = path.count("\t")
            while len(stack) != level:
                pre = stack.pop()
                curPath -= (len(pre)+1)
            if '.' in path:
                longestPath = max(longestPath, curPath + len(path[level:]))
            else:
                stack.append(path[level:]) # \t is a whole thing, therefore the start index is not level*2, but level
                curPath += (len(path[level:])+1)
            print level, path[level:]
        return longestPath

c = Solution()
print c.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
