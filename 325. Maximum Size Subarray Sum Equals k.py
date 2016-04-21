__author__ = 'liuxiyun'
# Idea: hashmap
# Ini a list of the sum of all ele before i
# Hashmap records the sum with index

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_sum=[0]
        max_len = 0
        dic = {}
        for i in xrange(0,len(nums)):
            pre_sum.append(nums[i]+pre_sum[i])
        for j in xrange(len(pre_sum)):
            if pre_sum[j] not in dic:
                dic[pre_sum[j]]=j
            need = pre_sum[j]-k
            if need in dic:
                max_len = max(max_len, j-dic[need])
        return max_len