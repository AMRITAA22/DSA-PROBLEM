class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = 0  
        for i, num in enumerate(nums):
            if i > last:
                return False 
            last = max(last, i + num) 
        return True
