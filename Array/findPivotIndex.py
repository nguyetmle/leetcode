"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index 
is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Level: Easy
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    #iterate through each index 
    #check if left sum == right sum
    #right sum = total - left - nums[i]
        leftSum = 0
        total = sum(nums)
        for i in range(len(nums)):
            if leftSum == total - leftSum - nums[i]:
                return i
            leftSum += nums[i]
        
        return -1
