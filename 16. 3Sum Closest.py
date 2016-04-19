class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 270000
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            j = i+1
            k = n-1
            while j<k:
                temp = nums[i]+nums[j]+nums[k]
                if abs(temp-target)<abs(result-target):
                    result = temp
                if temp == target:
                    return result
                if temp < target:
                    j+=1
                else:
                    k-=1
        return result
c = Solution()
print c.threeSumClosest([1,1,-1,-1,3],-1)

