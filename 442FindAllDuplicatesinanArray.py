"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for index in range(len(nums)):
            nums[abs(nums[index])-1] = -nums[abs(nums[index])-1] 
            if nums[abs(nums[index])-1] > 0:
                ans.append(abs(nums[index]))
    
        
        return ans
        
