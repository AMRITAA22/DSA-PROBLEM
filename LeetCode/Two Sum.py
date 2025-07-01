class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited={}
        for i,num in enumerate(nums):
            ans=target-num
            if ans in visited:
                return [visited[ans],i]
            visited[num]=i
