class Solution(object):
    def removeDuplicates(self, nums):
       
        l = 0 
        for i in nums:
            if l < 2 or i != nums[l - 2]: 
                nums[l] = i  
                l += 1  
        
        return l
